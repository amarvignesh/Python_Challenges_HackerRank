'''
Created on Jan 28, 2015

@author: amarvignesh_r
'''

def theMethod(str_list):
    tmp_list=[]
    for word in str_list: #........................... for every word in a list
        deletions=0
        tmp_list=list(word) #......................... converting string as list  
        listlen=len(tmp_list)
        for i in range(0,listlen-1): #................ from first word till (n-1) word
            if(tmp_list[i]==tmp_list[i+1]): #......... checking if i'th character is same as its next character
                deletions+=1
        print(deletions)    
               

if __name__ == '__main__':
    T = input()
    str_list=[]
    for in_str in range(int(T)):
        str_list.append(input())
    theMethod(str_list)