'''
Created on Jan 28, 2015

@author: amarvignesh_r
'''
def maxXor(l, r):
    XOR_list=[]  
    i=l
    while(l<=r):
        for i in range(l,r+1):
            XOR_list.append(l^i)
            print(int(l),'XOR', int(i), '=', int(l^i))
        l+=1
    return(max(XOR_list))
  
        
if __name__ == '__main__':
    l = int(input())
    r = int(input())
    print('max ',maxXor(l, r))