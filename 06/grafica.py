import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("6(Hoja2).csv",delimiter = ";")

x = df["B(mT)"].tolist()
y1 = df["mu"].tolist()
y2 = df["error_mu"].tolist()



result = sc.stats.linregress(x,y1)

print([result.slope,result.stderr],[result.intercept,result.intercept_stderr])

plt.errorbar(x,y1,fmt = "o",yerr=y2)
plt.plot(x,result.slope*np.array(x)+result.intercept,"r",label="y = 0.04x + 24")
plt.ylabel("$\Delta\\nu$(T)")
plt.xlabel("B(mT)")

plt.grid()
plt.legend()
plt.show()