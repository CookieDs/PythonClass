#IF - ELSE
#Condition checker. If the condition is true..., if not... #1 if, 1 else, endless elif
#if condition:
    #code to run if true
#elif another condition:
    #code to run if another condition is true
#else:
    #code to run if none were true

#Condition > true / false
desserts = ["ice cream", "chocolate", "apple pie", "baklawa", "cookies"]
favourite_dessert = "chocolate"

for dessert in desserts:
    if dessert == favourite_dessert:
        print(f"{dessert} is my favourite!!")
    else:
        print(f"{dessert} is not the best but still really good!")

#Logical Tests
#a == b - if a is equal to b (value)
#a != b - if a is not equal to b (value)
#a > b   #a >= b   #a < b   #a <= b   #a in ls - checking if a is in the list
print(3 in [4, 5])
print("a" in "car")
print("Cat" == "cat") #Capital letters matter, they're not the same
print("Cat".lower() == "cat")

#Exercise:
#0 5 true, 5 false
print(5 >= 3)
print(5 <= 3)
print("yes" == "no")
print("no" in "I know") 
print(4 != 2) 
print(0 in [0, 9, 8, 7]) 
print("hey" in "no")
print(4 > 9)
print(8 == 8) 
print(3 <= 1) 

students = ["Bedir", "Tarik", "Diana", "Jonas", "Nilgun", "Joseph"]
if len(students) > 4:
    print("The class is big enough")

for student in students:
    if len(student) > 5: #If the length of the student name is bigger than 5
        print(f"The letters here are too crowded {student}")
    elif student [0] == "j":
        print(f"Well, who do we have here! Such an honor: {student}")
    else:
        print(f"Well this one is just perfect: {student}")

#Exercise
#1
names = ["Diana", "Bedir", "Nilgun", "Tarik"]
if len(names) > 3:
    print("The room is being crowded.")


if len(names) > 3:
    print("The room is being crowded.")

def crowd_test():
    if len(names) > 3:
        print("The room is too crowded.")

#2
if len(names) > 3:
    print("The room is being crowded.")
else:
    print("The room is not very crowded.")

#3
#names.append("Tarik")
#names.append("Yunus")
#names.append("Yusuf")

if len(names) > 5:
    print("There is a mob in the room.")
elif len(names) > 3:
    print("The room is being crowded.")
elif len(names) >= 1:
    print("The room is not being crowded.")
else:
    print("The room is being empty.")

#Every value has a true value
#Int 0 = false, the rest = true
def truth_value(value):
    if value:
        print(f"This {value}, {type(value)} evaluates to True") #Type shows which value it is: int, str etc.
    else:
        print(f"This {value}, {type(value)} evaluates to False")
truth_value(0)
truth_value(1)
truth_value(-1)

#Strings
truth_value("") #The only false one is empty, the rest are true

#Special - None
truth_value(None)

#Boolean / True - False
truth_value(True)
truth_value(False)

#Floats
truth_value(0.0) #False

# Q:
    # Make a list of ten aliens, each of which is one color: 'red', 'green', or 'blue'.
    # You can shorten this to 'r', 'g', and 'b' if you want, but if you choose this option you have to include a comment explaining what r, g, and b stand for.
    # Red aliens are worth 5 points, green aliens are worth 10 points, and blue aliens are worth 20 points.
    # Use a for loop to determine the number of points a player would earn for destroying all of the aliens in your list.

aliens = ["red", "blue", "red", "green", "green", "blue", "red", "green", "blue", "green"] #3 red, 4 green, 3 blue

points = []

for i in aliens:
    if i == "red":
        points.append(5)
    elif i == "green":
        points.append(10)
    elif i == "blue":
        points.append(20)
print("Points earned:", sum(points))

#Another way:
aliens = ["red", "blue", "red", "green", "green", "blue", "red", "green", "blue", "green"]
points = 0
for alien in aliens:
    if alien == "red":
        points = points + 5
    elif alien == "green":
        points = points + 10
    elif alien == "blue":
        points = points + 20
print(points)

# There are three groups of people in a class. The first group is the teacher, the second group is the students, and the third group is the parents.
    # The teacher is worth 5 points, the students are worth 10 points, and the parents are worth 15 points.
    # Use a for loop to determine the total number of points the class would earn if all groups were to give all of their points.
    # If a student is missing their parents, they should not be counted.
    # Make sure to include a comment explaining what the variables are.
    # Make the program dynamic so that it can be run with any list of people. (use functions)

# Input sample:
people =["t", "t", "p1", "p2", "p4", "p6", "s1", "s2", "s5", "s4", "s3"]
# Output:
    # - 100

g1 = ["t1", "t2"] #Group 2 with teachers
g2 = ["s1", "s2", "s3", "s4", "s5"] #Group with 5 students
g3 = ["p1", "p2", "p3", "p4", "p5", "p6"] #Group with 6 parents

#t - p(int < 10), s - p(int < 10)
