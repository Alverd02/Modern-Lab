import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("practica 14(Hoja2).csv",delimiter = ";")

x = df["longitud d'ona (nm)"].tolist()
y1 = df["tensio"].tolist()
y2 = df["tensioA"].tolist()
y3 = df["tensioB"].tolist()

y1_new = []
y2_new = []
y3_new = []
error = []
for i,j,k in zip(y1,y2,y3):
    y1_new.append(float(".".join(i.split(","))))
    y2_new.append(float(".".join(j.split(","))))
    y3_new.append(float(".".join(k.split(","))))
    error.append(0.9)

T1 = abs(np.array(y2_new)/np.array(y1_new))
T2 = abs(np.array(y3_new)/np.array(y1_new))

result = sc.stats.linregress(1.24*10**(3)/np.array(x[36:47]),np.sqrt (np.log(0.91/np.array(T2[36:47])*50)))
result2 = sc.stats.linregress(1.24*10**(3)/np.array(x[59:70]),np.sqrt (np.log(0.91/np.array(T2[59:70])*50)))
print("slope: ",result.slope,"+-",result.stderr,"intercept: ",result.intercept,"+-",result.intercept_stderr)
print("slope: ",result2.slope,"+-",result2.stderr,"intercept: ",result2.intercept,"+-",result2.intercept_stderr)

a = np.sqrt(np.log(0.91/np.array(T2)*50))


plt.scatter((1.24*10**(3))/np.array(x), np.sqrt(np.log(0.91/np.array(T2)*50)))
plt.plot((1.24*10**(3))/np.array(x[30:57]),(result.slope*1.24*10**(3))/np.array(x[30:57])+result.intercept,"y",label = "y=7.7x-6.9")
plt.plot((1.24*10**(3))/np.array(x[40:80]),(result2.slope*1.24*10**(3))/np.array(x[40:80])+result2.intercept,"k",label = "y=1.06x-0.84")
plt.ylabel("$\\alpha^{1/2}(nm^{-1/2})$")
plt.xlabel("$h\\nu(eV)$")

plt.grid()
plt.legend()
plt.show()