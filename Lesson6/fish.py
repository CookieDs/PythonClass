from animal import Animal

class Fish(Animal):
    def __init__(self, color, speed, diet_type, name, size):
        super().__init__(color, speed, diet_type, name)
        
        self.size = size

    def swim(self, speed):
        print(f"{self.name} swims at {speed} km/h.")

    def reproduce(self):
        print(f"{self.name} lays eggs.")
    
    def __str__(self):
        return f"My name is {self.name}. I am a {self.diet_type} and I am {self.speed}, {self.size} and the color {self.color}."

# clown_fish = Fish("orange", "fast", "herbivore", "Nemo", "small")
# print(clown_fish)
