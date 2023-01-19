class Animal:
    def __init__(self, color, speed, diet_type, name):
        self.color = color
        self.speed = speed
        self.diet_type = diet_type
        self.name = name

    def eat(self, food):
        print(f"{self.name} is eating {food}.")
  
    def move(self):
        pass

    def sleep(self):
        print("I sleep normally.")
    
