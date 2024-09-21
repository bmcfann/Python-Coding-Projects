
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

def is_even(x):
    string = verify_int(x)                                          #verifys if input is an integer or not
    n = int(float(x))                                               #converts input to int thru float in case input is not integer; avoids str -> int failure cuz decimal
    
    if (string == "Input is not an integer!"):
        print("Input is not a whole number; try again")
        
        t1 = input("Enter a positive whole number that is not -1, 0, or 1: ")
        Prime_Factor(t1)
        
    else: 
        if (n % 2 == 0):
            #print("EVEN STEVENS")                                  #nested if-else determines if input is even or not; if even, returns input, if not, returns -1
            
            return n
            
        else:
            #print("NOT EVEN >:(")
            return -1
            
#def is_divisible(x , y):
    #string = verify_int(x)                                          #verifys if input is an integer or not
    #n = int(float(x))                                               #converts input to int thru float in case input is not integer; avoids str -> int failure cuz decimal
    #m = int(float(y))
    
    #if (string == "Input is not an integer!"):
        #print("Input is not a whole number; try again")
        
        ##call main prime factorization function##
        
    #else: 
        #if (n % m == 0):
            #print(x + " is divisible by " + y)                                  #nested if-else determines if input is even or not; if even, returns input, if not, returns -1
            
            #return n
            
        #else:
            #print(x + " is not divisible by " + y)
            
            #return -1
            
def is_prime(x):
    n = float(x)
    k = int(np.ceil(np.sqrt(n)))
    i = 2
    m = int(n)
    
    while (i <= k):
        y = m % i
        
        if (y == 0):
            #print("Is NOT prime")
            return "Is NOT prime"
        
        i = i + 1
    
    #print("Is likely prime")
    return "Is likely prime"

def Prime_Factor(x):
    a = is_even(x)
    count = 0
    
    if (a != -1 and int(float(x)) != 2 and int(float(x)) != 0 and int(float(x)) > 0): 
        
        while (a != -1):
            a = a/2
            a = is_even(str(a))                                       #checks if input is even, if so, keeps dividing by 2 until it isnt anymore
                                                                      #the count variable records how many factors of 2 the input has
            count = count + 1
        
        t = float(x) / float(2**count)
        s = is_prime(t)                                               #calls is_prime function 
        
        if (s == "Is likely prime" and int(t) != 1):
            print(x + " has prime factors of 2^" + str(count) + " and " + str(int(t)))
            
        elif (s == "Is likely prime" and int(t) == 1):
            print(x + " has a prime factor of 2^" + str(count))
            
        else:
            
            g1 = np.ceil( np.sqrt(t) )
            
            for i2 in range(1, int(g1)+1):
                j2 = 2*i2 + 1
                count3 = 0
                
                while (t % j2 == 0):
                    t = t/j2
                    
                    count3 = count3 + 1
                    
                if (count3 != 0):
                    print(x + " has a prime factor of " + str(j2) + "^" + str(count3))
            
            
            ##code for number with more factors than 2^(something) and a prime number##          !!!!!!!!!!!!!!!!!!! STILL TO DO !!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
            print(x + " has a prime factor of 2^" + str(count))
        
    elif (int(float(x)) == 2):
        print(x + " is prime")
        
    elif (int(float(x)) == 1 or int(float(x)) == 0 or int(float(x)) == -1):
        print("Input is not a prime number by definition; try again.")
        t2 = input("Enter a positive whole number that is not -1, 0, or 1: ")
        Prime_Factor(t2)
        
    elif (int(float(x)) < 0):
        print("Input is not positive. Prime factorization retains its uniqueness up to ordering only for positive integers. Please try again.")
        t3 = input("Enter a positive whole number that is not -1, 0, or 1: ")
        Prime_Factor(t3)
        
    else:
        r = is_prime(x)
        w = float(x)
        v = np.ceil( np.sqrt(w) )
        
        if (r == "Is likely prime"):
            print(x + " is prime")
            
        else:
            
            for i in range(1, int(v)+1):
                j = 2*i + 1
                count2 = 0
                
                while (w % j == 0):
                    w = w/j
                    
                    count2 = count2 + 1
                    
                if (count2 != 0):
                    print(x + " has a prime factor of " + str(j) + "^" + str(count2))

   
#----------- main -----------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    #call functions and stuff here (main method)
    
    z1 = input("Enter a positive whole number that is not -1, 0, or 1: ")
    #z2 = input("Enter another whole number to divide the first: ")
    #print(is_even(z1))
    
    Prime_Factor(z1)
    
    #is_prime(z1)
    
    #print(is_divisible(z1, z2))
    
if __name__ == "__main__" :
    main()
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------