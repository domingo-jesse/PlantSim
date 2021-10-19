# mainmenu 
from add_plants import add_plants
from water import water
from look import look 
from plant_crops import plant_crops


def main_menu(): 
 y = False
 while y == False: 
  print("1) Look Plants info")
  print("2) Add Plants")
  print("3) Pick the Weeds")
  print("4) Plant new crops")
  print("5) Leave the Garden\n" )

  x = input()
  if x == '1': 
      # function to look at plants
      look() 
  elif x == '2': 
      #function to water plant
      add_plants()
  elif x == '3': 
      #function to water plant
      water()
  elif x == '4': 
    # function to plant crops 
    plant_crops()

  elif x == '5': 
    print("\nYou leave the garden\n")
    y = True 
  else:
    #exception handler 
    print("\nInvalid Try again\n")
  



