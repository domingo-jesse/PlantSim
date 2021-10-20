#So i guess the Goal of this program will be to have a fun little plant simulator were we can grow plants and water them and therefore harvest them. 

#Idk exactky how this will work- creating graphics is really not to important just the programming behinf it is what will be good and it is always good just to have something to work on 

#from mainmenu import main_menu

#def main(): 
 # print("Hello Wecome to Plant Simulator!! \nThis is where you can plant grow and harvest all of your plants")
  
 # main_menu() 
  

 # return 0
  
from look import look 
from add_plants import add_plants
from water import water
from pick_weeds import pick_weeds
import tkinter as tk

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
  
def see_me(event):
  frm_entry.grid(row=0, column=0, padx=10)
  btn_add.grid(row=0, column=1, pady=10)
  btn_pick.grid(row=1, column=1, pady=10)
  btn_look.grid(row=2, column=1, pady=10)
  btn_water.grid(row=3, column=1, pady=10)
  a.grid(row=4, column=1, padx=10)
  btn_change.grid(row=5, column=1, padx=10)
  btn.grid(row=7, column=1, padx=10)
  btn2.grid(row=6, column=1, padx=10)

    

btn=tk.Button(master=window, text="Remove")
btn.bind('<Button-1>', hide_me)
btn2=tk.Button(master= window, text="Click too",)
btn2.bind('<Button-1>', see_me)


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
  a.config(text="changed text!")
  frm_entry.grid(row=0, column=0, padx=10)
  btn_add.grid(row=0, column=1, pady=10)
  btn_pick.grid(row=1, column=1, pady=10)
  btn_look.grid(row=2, column=1, pady=10)
  btn_water.grid(row=3, column=1, pady=10)
  a.grid(row=4, column=1, padx=10)
  btn_change.grid(row=5, column=1, padx=10)
  btn.grid(row=7, column=1, padx=10)
  btn2.grid(row=6, column=1, padx=10)

    
a = tk.Label(master=window, text="hello world")

btn_change = tk.Button(
  master= window, 
  text="Change Label Text",
  command=changetext
  )



lbl_result = tk.Label(master=window, text="Hello")

# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_add.grid(row=0, column=1, pady=10)
btn_pick.grid(row=1, column=1, pady=10)
btn_look.grid(row=2, column=1, pady=10)
btn_water.grid(row=3, column=1, pady=10)
a.grid(row=4, column=1, padx=10)
btn_change.grid(row=5, column=1, padx=10)
btn.grid(row=7, column=1, padx=10)
btn2.grid(row=6, column=1, padx=10)

# Run the application
window.mainloop()


# Driver program 
#main() 