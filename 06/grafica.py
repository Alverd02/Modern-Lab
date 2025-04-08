import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("5(Na2).csv",delimiter = ";")

x = df["lambda"].tolist()
y1 = df["comptes"].tolist()



y1_new = []



for k,i in zip(x,y1):
    y1_new.append(float(".".join(i.split(","))))



peaks, properties = sc.signal.find_peaks(y1_new,height = 250)
filtered_peaks = [p for p in peaks if 380<= x[p] <= 750]
print([x[p] for p in filtered_peaks],properties)
plt.annotate("(1569,206)",xy=(1569,206),    xytext=(1569+ 100, 206+300),arrowprops=dict(facecolor="red", arrowstyle="->"), fontsize=10, color="red")
plt.plot(x,y1_new)
plt.plot([x[p] for p in filtered_peaks], [y1_new[p] for p in filtered_peaks], "r.", label="Peaks")
plt.ylabel("Comptes")
plt.xlabel("$\lambda$ (nm)")

plt.grid()
plt.show()