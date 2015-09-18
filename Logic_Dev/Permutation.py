'''
Created on Jan 29, 2015

@author: amarvignesh_r
'''
from itertools import permutations
# pali='malayalam'
# 
# if(pali[::-1]==pali):
#     print('yes')
# else:
#     print('no')
    
inp_str=input()    
a_list=list(inp_str)

flag=0
for perm in permutations(a_list):
    st=''.join(perm)
    
    if(st[::-1]==st):
        print('YES')
        flag=0
        break
    else:
        flag+=1
#         continue
        
if flag>0:
    print('NO')
        
        
# s=input('enter... ')
# c=(len(s)//2)
# print(s[c])
# s_len=len(s)
# mid=s_len//2
# inp_str=s[-mid:]
# print(inp_str)