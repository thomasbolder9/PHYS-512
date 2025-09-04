import numpy as np
import matplotlib.pyplot as plt
plt.ion()

def fun(x):
    return 1/np.log(x)

x = np.linspace(2, 3, 21)
print(x)
y = fun(x)

plt.clf()
plt.plot(x,y)
plt.plot(x,y,'*')
plt.show()

xx = np.linspace(x[1], x[-2], 1001)
yy = 0*xx

 
#cubic fitting here
for i in range(len(xx)):
    for j in range(len(x)):
        if x[j]<i:
            ind=j
            break
    #trying to figure out which points we are going to use
    #i.e. find index of left hand neighbour
    ind = np.argmax(xx[i]>=x)
    #fit poly to left-neighbour minus 1 to right
    fitp = np.polyfit(x[ind-1:ind+3], y[ind-1:ind+3], 3)
