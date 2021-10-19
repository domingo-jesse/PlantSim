from image_opener import image_open
from plant_factory import plant_list


def look(): 
  
  if plant_list == {}:
    print("\nYou have no plants to look at Please add plants\n")
    pass
  else: 
    y = False
    while y == False:
      for i in plant_list: 
        print(str(i) + ") Look at " + plant_list[i].name)
   
        x = input("choose a plant to look at: ")
        try:
          key = int(x)
          if key in plant_list.keys():
            plant_list[key].plant_info()
            image_open(plant_list[key].image_path)
            x= input("Do you wanna look at another plant? (type yes or no) ")
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
  

