import streamlit as st
import pandas as pd
import joblib
from dicionario import df_dict

st.set_page_config(page_title="Preditor de Obesidade", layout="centered")

st.title("🏥 Preditor de Nível de Obesidade")
st.write("Sistema de apoio à decisão médica baseado em Machine Learning.")

model = joblib.load("model_obesity.joblib")

# =====================================================
# CRIAÇÃO DOS MAPAS A PARTIR DO DF_DICT
# =====================================================
def build_maps(df_dict, var):
    dfv = df_dict[df_dict["cd_variavel"] == var].copy()
    # EN -> PT (ex.: "Male" -> "Masculino")
    en_to_pt = dict(zip(dfv["nr_categoria"], dfv["ds_categoria"]))
    # PT -> EN (ex.: "Masculino" -> "Male")
    pt_to_en = {v: k for k, v in en_to_pt.items()}
    # opções em PT na ordem do dicionário
    options_pt = dfv["ds_categoria"].tolist()
    return options_pt, pt_to_en, en_to_pt

gender_opts, gender_pt_to_en, _ = build_maps(df_dict, "gender")
fh_opts, fh_pt_to_en, _ = build_maps(df_dict, "family_history")
favc_opts, favc_pt_to_en, _ = build_maps(df_dict, "favc")
caec_opts, caec_pt_to_en, _ = build_maps(df_dict, "caec")
smoke_opts, smoke_pt_to_en, _ = build_maps(df_dict, "smoke")
scc_opts, scc_pt_to_en, _ = build_maps(df_dict, "scc")
calc_opts, calc_pt_to_en, _ = build_maps(df_dict, "calc")
mtrans_opts, mtrans_pt_to_en, _ = build_maps(df_dict, "mtrans")

# Tradução do alvo (EN -> PT) para mostrar o resultado final
_, _, obesity_en_to_pt = build_maps(df_dict, "obesity")

# =====================================================
# INPUTS (INTERFACE EM PORTUGUÊS -> MODELO EM INGLÊS)
# =====================================================

# Gênero
gender_pt = st.selectbox("Gênero", gender_opts)
gender = gender_pt_to_en[gender_pt]

# Idade / Altura / Peso
age = st.number_input("Idade", 14, 80, 25)
height = st.number_input("Altura (cm)", 120, 220, 170)
weight = st.number_input("Peso (kg)", 30.0, 200.0, 70.0)

# Histórico familiar
family_history_pt = st.selectbox("Histórico familiar de excesso de peso?", fh_opts)
family_history = fh_pt_to_en[family_history_pt]

# Alimentos calóricos (FAVC)
favc_pt = st.selectbox("Alimentos altamente calóricos com frequência?", favc_opts)
favc = favc_pt_to_en[favc_pt]

# FCVC / NCP (mantidos como sliders numéricos)
fcvc = st.slider("Consumo de vegetais (1-3)", 1, 3, 2)
ncp = st.slider("Refeições principais por dia (1-4)", 1, 4, 3)

# CAEC
caec_pt = st.selectbox("Come entre refeições?", caec_opts)
caec = caec_pt_to_en[caec_pt]

# SMOKE
smoke_pt = st.selectbox("Fuma?", smoke_opts)
smoke = smoke_pt_to_en[smoke_pt]

# CH2O (mantido como slider numérico)
ch2o = st.slider("Água por dia (1-3)", 1, 3, 2)

# SCC
scc_pt = st.selectbox("Monitora calorias?", scc_opts)
scc = scc_pt_to_en[scc_pt]

# FAF / TUE (mantidos como sliders numéricos)
faf = st.slider("Atividade física (0-3)", 0, 3, 1)
tue = st.slider("Tempo em telas (0-2)", 0, 2, 1)

# CALC
calc_pt = st.selectbox("Consumo de álcool", calc_opts)
calc = calc_pt_to_en[calc_pt]

# MTRANS
mtrans_pt = st.selectbox("Transporte", mtrans_opts)
mtrans = mtrans_pt_to_en[mtrans_pt]

# =====================================================
# FEATURE ENGINEERING
# =====================================================
bmi = weight / ((height / 100) ** 2)

data = pd.DataFrame([{
    "gender": gender,
    "age": int(age),
    "height": int(height),
    "weight": float(weight),
    "family_history": family_history,
    "favc": favc,
    "fcvc": int(fcvc),
    "ncp": int(ncp),
    "caec": caec,
    "smoke": smoke,
    "ch2o": int(ch2o),
    "scc": scc,
    "faf": int(faf),
    "tue": int(tue),
    "calc": calc,
    "mtrans": mtrans,
    "bmi": float(bmi)
}])

FEATURE_ORDER = [
    "gender", "age", "height", "weight", "family_history", "favc", "fcvc", "ncp", "caec",
    "smoke", "ch2o", "scc", "faf", "tue", "calc", "mtrans", "bmi"
]

# garante a mesma ordem do treino
data = data[FEATURE_ORDER]

# ajuda a validar que o peso está sendo considerado
st.caption(f"BMI calculado: {bmi:.2f}")
st.caption(f"Peso: {weight} kg | Altura: {height} cm")

# =====================================================
# PREDIÇÃO
# =====================================================
if st.button("Prever"):
    pred = model.predict(data)[0]
    pred_pt = obesity_en_to_pt.get(pred, pred)
    st.success(f"Predição do modelo: **{pred_pt}**")

    # Mostrar probabilidades (se disponível)
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(data)[0]
        classes = model.classes_
        df_proba = pd.DataFrame({"classe": classes, "probabilidade": proba}) \
            .sort_values("probabilidade", ascending=False)

        # traduz classes para PT na tabela também
        df_proba["classe"] = df_proba["classe"].map(lambda x: obesity_en_to_pt.get(x, x))

        st.write("Probabilidades por classe:")
        st.dataframe(df_proba, use_container_width=True)

    st.info("Observação: este sistema é um apoio à decisão e não substitui avaliação clínica.")
