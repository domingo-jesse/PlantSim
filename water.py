from plant_factory import plant_list


def water(): 
  
  if plant_list == {}:
    print("\nYou have no plants to water at Please add plants\n")
    pass
  else: 
    y = False
    while y == False:
      for i in plant_list: 
        print(str(i) + ") Look at " + plant_list[i].name)
   
      x = input("choose a Plant to Water: ")
      try:
        key = int(x)
        if key in plant_list.keys():
          plant_list[key].watered = plant_list[key].watered + 1 
          print(plant_list[key].name + " has been watered! (Total: " +  str(plant_list[key].watered) + ")" ) 
          x= input("Do you wanna  water another plant? (type yes or no) ")
          if x == 'yes' : 
            pass
          elif x == 'no':
             y = True
             print("\nYou return to main menu\n")
        else:
          #exception handler 
          print("\nThat plant does not exist try again\n")
      except: 
        print("\nPlease enter a vaild number\n") 
  

