import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Preditor de Obesidade", layout="centered")

st.title("🏥 Preditor de Nível de Obesidade")
st.write("Sistema de apoio à decisão médica baseado em Machine Learning.")

model = joblib.load("model_obesity.joblib")

# Inputs
gender = st.selectbox("Gênero", ["Female", "Male"])
age = st.number_input("Idade", 14, 80, 25)
height = st.number_input("Altura (cm)", 120, 220, 170)
weight = st.number_input("Peso (kg)", 30.0, 200.0, 70.0)

family_history = st.selectbox("Histórico familiar de excesso de peso?", ["yes", "no"])
favc = st.selectbox("Alimentos altamente calóricos com frequência?", ["yes", "no"])

fcvc = st.slider("Consumo de vegetais (1-3)", 1, 3, 2)
ncp = st.slider("Refeições principais por dia (1-4)", 1, 4, 3)

caec = st.selectbox("Come entre refeições?", ["no","Sometimes","Frequently","Always"])
smoke = st.selectbox("Fuma?", ["yes","no"])
ch2o = st.slider("Água por dia (1-3)", 1, 3, 2)

scc = st.selectbox("Monitora calorias?", ["yes","no"])
faf = st.slider("Atividade física (0-3)", 0, 3, 1)
tue = st.slider("Tempo em telas (0-2)", 0, 2, 1)

calc = st.selectbox("Consumo de álcool", ["no","Sometimes","Frequently","Always"])
mtrans = st.selectbox("Transporte", ["Automobile","Motorbike","Bike","Public_Transportation","Walking"])

# Feature engineering
bmi = weight / ((height/100)**2)

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
    "gender","age","height","weight","family_history","favc","fcvc","ncp","caec",
    "smoke","ch2o","scc","faf","tue","calc","mtrans","bmi"
]

# garante a mesma ordem do treino
data = data[FEATURE_ORDER]

# ajuda a validar que o peso está sendo considerado
st.caption(f"BMI calculado: {bmi:.2f}")
st.caption(f"Peso: {weight} kg | Altura: {height} cm")


if st.button("Prever"):
    pred = model.predict(data)[0]
    st.success(f"Predição do modelo: **{pred}**")

    # Mostrar probabilidades (se disponível)
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(data)[0]
        classes = model.classes_
        df_proba = pd.DataFrame({"classe": classes, "probabilidade": proba}) \
                    .sort_values("probabilidade", ascending=False)
        st.write("Probabilidades por classe:")
        st.dataframe(df_proba, use_container_width=True)

