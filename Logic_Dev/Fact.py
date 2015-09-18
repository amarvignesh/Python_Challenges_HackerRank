'''
Created on Jan 27, 2015

@author: amarvignesh_r
'''
def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res    

res=(factorial(5))
print(res)