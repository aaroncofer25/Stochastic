import math
import random
import matplotlib.pyplot as plt

d = 0.01
l1 = 10
l2 = 10
u = random.uniform(0,1)

a = [1]

for i in range(500):
    if a[i] == 1:
        if u <= 1-(d*l1):
            a.append(1)
        else:
            a.append(2)
        
    else:
        if u > 1-(d*l2):
            a.append(1)
        else:
            a.append(2)
            
plt.plot(a)
print(a)