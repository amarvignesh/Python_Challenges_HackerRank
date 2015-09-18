'''
Created on Feb 4, 2015

@author: amarvignesh_r
'''
# ............. In a given string, finding if any of its permutation will be a palindrome?........# 

inp_str = input()
for c in inp_str:
    if inp_str.count(c) % 2 == 0:
        inp_str = inp_str.replace(c, '')  # ............... remove characters occuring even no.of times
if len(inp_str) == 1 or len(inp_str) == 0:  # .............. if all chars occurs even times then len=0 or even if it's 1 then YES
    print('YES')
else:    
    x = inp_str[0]
    if len(inp_str) == inp_str.count(x):  # .............. if len is >1 then check all chars in inp_str are the same
        print('YES')
    else:
        print('NO')
            
            
    
        
