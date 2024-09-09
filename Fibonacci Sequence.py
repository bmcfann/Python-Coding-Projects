
import numpy as np

#------------ Functions -----------------------------------------------------------------------------------------------------------------------------------------------------------

def verify_int(x):
    
    index1 = x.find(".")                                            #detects if the entered value has a decimal
    
    if (index1 == -1):                                              #if index1 == -1, that means input value does NOT have a decimal, so it is an integer
        return "Input is an integer!" 
        
    else: 
        for i in range( index1 + 1 , len(x) ):                      #The final index in x is len(x)-1 so range is perfect and len(x) + 1 is unnecessary for upper bound
            dec = int(x[i])                                         #i ranges between the first decimal (after index1) to the end of the string (the last decimal)
                                                                    #and for each decimal place (each dec = x[i]), if the decimal is not 0, the input is NOT an integer 
            if (dec != 0):                                          #The absence of an else statement in the nested if statement implies that if all decimal places are 0,
                return "Input is not an integer!"                   #then the input is an integer
        
def nth_fib(n):
    
    string = verify_int(n)                                          #calls above function to verify that the input is an integer 
    
    if (string == "Input is not an integer!"):
        print("Input is not an integer, try again.")                #if input is determined to not be in integer, nth_fib function is called again to facilitate another attempt
        w = input("Enter a positive integer: ")
        
        return nth_fib(w)
        
    else:
        sums = 0
        m = int(float(n))
    
        if (m == 1 or m == 2):
            sums = 1                                                #The nested if/elif/else statement contains initial conditions and other invalid inputs
            return sums
    
        elif (m < 1):
            print("Invalid input in this context; try again.")
            p = input("Enter a positive integer: ")
        
            return nth_fib(p)
        
        else:
            sums = nth_fib(str(m-1)) + nth_fib(str(m-2))
            return sums
            
def fib_sequence(t):
    
    string = verify_int(t)
    
    if (string == "Input is not an integer!"):
        print("Input is not an integer, try again.")                #if input is not an integer, fib_sequence function is called again to facilitate another attempt
        w = input("Enter a positive integer: ")
        
        return fib_sequence(w)  

    else: 
        k = int(float(t))
        
        if (k < 1):
            print("Invalid input in this context; try again.")     #if integer is negative, fib_sequence is called to facilitate another attempt
            p = input("Enter a positive integer: ")
        
            return fib_sequence(p)
            
        else: 
            for i in range(1, k):
                print(nth_fib(str(i)), end = ", ")                 #since range(1, k) goes from 1 to k-1, this prints every nth fibonacci number with a comma after until 
                                                                   #the (k-1)-nth one, then the print statement below prints the k-th one w/o a comma
            print(nth_fib(str(k)))
   
#----------- main -----------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    #call functions and stuff here (main method)
    
    x = input("Enter a positive integer: ")
    print( nth_fib(x) )
    
    y = input("Enter a positive integer: ")
    fib_sequence(y)
    
if __name__ == "__main__" :
    main()
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------