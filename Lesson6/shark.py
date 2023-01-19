from fish import Fish

class Shark(Fish):
    def __init__(self, color, speed, diet_type, name, size):
        super().__init__(color, speed, diet_type, name, size)

    def sleep(self):
        print("I keep swimming while asleep.")
    

baby_shark = Shark("blue", "fast", "carnivore", "Angie", "tiny")
print(baby_shark)    
baby_shark.sleep()
    