
import numpy as np

#------------ Functions -------------------------------------------------------------------------------------------------------------------------------------------------------

def f(x):
    y = np.sqrt(1 - np.square(x))                                    #this is the function f(x)=sqrt(1-x^2)
    
    return y
    
def integrate(a, b):
    sums = f(a)                                                      #sums is instantiated as f(a) because left riemann sums always start with the left endpoint 
    
    for i in range(1, 5000000):                                      #this for loop is the riemann sum; n = 1000000 so delta_x = (b-a)/1000000),thus, we increment on top
        sums = sums + f(a + ( i * ((b-a)/5000000) ))                 #of the left endpoint f(a) by adding i slices of delta_x, hence f(a + ( i * ((b-a)/1000000) )).
                                                                     #Then, we add it to sums as a summation does. Finally, we multiply the whole sum by delta_x as should   
    sums = ((b-a)/5000000)*sums                                      #be done in riemann sums.
        
    return sums
    
def pi_to_nth_digit():
    mth_Digit_String = input("Enter integer between 1 and 10: ")            #this line takes user input
    
    index1 = mth_Digit_String.find(".")                                     #this line detects if the input contains a decimal
    
    if (float(mth_Digit_String) < 1 or float(mth_Digit_String) > 10):
        print("Outside range; try again")                                   #if the number is outside (1,10), function is called again to restart process
        pi_to_nth_digit()
        
    elif (index1 != -1):
        print("Decimal detected, number rounded down to nearest integer")
        f_mth = float(mth_Digit_String)                                                   #converts to float to not lose info then truncates using int typecast
        mth_Digit = int(f_mth)
    
        c = 2 * integrate(-1,1)                                                           #calls integrate function and since integrate function returns ~pi/2, we mult by 2
    
        c_string = str(c)                                                                 #turns c into a string
        c_mth_decimals_only = c_string[2:1+mth_Digit]                                     #slices the string c into only the numbers of pi AFTER the decimal
    
        c_trun_pi = "pi to " + str(mth_Digit) + " digits: 3." + c_mth_decimals_only       #adds, as a string, the "3." in front of the decimals of pi
    
        print(c_trun_pi)
        
    else:
    
        mth_Digit = int(mth_Digit_String) 
    
        c = 2 * integrate(-1,1) 
    
        c_string = str(c) 
        c_mth_decimals_only = c_string[2:1+mth_Digit] 
    
        c_trun_pi = "pi to " + str(mth_Digit) + " digits: 3." + c_mth_decimals_only 
    
        print(c_trun_pi)

    
#----------- main below -------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    #call functions and stuff here (main "method") 
    pi_to_nth_digit() 
    
    #S = 2 * integrate(-1,1)
    #print(S)

if __name__ == "__main__" :
    main()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------