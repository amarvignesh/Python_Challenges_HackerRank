'''
Created on Jan 14, 2015

@author: amarvignesh_r
'''

def pigLatin(input_str):
    vowels = ['a','e','i','o','u']
    position=0    
    
    pig_latin=input_str.strip() #Trimming white spaces
        
    for c in pig_latin:
        if c in vowels:         #Vowel lookup
            position=pig_latin.index(c)
            return position
        
#######################################  It starts here...
        
if __name__=='__main__':
    string_input = input('Enter a word: ')  #Input string
    position=pigLatin(string_input)  

    if position==None:
        print(string_input +'way')
    elif position==0:
        output_string=string_input+'way'
        print(output_string)
    else:
        output_string=string_input[position:]+string_input[:position]+'ay'
        print(output_string)