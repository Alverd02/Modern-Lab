import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Libro(lamda(Z)).csv",delimiter = ";")



x = df["Z"].tolist()
y1 = df["lambda2"].tolist()



x_new = []
y1_new = []



for a,b in zip(x,y1):
    x_new.append(int(a))
    y1_new.append(float(".".join(b.split(","))))


result = sc.stats.linregress(x_new,y1_new)

#plt.annotate("$\lambda = 128.48pm $",xy=(128.48,0.05),    xytext=(128.48+10,0.05),arrowprops=dict(facecolor="red", arrowstyle="->"), fontsize=10, color="red")
plt.scatter(x_new,y1_new)
plt.plot(x_new,result.slope*np.array(x_new)+result.intercept,"r",label = "y = 0.00322-0.009")
#plt.plot(128.48,0.05,"o")
#plt.plot(x_new,y1_new,"-.",label = "Zn")

plt.ylabel("$\lambda^{-1/2}(1/pm^{-1/2})$")
plt.xlabel("Z")

plt.grid()
plt.legend()
plt.show()