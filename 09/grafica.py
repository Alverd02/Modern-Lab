import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("9(Hoja3).csv",delimiter = ";")

x = df["d"].tolist()
y1 = df["sin"].tolist()
y2 = df["error"].tolist()

x_new = []
y1_new = []
y2_new = []


for k,i,j in zip(x,y1,y2):
    x_new.append(int(k))
    y1_new.append(float(".".join(i.split(","))))
    y2_new.append(float(".".join(j.split(","))))

a = np.sum(np.array(x_new) * np.array(y1_new)) / np.sum(np.array(x_new) ** 2)
residuos = np.array(y1_new) - a * np.array(x_new)
sigma_a = np.sqrt(np.sum(residuos**2) / ((3 - 1) * np.sum(np.array(x_new)**2)))
print(a,sigma_a)

plt.errorbar(x_new,y1_new,fmt = "o",yerr=y2_new)
plt.plot(x_new,a*np.array(x_new),"r",label="y = 0.22x")

plt.ylabel("sin(theta)")
plt.xlabel("n")

plt.grid()
plt.legend()
plt.show()