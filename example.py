# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:42:25 2021

@author: Henrik
"""
import multiprocessing as mp
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future

def runner():
    print("Performing a costly function")
    pause(1)
    print("Function complete")
    
if __name__ == "__main__":
    start = pc()
    p1 = mp.Process(target=runner)
    p2 = mp.Process(target=runner)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds") 
    #for _ in range(10):
        #runner()
    #end = pc()
       

"""processes = []
2 for _ in range(10):
3 p = mp.Process(target=some_method, args=[some_var])
4 processes.append(p)
5 for p in processes:
6 p.start()
7 for p in processes:
8 p.join()"""