from make_plant import make_plant
plant_list = dict()

def create_plant(n): 
  key = n
  plant_name = input("Name your plant: ")
  plant_name = make_plant(plant_name)
  plant_list[key] = plant_name
  n = n+1
 