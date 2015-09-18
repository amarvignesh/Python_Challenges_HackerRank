'''
Created on Jan 14, 2015

@author: amarvignesh_r
'''
cycles = 2
a_list = [0, 1]
height = 1

for i in a_list: 
    height = 1
    for k in range(1, i + 1):
        if(k % 2 == 0):
            height += 1
        else:
            height += height
    print(height)
    
        
        
