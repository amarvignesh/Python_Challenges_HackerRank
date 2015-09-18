'''
Created on Jan 15, 2015

@author: amarvignesh_r
'''
vowels = ['a','e','i','o','u']
output_dict={}

input_str=input('Enter a string: ')
word=input_str.strip() #.................Trimming white spaces
print('Vowel : Occurence')
for i in vowels:
    if word.count(i) > 0:
        print(i,"    :",word.count(i))
      
    
#................ another method Using dictionary
# for c in word:
#     if c in output_dict.keys():
#         count=output_dict[c]
#     else:
#         count=0
#     if c in vowels_set:        #Vowel lookup
#         output_dict[c]=count+1
# print(output_dict)
