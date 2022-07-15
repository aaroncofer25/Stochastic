import math
import random
import matplotlib.pyplot as plt

d = 0.01
l1 = 5
l2 = 10


a = [1]
b = [1]
c = [1]
d1 = [1]
e = [1]

lst =[0]

for i in range(1):
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
            
            
    for i in range(500):
        if a[i] == 1:
            u = 0.1
        if a[i] == 2:
            u = -0.2
    
        if a[i] == 1:
            s = 0.2
        if a[i] == 2:
            s = 0.3
    
        lst.append(d*u + math.sqrt(d)*s *random.random())
        
        plt.ylim(0,.05)
        plt.plot(lst)