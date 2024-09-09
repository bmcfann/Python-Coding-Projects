from decimal import *
getcontext().prec = 15
    
import numpy as np

#------------ Functions -----------------------------------------------------------------------------------------------------------------------------------------------------------

def discrete_factorial(n):

    #as a behind-the-scenes function, n is guaranteed to be an integer; edge cases of non-positive and/or non-integer values are nonissues
    
    number = int(n)
    product = 1
    
    if number == 0:
        return product
    else:
        for i in range(1, number + 1):
            
            product = product * i
        
        return product
    

def generate_e():
    
    sums = Decimal(0)
    
    for i in range(0, 5000):
        
        sums = sums + Decimal( (1/discrete_factorial(i)) ) 

    return sums
    
def e_to_nth_digit():
    
    mth_Digit_String = input("Enter integer from 1 to 15: ")                              #this line takes user input
    
    index1 = mth_Digit_String.find(".")                                                   #this line detects if the input contains a decimal
    
    if (float(mth_Digit_String) < 1 or float(mth_Digit_String) > 15):
        print("Outside range; try again")                                                 #if the number is outside (1,10), function is called again to restart process
        e_to_nth_digit()
        
    elif (index1 != -1):
        print("Decimal detected, number rounded down to nearest integer")
        f_mth = float(mth_Digit_String)                                                   #converts to float to not lose info then truncates using int typecast
        mth_Digit = int(f_mth)
        
        c = generate_e()                                                                  #calls generate_e() and assigns it to c
        c_string = "{0:f}".format(c)                                                      #this line transforms the number returned by generate_() into a string that can be parsed
        c_mth_decimals_only = c_string[2:1+mth_Digit]                                     #slices the string c_string into only the numbers of pi AFTER the decimal
        c_trun_e = "e to " + str(mth_Digit) + " digits: 2." + c_mth_decimals_only         #adds, as a string, the "2." in front of the decimals of e
        
        print(c_trun_e)
        
    else: 
        mth_Digit = int(mth_Digit_String)
    
        c = generate_e() 
        c_string = "{0:f}".format(c)  
        c_mth_decimals_only = c_string[2:1+mth_Digit]  
        c_trun_e = "e to " + str(mth_Digit) + " digits: 2." + c_mth_decimals_only  
        
        print(c_trun_e)
    
#----------- main -----------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    #call functions and stuff here (main "method")
    
    #print(discrete_factorial(0) + discrete_factorial(2))
    
    #print(generate_e())
    
    e_to_nth_digit()

if __name__ == "__main__" :
    main()
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------