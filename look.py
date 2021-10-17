from image_opener import image_open
from classes import Plant

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
      image_open('./images/rose-peach.jpg')
      p1 = Plant("Rose", 35)
      p1.plant_info()


    elif x == '2': 
      image_open('./images/willow-tree.jpg')
      p2 = Plant("Willow", 30)
      p2.plant_info()

    elif x == '3': 
      image_open('./images/Venus-flytrap.jpg')
      p3 = Plant("Venus FlyTrap", 20)
      p3.plant_info()

    elif x == '4': 
      print("\nYou go to the main menu\n")
      y = True 
    else:
      print("\nInvalid Try again\n")
  return 0
