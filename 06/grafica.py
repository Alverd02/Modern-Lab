import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("6(Hoja2).csv",delimiter = ";")

x = df["B(mT)"].tolist()
y1 = df["mu"].tolist()
y2 = df["error_mu"].tolist()


a = np.sum(np.array(x) * np.array(y1)) / np.sum(np.array(x) ** 2)
residuos = np.array(y1) - a * np.array(x)
sigma_a = np.sqrt(np.sum(residuos**2) / ((3 - 1) * np.sum(np.array(x)**2)))
print(a,sigma_a)

plt.errorbar(x,y1,fmt = "o",yerr=y2)
plt.plot(x,a*np.array(x),"r",label="y = 0.078x")
plt.ylabel("$\Delta\\nu$(T)")
plt.xlabel("B(mT)")

plt.grid()
plt.legend()
plt.show()