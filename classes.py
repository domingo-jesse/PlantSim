class Plant:
  def __init__(self, name, age, image_path):
    self.name = name
    self.age = age
    self.image_path = image_path

  def plant_info(self):
    print("\nThis plant is a  " + self.name)
    print("the life span is " + str(self.age) + "\n")
  
    
  


