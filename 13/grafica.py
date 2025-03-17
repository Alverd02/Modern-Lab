import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Asegúrate de especificar el separador correcto
df = pd.read_csv("practica 13b(Hoja2).csv", delimiter=';')
x = df["T"].tolist()
y = df["mob"].tolist()
#error = df["error"].tolist()
x_new = []
y_new = []
error_new = []
for i in x:
    x_new.append(float(".".join(i.split(","))))
for i in y:
    if type(i) == str:
        y_new.append(float(".".join(i.split(","))))

result = sc.stats.linregress(np.log(x_new[45:]),np.log(y_new[45:]))
#result2 = sc.stats.linregress(x2,polla)
#result3 = sc.stats.linregress(x3,y_new3)

print("(",result.slope,"+-",result.stderr,")x + ",result.intercept,"+-",result.intercept_stderr)

plt.ylabel('$ln(R^{-1})$')
plt.xlabel('ln(T)')
plt.scatter(np.log(x_new),np.log(y_new))
plt.plot(np.log(x_new),result.slope*(np.log(x_new))+result.intercept,"y",label = "y=-2.71x+16.77")
#plt.errorbar(x,y_new,yerr=error_new,ecolor="k",fmt='o')
plt.legend()
plt.grid()
plt.show()