#So i guess the Goal of this program will be to have a fun little plant simulator were we can grow plants and water them and therefore harvest them. 

#Idk exactky how this will work- creating graphics is really not to important just the programming behinf it is what will be good and it is always good just to have something to work on 

#from mainmenu import main_menu

#def main(): 
 # print("Hello Wecome to Plant Simulator!! \nThis is where you can plant grow and harvest all of your plants")
  
 # main_menu() 
  

 # return 0
from plant_factory import plant_list 
from look import look 
from add_plants import add_plants
from water import water
from pick_weeds import pick_weeds
import tkinter as tk

from tkinter import *

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"



# Set-up the window
window = tk.Tk()
window.title("Plant Dairy")
window.resizable(width=True, height=True)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="Plant Name")


  

def show():
    Restore()
    label.config( text = clicked.get() )
  


# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

def hide_me(event):
  lbl_temp.grid_remove()
  frm_entry.grid_remove()
  btn_add.grid_remove()
  btn_pick.grid_remove()
  btn_look.grid_remove()
  btn_water.grid_remove()
  a.grid_remove()
  btn_change.grid_remove()
  
def Restore(): 
  frm_entry.grid(row=0, column=0, padx=10)
  btn_add.grid(row=0, column=1, pady=10)
  btn_pick.grid(row=0, column=2, pady=10)
  btn_look.grid(row=1, column=1, pady=10)
  btn_water.grid(row=1, column=2, pady=10)
  a.grid(row=1, column=0, padx=10)
  btn_change.grid(row=2, column=0, padx=10)
  btn.grid(row=2, column=1, padx=10)
  btn2.grid(row=2, column=2, padx=10)
  # Dropdown menu options
 

plants = list(plant_list.keys())
options = [
  plants
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set("Choose a Plant")
  
# Create Dropdown menu
drop = OptionMenu( window , clicked , *options )
drop.grid()
  
# Create button, it will change label text
button = Button( window , text = "click Me" , command = show ).grid()
  
# Create Label
label = Label( window , text = " " )
label.grid()

    

btn=tk.Button(master=window, text="Remove")
btn.bind('<Button-1>', hide_me)
btn2=tk.Button(master= window, text="Click too", command = Restore)


# Create the conversion Button and result display Label
btn_add = tk.Button(
    master=window,
    text="Add",
    command= add_plants
)

btn_water = tk.Button(
    master=window,
    text="Water",
    command= water
)

btn_pick = tk.Button(
    master=window,
    text="Pick Weeds",
    command= pick_weeds
)

btn_look = tk.Button(
    master=window,
    text="Look",
    command= look
)

def changetext():
  a.config(text="Current Plant has been Watered")

    
a = tk.Label(master=window, text="hello world")

btn_change = tk.Button(
  master= window, 
  text="Change Label Text",
  command=changetext
  )



lbl_result = tk.Label(master=window, text="Hello")

def Restore(): 
  btn_add.grid(row=0, column=1, pady=10)
  btn_pick.grid(row=0, column=2, pady=10)
  btn_look.grid(row=1, column=1, pady=10)
  btn_water.grid(row=1, column=2, pady=10)
  a.grid(row=5, column=0, padx=10)
  btn_change.grid(row=6, column=0, padx=10)
  btn.grid(row=2, column=1, padx=10)
  btn2.grid(row=2, column=2, padx=10)
Restore() 

# Run the application
window.mainloop()


# Driver program 
#main() 