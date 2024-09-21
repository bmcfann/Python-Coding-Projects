
import numpy as np
import tkinter as tk

#------------ Functions -----------------------------------------------------------------------------------------------------------------------------------------------------------

def tile_cost():
    
    def calc_cost():
        
        try:                                                                      #the try/except thing is a way to check for an error. The code under the try statement is
            sqft = float(sqft_ent.get())                                          #run if the error or condition outlined in the "except" part (in this case a ValueError) 
            width = float(width_ent.get())                                        #is not detected. Like an if-else statement, if the ValueError is detected, the code under
            length = float(length_ent.get())                                      #the except block is run instead. 
        
            COST = width * length * sqft
        
            cost_lbl_2.config(text = "$" + str(COST))                             #*label*.config(text = "string") is used to update the text in the label chosen
            
        except ValueError:
            cost_lbl_2.config(text = "Please only enter numbers. Thank you.")
    
    window = tk.Tk()                                                              #builds the window
    window.title("Tile Cost Estimator")
    
    #window.columnconfigure(0, weight = 1)
    #window.rowconfigure(0, weight = 1)
    
    frame1 = tk.Frame(window, bd = 4, relief = "ridge")                           #the frame surrounding the entry boxes for measurements/price
    frame1.grid(padx = 15, pady = 15)
    
    frame2 = tk.Frame(window, bd = 1, relief = "ridge")                           #frame surrounding the final total cost
    frame2.grid(padx = 15, pady = 15)
    
    frame3 = tk.Frame(frame2, bg = "white", bd = 1, relief = "groove", height = 25, width = 150)          #frame/area where final total cost is displayed
    frame3.grid(in_ = frame2, column = 0, row = 8, pady = 10)
    #frame3.grid_propagate(0)
    
    cost_lbl_1 = tk.Label(frame2, text = "Total estimated cost of the flooring is:")
    cost_lbl_1.grid(column = 0, row = 6, padx = 10, pady = 10, sticky = tk.E + tk.W + tk.N + tk.S)
    
    cost_lbl_2 = tk.Label(frame3, text = "       ", bg = "white")
    cost_lbl_2.grid(column = 0, row = 0, padx = 5, pady = 5)
    
    sqft_lbl = tk.Label(frame1, text = "Enter cost of tile per sq. ft (in dollars):")                  #"frame" tells the label to be attached to the frame object, not the window
    sqft_lbl.grid(column = 0, row = 2, padx = 10, pady = 10, sticky = tk.W)                                           #.grid(...) tells the widget how to be placed in the frame; w/o this line the widget wont show up in the frame
    
    width_lbl = tk.Label(frame1, text = "Enter width of floor (in feet):")
    width_lbl.grid(column = 0, row = 3, padx = 10, pady = 10, sticky = tk.W)
    
    length_lbl = tk.Label(frame1, text = "Enter length of floor (in feet):")
    length_lbl.grid(column = 0, row = 4, padx = 10, pady = 10, sticky = tk.W)
    
    sqft_ent = tk.Entry(frame1, width = 15)
    sqft_ent.grid(column = 1, row = 2, padx = 10)
    
    width_ent = tk.Entry(frame1, width = 15)
    width_ent.grid(column = 1, row = 3, padx = 10)
    
    length_ent = tk.Entry(frame1, width = 15)
    length_ent.grid(column = 1, row = 4, padx = 10)
    
    calc_btn = tk.Button(window, text = "Calculate", bg = "blue", fg = "white", command = calc_cost)
    calc_btn.grid(padx = 15, pady = 15)
    
    window.mainloop()                                   ##follows all code; as a loop, all code above mainloop is "inside" the loop, anything below it will not update in window/GUI
    print("Window closed")                              ##anything below mainloop will be executed when the window is exited, tho   
#----------- main -----------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    #call functions and stuff here (main method)
    #print("Hello World")
    
    tile_cost()
    
if __name__ == "__main__" :
    main()
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------