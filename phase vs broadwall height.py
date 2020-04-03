import matplotlib.pyplot as plt
import math

x = (2*math.pi)/(3*math.pow(10,8))
z = 0
a = 8
res = 40
zinc = 200/res
adec = 3/res
zlist, alist, fc10list, betalist = ([] for i in range (4))
while z <= 200:
    zlist.append(z)
    alist.append(a)
    fc10 = (3*math.pow(10,11))/(2*a)
    fc10list.append(fc10)
    beta = x*math.sqrt((math.pow(35000000000,2))-(math.pow(fc10,2)))
    betalist.append(beta)
    z = z + zinc
    a = a - adec
#print (fc10list,"\n", betalist)
plt.plot(fc10, a)
plt.show()
