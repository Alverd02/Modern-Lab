import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("9(Hoja2).csv",delimiter = ";")

x = df["angle"].tolist()
y1 = df["intensitat"].tolist()


x_new = []
y1_new = []



for k,i in zip(x,y1):
    y1_new.append(int(i))
    x_new.append(float(".".join(k.split(","))))


peaks, properties = sc.signal.find_peaks(y1_new,height = 56)


I = [y1_new[p]/sum([y1_new[p] for p in peaks]) for p in peaks]
print(I,[y1_new[p] for p in peaks])

#plt.annotate("(649,2036)",xy=(649,2036),    xytext=(649+ 300, 2036),arrowprops=dict(facecolor="red", arrowstyle="->"), fontsize=10, color="red")
plt.fill_between(x_new,y1_new,alpha = 1.0)
plt.plot([x_new[p] for p in peaks], [y1_new[p] for p in peaks], "ro", label="Peaks (500-1000)")
plt.xlabel("$theta(º)$")
plt.ylabel("Intensitat")

plt.grid()

plt.show()