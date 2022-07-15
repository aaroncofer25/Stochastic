import math
import random
import matplotlib.pyplot as plt

d = 0.01
l1 = 6
l2 = 10


a = [1]
b = [1]
c = [1]
d1 = [1]
e = [1]

for i in range(500):
    u = random.random()
    if a[i] == 1:
        if u <= 1-(d*l1):
            a.append(1)
        if u > 1-(d*l1):
            a.append(2)
        
    if a[i] == 2:
        if u > 1-(d*l2):
            a.append(1)
        if u <= 1-(d*l2):
            a.append(2)
        


plt.ylim(0,3)            
plt.plot(a)
plt.plot(a)
plt.plot(a)
plt.plot(a)
plt.plot(a)
#print(a)