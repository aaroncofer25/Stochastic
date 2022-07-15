import math
def f(a, n):
        for i in range(1,20):
            a = a**i % n
            if a == 1:
                print("Pick new a")
            d = math.gcd(a -1, n)
            if d > 1 and d < n:
                print(i, d)
                
            
                