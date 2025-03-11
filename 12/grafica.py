import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Asegúrate de especificar el separador correcto
df = pd.read_csv("practica 12(Hoja4).csv", delimiter=';')
x = df["B"].tolist()
y = df["Vh"].tolist()
x2 = df["B2"].tolist()
y2 = df["Vh2"].tolist()
x3 = df["B3"].tolist()
y3 = df["Vh3"].tolist()
x_new = []
y_new = []
x_new2 = []
y_new2 = []
x_new3 = []
y_new3 = []
#for i in x:
    #x_new.append(float(".".join(i.split(","))))
for i in y:
    if type(i) == str:
        y_new.append(float(".".join(i.split(","))))

#for i in x:
    #x_new.append(float(".".join(i.split(","))))
for j in y2:
    if type(j) == str:
        y_new2.append(float(".".join(j.split(","))))
    #for i in x:
    #x_new.append(float(".".join(i.split(","))))
for k in y3:
    if type(k) == str:
        y_new3.append(float(".".join(k.split(","))))


result = sc.stats.linregress(x,y_new)
result2 = sc.stats.linregress(x2,y_new2)
result3 = sc.stats.linregress(x3,y_new3)
print("Im = 5 A=>","(",result.slope,"+-",result.stderr,")x + ",result.intercept,"+-",result.intercept_stderr)
print("Im = 7.5 A=>","(",result2.slope,"+-",result2.stderr,")x + ",result2.intercept,"+-",result2.intercept_stderr)
print("Im = 10 A=>","(",result3.slope,"+-",result3.stderr,")x + ",result3.intercept,"+-",result3.intercept_stderr)

y_new3=[l*10 for l in y_new3]
y_new2=[l*7.5 for l in y_new2]
y_new=[l*5 for l in y_new]

polla = []

for m in range(len(y_new2)):
    polla.append(y_new2[-1-m])

plt.ylabel('$V_H(mV)$')
plt.xlabel('$I_mB(AmT)$')
plt.scatter(x,y_new)
plt.scatter(x2,polla)
plt.scatter(x3,y_new3)
plt.grid()
plt.show()