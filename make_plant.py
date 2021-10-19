from classes import Plant
from image_get import get_image

def make_plant(name): 
  plantname = name
  plantage = input ("Enter the plant age: ")
  plantimage = get_image()
  return  Plant(plantname, plantage, plantimage)

