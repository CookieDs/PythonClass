#List Comprehensions

squares = []
for number in range(1,11):
    new_square = number ** 2
    squares.append(new_square)

for square in squares:
    print(square)

#To make all this ^ in one line v
squares = [number ** 2 for number in range(1,11)]
print(squares)

#Non-numerical versions
students = ["Tarik" , "Diana", "Yunus"]
great_students = []
for student in students:
    great_students.append(student + " the great...")

for great_student in great_students:
    print("Hello", great_student)

#great_students = [add "the great" to each student, for each student]
great_students = [student + " the great" for student in students]
for great_student in great_students:
    print("Hello", great_student)

#Exercises:
#0
tens = [number * 10 for number in range(1, 11)]
print(tens)

#1
cubes = [[number ** 3 for number in range(1,11)]]
print(cubes)

#2
names = ["diana", "tarik", "nilgun", "bedir", "yunus"]
awesome_names = [name.title() + " is awesome!" for name in names] #??
for awesome in awesome_names:
    print(awesome)

#3
plus_thirteen = [num + 13 for num in range(1, 11)]
print(plus_thirteen)

#Strings as Lists  - the order matters! (different indexes)
s = "Diana"
for letter in s:
    print(letter)

ls = list(s) #You make the string as a list, each character as one string?
print(ls)

#Slicing strings
name = "Braddock"
first_ch = name[0]
last_ch = name[-1]

first_4_letters = name[:4]
last_4_letters = name[-4:]

print(first_4_letters)
print(last_4_letters)

sentence = "He was the champ!"
print(sentence[3:6])
#print(sentence[-16::-1])
print(sentence[:3] + sentence[:3])

#Finding substrings
message = "He fought for all!"
all_present = "all" in message
print(all_present)

all_index = message.find("all")
print(all_index)
print(message[all_index:all_index +len("all")])

msg = "Cats and dogs... Cats and dogs..." #If more than one is the same
print(msg.find("Cats")) #Only looks for the first
print(msg.rfind("Cats")) #Finds the first from right to left
print(msg.count("dogs"))

#Replace
print(msg.replace("dogs", "turtles"))

#Splits
sent = "The hockey team lost"
ls = sentence.split(" ") #Removes " " and splits
print(ls)

animals = "cat, dog, turtle, hamster, lion"
print(animals.split(", "))

#Tuples
#Lists that we can never change, immutable
colors = ("red", "green", "blue") #Tuples = (), lists = []
print(colors[0])
for color in colors:
    print(color)

#String formatting with numbers
#print("hi " + 23) #Does not work because it's string + integer
print("hi " + str(23)) #Make the integer into a string

num = 23
print("Hi " + str(num))

print("Hi there beautiful number %d." % num)
ls = [7, 13, 19]
#print("Some of the amazing prime numbers are %d, %d and %d.") % (ls[0], ls[1], ls[2])
print("some tries: %s %d %f" % ("hey there", 3, 3.0))

#%s - string
#%d - int
#%f - float

#Variable types:
#Bool is the variable for True and False

#Basic math operators
a = 5 // 2 #Div without remaimder, 2 instead of 2.5 (whole number)
a = 5 % 2 #The remainder, 1 ("rest")

val = True
val = False

print("A float: %.2f" % 3.0) 
float_number = 3.0
print(f"A float: {float_number}") #Forced string, what he puts inside is a variable

print("Some of the amazing prime numbers are {}, {} and {}.".format(ls[0], ls[1], ls[2]))

#Functions 
#Instead of repeating
#def function_name(arguments): #Define function, arguments are what differs a function
#function_name(arguments)
print("You are an amazing person Allie!") #You wanna change the name Allie
print("We are appriciating your existence...")
print("Please spend more time with us.")
print("To enroll, click the button below!")

def ad_run(name):
    print(f"You are an amazing person {name}!") #Forcing in the name, defining a function
    print("We are appriciating your existence...")
    print("Please spend more time with us.")
    print("To enroll, click the button below!")

ad_run("Nilgun") #Has to be below definition
ad_run("Yunus")
ad_run("Diana")
ad_run("Tarik")

emails = ["em1@gmail.com", "e2@gmail.com", "f3@gmail.com", "gg5@gmail.com"]
message = "students must bring a pen!"
for email in emails:
    print(f"Sent to: {email}") #Sending email to different students
    print(f"Message: {message}") #If you want a different message youd have to copy and paste with a different message. 

#Here's an easier way, using a function:
def email_students(message, emails): #Have the message and emails as arguments so you can change them, use different messages and emails
    for email in emails:
        print(f"Sent to: {email}")
        print(f"Message: {message}")

emails = ["em1@gmail.com", "e2@gmail.com", "f3@gmail.com", "gg5@gmail.com"]
message = "Students must bring a pen!"
email_students(message, emails)

message = "Also an eraser please..."
email_students(message, emails)

message = "No pen, meant pencil!"
email_students(message, emails[:2]) #The first two

#Functions can turn into a value
def get_number_of_words(sentence):
    ls = sentence.split(" ")
    return len(ls) #Gives result of len(ls) #Return - goes out of the function

message = "The world is an amazing place!"
length = get_number_of_words(message)
print(length)

#Exercises:
#3
def greetings(name):
    print(f"Hello {name}!") #Forcing in the name, defining a function
    print(f"How are you {name}?")
    print(f"Good to see you {name}")

greetings("Diana")
greetings("Bedir")
greetings("Nilgun")

def name(first, last):
    print(f"Hey, {first} {last}.")

name("Diana", "S")

def nums(n1, n2):
    print(f"{n1} + {n2} = {n1 + n2}")

nums(1, 3) 
nums(2, 5)
nums(6, 6)

name = input("What's your name?")
print(f"Hi {name}")

n1 = int(input("First number: "))
n2 = int(input("Second number: "))
print(f"The sum is = {n1 + n2}")
