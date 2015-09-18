'''
Created on Feb 3, 2015

@author: amarvignesh_r
'''

T=int(input())
K=int(input())
inp_list=[]
min_=999999
for item in range(T):
    inp_list.append(int(input()))
tmp_diff=0
inp_list.sort()
for i in range(T-K):
    tmp_diff=inp_list[i+K-1]-inp_list[i]
    if tmp_diff < min_:
        min_=tmp_diff
     
print(min_)
           

