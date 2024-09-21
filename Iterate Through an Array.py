import numpy as np

a = np.array([[1, 2], [8, 9]])

print(a[1, 0])

# arrays are obviously like matrices; in a[1,0], "1" identifies the second nested array -- or the second "column" as in linear algebra, if you will --
# i.e., [8,9](because first index = 0) and 0 identifies the zero-th element of that array, i.e., the number 8. So, in linear algebra terms, 
#       
#       | 1   8 |
#   a = |       |   and a[1,0] is equivalent to 2nd column, 1st row
#       | 2   9 |


NumString = input("Enter numbers separated by commas: ")            #receive user input; input() function returns string
 
NumList = NumString.split(", ")                                     #.split() function returns a list; here each list entry is a string 

comp = float(NumList[0])                                            #uses first number of NumList to compare others to to find maximum

for i in NumList:
    x = float(i)                                                    #converts string in NumList to float
    
    if x >= comp:                                                   #compares numbers, assigns comp larger number if x >= comp
        comp = x 

if int(comp) == comp:                                               #checks if comp is in integer and prints it as integer (no decimal) if it is; if not, prints it as is
    print(int(comp))
else: 
    print(comp)

