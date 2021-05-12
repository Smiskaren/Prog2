#!/usr/bin/env python3

from heltal import Heltal
import random
import matplotlib.pyplot as plt
import math
import numpy as np
import concurrent.futures as future
from time import perf_counter as pc


def pi_estimate(n):
        
        circle = 0
                
        circle_x = []
        circle_y = []
        square_x = []
        square_y = []
        
        for i in range(n):
            x = random.uniform(-1,1)
            y = random.uniform(-1,1)
            if x**2+y**2 <= 1:
                circle += 1
                circle_x.append(x)
                circle_y.append(y)
            else:                
                square_x.append(x)
                square_y.append(y)
            
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.scatter(circle_x, circle_y, color='b')
        ax.scatter(square_x, square_y, color='r')
        plt.savefig(f"{n}monte_carlo.png", dpi=500)
        
        pi = 4*circle/n
        return ('Estimate PI:', pi, 'Real PI:', math.pi)
                
def hypersphere(l):
    
    n,d = l        
    spherecount = 0

    for i in range(n):
        coordinates = [random.uniform(-1,1) for ii in range(d)]         
        distance = sum(map(lambda x : x**2, coordinates))
        if distance <= 1.0:
            spherecount += 1
    
    return ('Estimated volume sphere:', np.power(2.0, d)*(spherecount / n), 'Real volume:', math.pi**(float(d)/2)/math.gamma(float(d)/2 + 1))

def time_hypersphere(p):
    start = pc()
    with future.ProcessPoolExecutor() as ex:
       
        results = ex.map(hypersphere, p)
                   
        for r in results:
             print(r)

    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")

def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))
     
     

def main():
    """f = Heltal(5)
    print(f.get())
    f.set(7)
    print(f.get())"""

    #f = Heltal(5)
    #print(f.fib(5))
    
        
    """for n in [1000,10000,100000]:
        #print(pi_estimate(n))
    
    for n,d in [(100000,2), (100000,11)]:
        #print(hypersphere((n,d)))

    t1_start = pc() 
  
    hypersphere((10000000,11))  

    t1_stop = pc()
   
    print("Elapsed time during the whole program in seconds:",
                                        t1_stop-t1_start)""""

    resultpy = []
    resultc = []
    for i in range(16):
        n = 30+i
        print(pc())
        t1_start = pc()
        fib_py(n)
        t1_stop = pc()
        resultpy.append(t1_stop-t1_start)
        
        t1_start = pc()
        (f.fib(n))
        t1_stop = pc()        
        resultc.append(t1_stop-t1_start)
            
    x = list(range(30,46))
    
    y1 = resultpy
    y2 = resultc
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.savefig("Time_fib.png", dpi=500)


    print('Fibonacci c++ n=47', f.fib(47))
        
if __name__ == '__main__':
    
    #p = [(1000000, 11),(1000000, 11),(1000000, 11),(1000000, 11),(1000000, 11),(1000000, 11),(1000000, 11),(1000000, 11),(1000000, 11),(1000000, 11)]
    #time_hypersphere(p)
    main()
    
