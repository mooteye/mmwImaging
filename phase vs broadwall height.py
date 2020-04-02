import matplotlib
import math

x = 2*math.pi/math.pow(10,8)
z = 0
a = 8
res = 40
zinc = 200/res
adec = 3/res
zlist, alist, fc10list, betalist = ([] for i in range (4))
while z <= 200:
    zlist.append(z)
    alist.append(a)
    fc10 = 300/(2*a)
    fc10list.append(fc10)
    betalist.append(beta)
    z = z + zinc
    a = a - adec
print (fc10list,"\n", betalist)
