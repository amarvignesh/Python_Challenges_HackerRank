'''
Created on Jan 29, 2015

@author: amarvignesh_r
'''
#.........For a given word, find the min required downgrade moves(by changing d to c but not c to d or a to b) 
#.........to convert it in to a palindrome

def love_letter_mystery(str_list):
    chr_list=[]
        
    for word in str_list: #........................................ for every word in the list        
        moves=0         
        chr_list=list(word) #...................................... converting string to list
        lislen=int(len(chr_list)) #................................ finding string length
        for i in range(0,lislen):
            tmp=ord(chr_list[i])-ord(chr_list[lislen-(i+1)]) #..... ascii difference of (1st and nth char, 2nd and n-1...)
            if(tmp>0): #........................................... because only positive values need to be downgraded (ex:c to b)
                moves+=tmp
        print(moves)
                      

if __name__ == '__main__':
    T = input()
    str_list=[]
    for in_str in range(int(T)):
        str_list.append(input())
    love_letter_mystery(str_list)