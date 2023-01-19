#Dictionaries 
#{key: value}
#for key,value in dictionary.items():
#   access the key-value pairs 

#for key in dictionary.keys():
#   access keys only
#print(dictionary.keys()) #Printing keys right away

#for value in dictionary.values():
#   access values only
#print(dictionary.values()) #Printing the values right away

#Add a key + value (element)
#dictionary["New key"] = "New value"

#Modify
#dictionary["New key"] = dictionary["New key"] + "something else"

#Remove a pair
#del dictionary["Old key"]

#Modify a key
#dictionary["Another one"] = dictionary["New key"] #Recreating (copy) an element pair
#del dictionary["New key"]                         #Removing the old one

#Nesting - A dictionary in a dictionary, just like lists, loops and if-else etc

#print(house["Room2"]["Item1"])
#For lists: print(ls[the list in ls][the index of an item in the list])

numbers = {
    "odd": [1, 3, 5, 7, 9],
    "even": [0, 2, 4, 6, 8]
}
print(numbers["odd"][0]) #To access the first odd number

#Default arguments
def greetings(name = "everyone"):
    print(f"Hello {name}!")

greetings() #If you don't call anything in the function you can have it in the argument after = 
greetings("Diana")

#Position arguments
def describe_person(first_name, last_name, age):
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")
    print(f"Age: {age}")

describe_person("Diana", "S", 16) #Put it in the right order
#Keyword arguments: - but then you have to do it on ALL of the arguments
describe_person(age = 16, first_name = "Diana", last_name = "S") #You can name them, whatever argument you called

#Sequence of arguments
def sample(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    for arg in args:
        print(arg)

print(sample(0, 1, 2)) 
#Normally you can only give as many as the arguments but the * means sequence so you can take in more as a tuple
print(sample(0, 1, 2, 3, 4))

def name_score(name = "None", *scores):
    total = 0
    for score in scores:
        total += score
    print(f"{name}:", total)

name_score("Diana", 0, 4, 9, 3)

#arb. number of keyword args
def describe_person(first_name, last_name, **kwargs): #Two stars = dictionary
    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")

    for key in kwargs:
        print(f"{key.title()}: {kwargs[key]}") #kwargs[key] = value
    for key, value in kwargs.items():
        print(f"{key.title()}: {value}")

describe_person("Diana", "S", age = 16, hair_color = "dark brown")

#Classes
#Example rocket and we want to track the x + y of the rocket
class Rocket(): #The blueprint
    def __init__(self): #self = accessing the variable anywhere in the class #The functions are the behaviors
        #Class contains 2 pieces of information #Classes are a way of combining information and behavior
        self.y = 0 #These two "self" belongs to the class 
        self.x = 0

    def move_up(self): #Updates the value y by 1 when the rocket moves up
        self.y += 1

    def get_location(self): #Report the rocket's location
        return (self.x, self.y)

#Blueprint is a sketch or drawing of the house #This is the general idea of a rocket. Every rocket that we define will be able to do these things
my_rocket = Rocket() #Now we initialized the rocket
print(my_rocket) #Now we have a rocket object
#Instance of a rocket class
#If we change the value of x for my_rocket it won't change the default x, the blueprint is set.
print("Rocket position:", my_rocket.get_location())
my_rocket.move_up() #We move up once
print("Rocket position:", my_rocket.get_location())
my_rocket.move_up() #We move up once more
print("Rocket position:", my_rocket.get_location())

my_fleet = [Rocket() for i in range(5)] #List comprehension

rocket1 = Rocket()
rocket2 = Rocket()
rocket3 = Rocket()
rocket4 = Rocket()
rocket5 = Rocket()

my_rockets = []
my_rockets.append(rocket1.get_location())
my_rockets.append(rocket2.get_location())
my_rockets.append(rocket3.get_location())
my_rockets.append(rocket4.get_location())
my_rockets.append(rocket5.get_location())
print(my_rockets)

x = 0
y = 0
location = (x, y)
rockets = ["r1", "r2", "r3", "r4", "r5"]
for rocket in rockets:
    rocket = f"{rocket}: {location}"
print(rockets)
for rocket in my_fleet:
    print(rocket) #5 different rockets #The objects memory location are different but the location we set(get_location()) are defaulted

#Python works with objects, everything is turned into objects and stored like that.
#Object oriented programming = OOP, making stuff reusable - classes #Should be little to none code repetition
#When creating a class you define an initial method so it'll be called #Everything you're generally gonna use
#When naming a class use capital letter and () #Camelcase = WordsTogether #Snakecase = small letters? < search 
#The function name __init__ calls automatically when you create an object from this class #Any valueable attributes are set there
#self refers to the objects itself, all methods in a class should have self in the first argument #So you use any self functions, in our example ^ you can use.x (accessing self.x)
'''
import math 
class Rocket(): 
    def __init__(self, x_value = 0, y = 0): 
        self.y = x_value #Generally don't do this, have it the same but this time just to understand and show.
        self.x = y 

    def move(self, speed_x, speed_y): #Moves the rocket #If you know your function definetly needs this function you don't need to put a default
        self.x += speed_x
        self.y += speed_y


    def get_location(self):
        return (self.x, self.y)

    def get_distance(self, other_rocket):
        distance = sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2)

my_rocket = Rocket(5, 5)
print(my_rocket.get_location)
my_rocket = Rocket()
print(my_rocket.get_location)
my_rocket.move(1, 2) #Gonna stay, when you move 1, 2 again it'll just add
print(my_rocket.get_location)
my_rocket.move(1, 2) 
print(my_rocket.get_location)
'''

#Class in class. From bottom to top. Check subclass and then upper class.