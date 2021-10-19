class Plant:
  def __init__(self, name, age, image_path, watered = 0):
    self.name = name
    self.age = age
    self.image_path = image_path
    self.watered = watered 

  def plant_info(self):
    print("\nThis plant is a  " + self.name)
    print("the life span is " + str(self.age))
    print(self.name + " has been watered " + str(self.watered) + " times\n")
  
    
  


