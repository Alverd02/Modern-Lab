import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("1(Hoja6).csv",delimiter = ";")

x = df["t"].tolist()
y1 = df["ln"].tolist()
y2 = df["errorln"].tolist()

x_new = []
y1_new = []
y2_new = []


for k,i,j in zip(x,y1,y2):
    x_new.append(float(".".join(k.split(","))))
    y1_new.append(float(".".join(i.split(","))))
    y2_new.append(float(".".join(j.split(","))))


def exponential(x,a,b):
    return a * np.exp(b*np.array(x))

result = sc.stats.linregress(x_new,y1_new)
params, covariance = sc.optimize.curve_fit(exponential, x_new,y1_new, p0=(max(y1_new), -0.0045),sigma = 0.01)
perr = np.sqrt(np.diag(covariance))

a,b = params
print(result.slope,result.intercept,result.stderr)
plt.errorbar(x_new,y1_new,fmt = "o",yerr=y2_new)
plt.plot(x_new,result.slope*np.array(x_new)+result.intercept,"r",label="y = -0.077x + 2.53")
plt.ylabel("ln(A)")
plt.xlabel("$gruix(g/cm^2)$")

plt.grid()
plt.legend()
plt.show()