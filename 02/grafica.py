import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("sodi.csv",delimiter = ";")

x = df["Channel"].tolist()
y1 = df["Impulses"].tolist()


x_new = []
y1_new = []



for k,i in zip(x,y1):
    x_new.append(int(k))
    y1_new.append(int(i))


peaks, properties = sc.signal.find_peaks(y1_new,height = 1750)
filtered_peaks = [p for p in peaks if 600<= x_new[p] <= 700]
print(filtered_peaks,properties)
plt.annotate("(649,2036)",xy=(649,2036),    xytext=(649+ 300, 2036),arrowprops=dict(facecolor="red", arrowstyle="->"), fontsize=10, color="red")
plt.fill_between(x_new,y1_new,alpha = 1.0)
plt.plot([x_new[p] for p in filtered_peaks], [y1_new[p] for p in filtered_peaks], "ro", label="Peaks (500-1000)")
plt.ylabel("Impulses")
plt.xlabel("Channel")

plt.grid()

plt.show()