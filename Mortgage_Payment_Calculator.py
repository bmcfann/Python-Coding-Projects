
import numpy as np
import tkinter as tk

#----------- Functions ------------------------------------------------------------------------------------------------------------------------------------------------------------

def Calculate_Mortgage():
    
    
    window = tk.Tk()
    window.title("Mortgage Payment Calculator")
    window.columnconfigure(0, weight = 2)
    
    window_frm = tk.Frame(master = window, bd = 7, relief = "groove", 
        bg = "#d4d4d4", height = 100, width = 100)
    window_frm.pack(fill = tk.BOTH, expand = True)                                           ##fill and expand make sure the frame scales with window resizing
    
    prin_lbl = tk.Label(master = window_frm, 
        text = "Enter principal amount of loan (in dollars) :", 
            bg = "#d4d4d4")
    prin_lbl.grid(column = 0, row = 0, padx = 10, pady = 10, sticky = tk.W)
    
    prin_ent = tk.Entry(master = window_frm, width = 20)
    prin_ent.grid(column = 1, row = 0, padx = 10, sticky = tk.W)
    
    interest_lbl = tk.Label(master = window_frm, text = "Enter annual interest (as a percentage or decimal) :", 
        bg = "#d4d4d4")
    interest_lbl.grid(column = 0, row = 1, padx = 10, pady = 10, sticky = tk.W)
    
    interest_ent = tk.Entry(master = window_frm, width = 20)
    interest_ent.grid(column = 1, row = 1, padx = 10, pady = 10, sticky = tk.W)
    
    comp_lbl = tk.Label(master = window_frm, text = "Enter compounding frequency (annually, monthly, etc.) :", 
        bg = "#d4d4d4")
    comp_lbl.grid(column = 0, row = 2, padx = 10, pady = 10, sticky = tk.W)
    
    comp_ent = tk.Entry(master = window_frm, width = 20)
    comp_ent.grid(column = 1, row = 2, padx = 10, pady = 10, sticky = tk.W)
    
    time_lbl = tk.Label(master = window_frm, text = "Enter time (in years) :", bg = "#d4d4d4")
    time_lbl.grid(column = 0, row = 3, padx = 10, pady = 10, sticky = tk.W)
    
    time_ent = tk.Entry(master = window_frm, width = 20)
    time_ent.grid(column = 1, row = 3, padx = 10, pady = 10, sticky = tk.W)
    
    window.mainloop()
    
    print("Window closed.")
 
#----------- Main -----------------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
    #call functions and stuff here (main method)
    print("Hello World")
    
    Calculate_Mortgage()
    
if __name__ == "__main__" :
    main()
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------