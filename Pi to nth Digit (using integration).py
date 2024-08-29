
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
    mth_Digit_String = input("Enter nth digit of pi desired: ")      #this line and the line below take the input from the user and transform it into an integer
    mth_Digit = int(mth_Digit_String)
    
    c = 2 * integrate(-1,1)                                          #calls integrate function and since integrate function returns ~pi/2, we mult by 2
    
    c_string = str(c)                                                #turns c into a string
    c_mth_decimals_only = c_string[2:1+mth_Digit]                    #slices the string c into only the numbers of pi AFTER the decimal
    
    c_trun_pi = "3." + c_mth_decimals_only                           #adds, as a string, the "3." in front of the decimals of pi
    
    print(c_trun_pi)
    
#----------- main below -------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    #call functions and stuff here (main "method")                   #!!!!!!!!!!!!!!!!!!!!!!!!---------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!
    pi_to_nth_digit()                                                #INCLUDING THE "3.", ONLY PRINTS ACCURATELY TO 10TH DIGIT, I.E., "3.141592653"
                                                                     #!!!!!!!!!!!!!!!!!!!!!!!!---------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!
    #S = 2 * integrate(-1,1)
    #print(S)

if __name__ == "__main__" :
    main()
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------