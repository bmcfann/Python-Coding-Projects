
from decimal import *
getcontext().prec = 18
    
import numpy as np

#------------ Functions -----------------------------------------------------------------------------------------------------------------------------------------------------------

def BBP():
    sums = Decimal(0)
    
    for i in range(0, 50000):
        sums = sums + Decimal( (   (1/(16**i)) * (  (4/(8*i + 1)) - (2/(8*i + 4)) - (1/(8*i + 5)) - (1/(8*i + 6))  )   )  )   #BBP algorithm/summation
    
    return sums
    
def pi_to_nth_digit():
    
    mth_Digit_String = input("Enter integer from 1 to 15: ")                              #this line takes user input
    
    index1 = mth_Digit_String.find(".")                                                   #this line detects if the input contains a decimal
    
    if (float(mth_Digit_String) < 1 or float(mth_Digit_String) > 15):
        print("Outside range; try again")                                                 #if the number is outside (1,10), function is called again to restart process
        pi_to_nth_digit()
        
    elif (index1 != -1):
        print("Decimal detected, number rounded down to nearest integer")
        f_mth = float(mth_Digit_String)                                                        #converts to float to not lose info then truncates using int typecast
        mth_Digit = int(f_mth)
        
        c = BBP()                                                                              #calls BBP() and assigns it to c
        c_string = "{0:f}".format(c)                                                           #this line transforms the number returned by BBP() into a string that can be parsed
        c_mth_decimals_only = c_string[2:1+mth_Digit]                                          #slices the string c_string into only the numbers of pi AFTER the decimal
        c_trun_pi = "pi to " + str(mth_Digit) + " digits: 3." + c_mth_decimals_only            #adds, as a string, the "3." in front of the decimals of pi
        
        print(c_trun_pi)
        
    else: 
        mth_Digit = int(mth_Digit_String)
    
        c = BBP() 
        c_string = "{0:f}".format(c)  
        c_mth_decimals_only = c_string[2:1+mth_Digit]  
        c_trun_pi = "pi to " + str(mth_Digit) + " digits: 3." + c_mth_decimals_only  
        
        print(c_trun_pi)

    
#----------- main below -----------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    #call functions and stuff here (main "method")
    
    pi_to_nth_digit()

if __name__ == "__main__" :
    main()
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------