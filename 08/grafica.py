import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Libro(tungste).csv",delimiter = ";")



x = df["lambda"].tolist()
y1 = df["Conjunt 3"].tolist()



x_new = []
y1_new = []



for a,b in zip(x,y1):
    y1_new.append(int(b))
    x_new.append(float(".".join(a.split(","))))


#result = sc.stats.linregress(x_new,y1_new)


peaks, properties = sc.signal.find_peaks(y1_new,height = 470)
print([x_new[p] for p in peaks])
plt.plot([x_new[p] for p in peaks], [y1_new[p] for p in peaks], "ro", label="Peaks")
#plt.annotate("$\lambda = 128.48pm $",xy=(128.48,0.05),    xytext=(128.48+10,0.05),arrowprops=dict(facecolor="red", arrowstyle="->"), fontsize=10, color="red")
plt.plot(x_new,y1_new,"-.")
plt.plot(167.679,219.7,"ro")
#plt.plot(x_new,result.slope*np.array(x_new)+result.intercept,"r",label = "y = 0.00322-0.009")
#plt.plot(128.48,0.05,"o")
#plt.plot(x_new,y1_new,"-.",label = "Zn")

plt.ylabel("Intensitat")
plt.xlabel("$\lambda(pm)$")

plt.grid()
plt.legend()
plt.show()