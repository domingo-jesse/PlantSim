from image_opener import image_open
from make_plant import make_plant


def look(): 
  print("What do you wanna look at?")
  y = False
  while y == False:
    print("1) Look at rose ")
    print("2) Look at Willow")
    print("3) Look at Venus FlyTrap ")
    print("4) Go back to main menu\n" )

    x = input()
    if x == '1': 
      Plant1 = make_plant()
      Plant1.plant_info()
      image_open(Plant1.image_path)

    elif x == '2': 
      Plant2 = make_plant()
      Plant2.plant_info()
      image_open(Plant2.image_path)

    elif x == '3': 
      Plant3 = make_plant()
      Plant3.plant_info()
      image_open(Plant3.image_path)

    elif x == '4': 
      print("\nYou go to the main menu\n")
      y = True 
    else:
      print("\nInvalid Try again\n")
  return 0
