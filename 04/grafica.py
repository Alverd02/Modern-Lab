import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("4(Hoja5).csv",delimiter = ";")

x = df["energia"].tolist()
y1 = df["comptes"].tolist()


x_new = []
y1_new = []



for k,i in zip(x,y1):
    x_new.append(float(".".join(k.split(","))))
    y1_new.append(float(".".join(i.split(","))))

u = np.polyfit(x_new,y1_new,deg = 2)
y_pred = u[0] * np.array(x_new)**2 + u[1]* np.array(x_new) + u[2]

plt.scatter(x_new,y1_new)
plt.plot(x_new,y_pred,"r")
plt.xlabel("Energia(MeV)")
plt.ylabel("#/s")

plt.grid()
plt.legend()
plt.show()