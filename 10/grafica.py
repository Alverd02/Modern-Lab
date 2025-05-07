import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df1 = pd.read_csv("DadesModernaP10(Hoja1).csv",delimiter = ";")
df2 = pd.read_csv("DadesModernaP10(Hoja2).csv",delimiter = ";")


x1 = df1["Temp"].tolist()
y1 = df1["PujadaPrima"].tolist()
x2 = df2["Temp"].tolist()
y2 = df2["BaixadaPrima"].tolist()


x1_new = []
y1_new = []
x2_new = []
y2_new = []


for a,b in zip(x1,y1):
    y1_new.append(float(".".join(b.split(","))))
    x1_new.append(float(".".join(a.split(","))))
    
for a,b in zip(x2,y2):
    
    y2_new.append(float(".".join(b.split(","))))
    x2_new.append(float(".".join(a.split(","))))

maxC = min(y2_new)
index = y2_new.index(maxC)
print(maxC,index)

result1 = sc.stats.linregress(x2_new[60:84],y2_new[60:84])
result2 = sc.stats.linregress(x2_new[84:100],y2_new[84:100])

print((result1.slope,result1.stderr),(result1.intercept,result1.intercept_stderr))
print((result2.slope,result2.stderr),(result2.intercept,result2.intercept_stderr))
plt.scatter(x2_new[:84],y2_new[:84])
plt.plot(x2_new[50:90],result1.slope*np.array(x2_new[50:90])+result1.intercept,"r",label = "y =-0.00164x+0.085 ")
plt.scatter(x2_new[84:],y2_new[84:])
plt.plot(x2_new[84:],result2.slope*np.array(x2_new[84:])+result2.intercept,"k",label = "y =0.00124x-0.061 ")


#plt.errorbar(x1_new[:98],y1_new[:98],xerr=0.1,yerr=error[:98],color ="k",fmt = "o")
#plt.errorbar(x1_new[98:],y1_new[98:],xerr=0.1,yerr=error[98:],color ="k",fmt = "o")


plt.ylabel("1/C(1/pF)")
plt.xlabel("T(ºC)")

plt.grid()
plt.legend()
plt.show()