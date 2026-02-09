import pandas as pd

data = [
    ("gender", "Sexo biológico", "Female", "Feminino"),
    ("gender", "Sexo biológico", "Male", "Masculino"),

    ("family_history", "Histórico familiar de excesso de peso", "yes", "Há histórico"),
    ("family_history", "Histórico familiar de excesso de peso", "no", "Não há histórico"),

    ("favc", "Consumo frequente de alimentos altamente calóricos", "yes", "Sim"),
    ("favc", "Consumo frequente de alimentos altamente calóricos", "no", "Não"),

    ("fcvc", "Frequência de consumo de vegetais nas refeições", 1, "Raramente"),
    ("fcvc", "Frequência de consumo de vegetais nas refeições", 2, "Às vezes"),
    ("fcvc", "Frequência de consumo de vegetais nas refeições", 3, "Sempre"),

    ("ncp", "Número de refeições principais por dia", 1, "Uma refeição"),
    ("ncp", "Número de refeições principais por dia", 2, "Duas refeições"),
    ("ncp", "Número de refeições principais por dia", 3, "Três refeições"),
    ("ncp", "Número de refeições principais por dia", 4, "Quatro ou mais refeições"),

    ("caec", "Consumo de alimentos entre as refeições", "no", "Não consome"),
    ("caec", "Consumo de alimentos entre as refeições", "Sometimes", "Às vezes"),
    ("caec", "Consumo de alimentos entre as refeições", "Frequently", "Frequentemente"),
    ("caec", "Consumo de alimentos entre as refeições", "Always", "Sempre"),

    ("smoke", "Hábito de fumar", "yes", "Fuma"),
    ("smoke", "Hábito de fumar", "no", "Não fuma"),

    ("ch2o", "Consumo diário de água", 1, "Menos de 1 litro/dia"),
    ("ch2o", "Consumo diário de água", 2, "Entre 1 e 2 litros/dia"),
    ("ch2o", "Consumo diário de água", 3, "Mais de 2 litros/dia"),

    ("scc", "Monitora a ingestão calórica diária", "yes", "Sim"),
    ("scc", "Monitora a ingestão calórica diária", "no", "Não"),

    ("faf", "Frequência semanal de atividade física", 0, "Nenhuma"),
    ("faf", "Frequência semanal de atividade física", 1, "1–2 vezes por semana"),
    ("faf", "Frequência semanal de atividade física", 2, "3–4 vezes por semana"),
    ("faf", "Frequência semanal de atividade física", 3, "5 vezes por semana ou mais"),

    ("tue", "Tempo diário usando dispositivos eletrônicos", 0, "0–2 horas/dia"),
    ("tue", "Tempo diário usando dispositivos eletrônicos", 1, "3–5 horas/dia"),
    ("tue", "Tempo diário usando dispositivos eletrônicos", 2, "Mais de 5 horas/dia"),

    ("calc", "Consumo de bebida alcoólica", "no", "Não bebe"),
    ("calc", "Consumo de bebida alcoólica", "Sometimes", "Às vezes"),
    ("calc", "Consumo de bebida alcoólica", "Frequently", "Frequentemente"),
    ("calc", "Consumo de bebida alcoólica", "Always", "Sempre"),

    ("mtrans", "Meio de transporte habitual", "Automobile", "Carro"),
    ("mtrans", "Meio de transporte habitual", "Motorbike", "Moto"),
    ("mtrans", "Meio de transporte habitual", "Bike", "Bicicleta"),
    ("mtrans", "Meio de transporte habitual", "Public_Transportation", "Transporte público"),
    ("mtrans", "Meio de transporte habitual", "Walking", "A pé"),

    ("obesity", "Nível de obesidade (coluna alvo)", "Insufficient_Weight", "Abaixo do peso"),
    ("obesity", "Nível de obesidade (coluna alvo)", "Normal_Weight", "Peso normal"),
    ("obesity", "Nível de obesidade (coluna alvo)", "Overweight_Level_I", "Sobrepeso nível I"),
    ("obesity", "Nível de obesidade (coluna alvo)", "Overweight_Level_II", "Sobrepeso nível II"),
    ("obesity", "Nível de obesidade (coluna alvo)", "Obesity_Type_I", "Obesidade tipo I"),
    ("obesity", "Nível de obesidade (coluna alvo)", "Obesity_Type_II", "Obesidade tipo II"),
    ("obesity", "Nível de obesidade (coluna alvo)", "Obesity_Type_III", "Obesidade tipo III"),
]

df_dict = pd.DataFrame(
    data,
    columns=["cd_variavel", "ds_variavel", "nr_categoria", "ds_categoria"]
)
