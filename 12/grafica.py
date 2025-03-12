import scipy as sc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Asegúrate de especificar el separador correcto
df = pd.read_csv("practica 12(Hoja4).csv", delimiter=';')
x = df["B"].tolist()
y = df["Vh"].tolist()
x2 = df["B2"].tolist()
y2 = df["Vh2"].tolist()
x3 = df["B3"].tolist()
y3 = df["Vh3"].tolist()
x_new = []
y_new = []
x_new2 = []
y_new2 = []
x_new3 = []
y_new3 = []
#for i in x:
    #x_new.append(float(".".join(i.split(","))))
for i in y:
    if type(i) == str:
        y_new.append(float(".".join(i.split(","))))

#for i in x:
    #x_new.append(float(".".join(i.split(","))))
for j in y2:
    if type(j) == str:
        y_new2.append(float(".".join(j.split(","))))
    #for i in x:
    #x_new.append(float(".".join(i.split(","))))
for k in y3:
    if type(k) == str:
        y_new3.append(float(".".join(k.split(","))))

x3=[l*10 for l in x3]
x2=[l*7.5 for l in x2]
x=[l*5 for l in x]

polla = []

for m in range(len(y_new2)):
    polla.append(y_new2[-1-m])


result = sc.stats.linregress(x+x2+x3,y_new+polla+y_new3)
#result2 = sc.stats.linregress(x2,polla)
#result3 = sc.stats.linregress(x3,y_new3)

print("Im = 5 A=>","(",result.slope,"+-",result.stderr,")x + ",result.intercept,"+-",result.intercept_stderr)
#print("Im = 7.5 A=>","(",result2.slope,"+-",result2.stderr,")x + ",result2.intercept,"+-",result2.intercept_stderr)
#print("Im = 10 A=>","(",result3.slope,"+-",result3.stderr,")x + ",result3.intercept,"+-",result3.intercept_stderr)



#fig, axs = plt.subplots(3)
#fig.supylabel('$V(mV)$')
#fig.supxlabel('$B(mT)$')
#axs[0].scatter(x,y_new)
#axs[1].scatter(x2,polla)
#axs[2].scatter(x3,y_new3)
#axs[0].plot(x,result.slope*np.array(x)+result.intercept,"g")
#axs[1].plot(x2,result2.slope*np.array(x2)+result2.intercept,"g")
#axs[2].plot(x3,result3.slope*np.array(x3)+result3.intercept,"g")
#axs[1].grid()
#axs[2].grid()
#axs[0].grid()

plt.ylabel('$V_H(mV)$')
plt.xlabel('$I_mB(AmT)$')
plt.scatter(x,y_new,label="$I_m = 5 A$")
plt.scatter(x2,polla,label="$I_m = 7.5 A$")
plt.scatter(x3,y_new3,label="$I_m = 10 A$")
plt.plot(x+x2+x3,result.slope*np.array(x+x2+x3)+result.intercept,"y")
plt.legend()
plt.grid()
plt.show()