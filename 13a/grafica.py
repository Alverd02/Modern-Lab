import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = []
y = []
z = []
errorx = []
errory = []
errorz = []
# Asegúrate de especificar el separador correcto
with open("P13_20250310_171049.dat") as file:
    for i in file.readlines():
        i = i.split(" , ")
        if len(i)<2:
            continue
        else:
            x.append(1/(float(i[0])+273))
            y.append(float(i[1]))
            z.append(float(i[2]))
            errorx.append(float(i[3]))
            errory.append(float(i[4]))
            errorz.append(float(i[5]))
        
sigma = [(2000*I)/(V) for I,V in zip(z[:165],errory[:165])]

result = sc.stats.linregress(x[:165],np.log(np.array(sigma)))
print("(",result.slope,"+-",result.stderr,")x + ",result.intercept,"+-",result.intercept_stderr)

plt.xlabel("$1/T(K^{-1})$")
plt.ylabel("$ln(\sigma)$")
plt.scatter(x[:165],np.log(np.array(sigma)))
plt.plot(x[:165],result.slope*np.array(x[:165])+result.intercept,"y",label = " y = -4210x+14.90")
plt.grid()
plt.legend()
plt.show()