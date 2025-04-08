import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Asegúrate de especificar el separador correcto
df = pd.read_csv("600_mitjana.csv", delimiter=';')
x = df["n"].tolist()
y = df["lambda"].tolist()
error = df["error"].tolist()
x_new = []
y_new = []
error_new = []
for i in x:
    x_new.append(float(".".join(i.split(","))))
for i in y:
    if type(i) == str:
        y_new.append(float(".".join(i.split(","))))
for i in error:
    if type(i) == str:
        error_new.append(float(".".join(i.split(","))))


result = sc.stats.linregress(x_new,y_new)
a = np.sum(np.array(x_new) * np.array(y_new)) / np.sum(np.array(x_new) ** 2)
residuos = np.array(y_new) - a * np.array(x_new)
sigma_a = np.sqrt(np.sum(residuos**2) / ((3 - 1) * np.sum(np.array(x_new)**2)))
print(a,sigma_a)

plt.ylabel('$\lambda (nm)$')
plt.xlabel('$n^2/(n^2-4)$')
#plt.scatter(x_new,y_new)
plt.errorbar(x_new,y_new,yerr=error_new,ecolor="k",fmt='o')
plt.plot(x_new,a*np.array(x_new),"r",label = "y=365.7x")
plt.legend()
plt.grid()
plt.show()