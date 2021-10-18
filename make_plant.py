from classes import Plant
from image_get import get_image

def make_plant(): 
  plantname = input("\nenter plant name: \n")
  plantage = input ("Enter the plant age: \n")
  plantimage = get_image()
  return  Plant(plantname, plantage, plantimage)
 