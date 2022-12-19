import pandas as pd

df_1 = pd.read_excel("resultados_busqueda_tomas.xlsx", sheet_name="Sheet1")
df_2 = pd.read_excel("resultados_busqueda_mateo.xlsx", sheet_name="Sheet1")
dif = df_2.compare(df_1)
int_df = pd.merge(df_1, df_2, on=["label", "id"])
print(dif)
yes, no, maybe, academic = 0, 0, 0, 0
for item in int_df["label"]:
    if item == "yes":
        yes += 1
    elif item == "no":
        no += 1
    elif item == "academic":
        academic += 1
    else:
        maybe += 1
print("Sí: " + str(yes))
print("No: " + str(no))
print("Maybe: " + str(maybe))
print("Academic: " + str(academic))


# Intercoder Reliability
from sklearn import metrics

print("Cohen Kappa Score: ", metrics.cohen_kappa_score(df_1["label"], df_2["label"]))
