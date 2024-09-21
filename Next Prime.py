
import numpy as np
import Prime_Factorization

#------------ Functions -----------------------------------------------------------------------------------------------------------------------------------------------------------

def next_prime():
    n = 2
    s0 = input("The first prime number is 2. Do you want to go to the next prime number? Y/N :  ")
    
    if (s0 == "Y" or s0 == "y"):
        print("YAY!", end = " ")
        
        while (s0 == "Y" or s0 == "y"):
            n = n+1 
            s1 = Prime_Factorization.is_prime(n)
            
            if (s1 == "Is likely prime"):
                print("The next prime number is " + str(n))
                s0 = input("Next prime? Y/N :  ")
        
        print("Program done. Press Alt+R to run again.")  
        
    elif (s0 == "N" or s0 == "n"):
        print("Aww, why?")
        
    else:
        print("Invalid input. Please enter \"Y\", \"y\", \"N\", or \"n\". ")
   
#----------- main -----------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    #call functions and stuff here (main method)
    #print("Hello World")
    #s = Prime_Factorization.is_prime(3)                  ##syntax for referencing/calling functions in Prime_Factorization file
    #print(s)
    
    next_prime()
    
if __name__ == "__main__" :
    main()
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------