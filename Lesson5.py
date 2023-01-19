#While loops #Runs in specific conditions
#while condition:
#    run the code as long as condition is satisfied
'''
health = 5
while health: #Runs until it's not true?
    print(f"Still fighting..! Health: {health}")
    health = health - 1

print("You are dead now.") 

# Make a variable called strength, and set its initial value to 5.
    # Print a message reporting the player's strength.
    # Set up a while loop that runs until the player's strength increases to a value such as 10.
    # Inside the while loop, print a message that reports the player's current strength.
    # Inside the while loop, write a statement that increases the player's strength.
# Outside the while loop, print a message reporting that the player has grown too strong, and that they have moved up to a new level of the game.
    # Bonus: Play around with different cutoff levels for the value of strength, and play around with different ways to increase the strength value within the while loop.

strength = 5

while strength:
    print(f"Your strength is: {strength}")
    #print("Your strenght increased by 1")
    strength = strength + 1
    if strength == 11:
        break

#Input taking
#var = input("message") #Takes it as a string
names = ["Diana"]
another_name = input("A name I should know:")
names.append(another_name)
print(names)

#Exercises:
#0
games = ["lol", "Minecraft", "Wild rift"]
print("I like to play:", games)
another_game = input("What games do you like?")
games.append(another_game)
print("We like to play:", games)

#While loops - keep it running
names = []
new_name = ""
while new_name != "quit":
    new_name = input("Give me a name (type quit if you want ot stop): ")
    if new_name != "quit":
        names.append(new_name)
print(names)

#Dictionaries
l = [3, 4]
l[0] #In a list, num
#dct = {}
# dct = {
#   key: value
# }

dct = {
    "bedroom": "beautiful room", #Colon between the key and the value
    3: "Hi there"
}
print(dct["bedroom"]) #Prints the value
print(dct[3])


#While - Menu #Making a game together
def play_game():
    pass
def display_options():
    pass

choice = ""

#The reason we use while loop is becuase if they choose a wrong choice it plays infinitly until it's a right input
while choice != "q":
    print("[1] Start the game")
    print("[2] Options")
    print("[q] to quit")
    #Ask the user
    choice = input("Please choose an index: ")

    if choice == "1":
        play_game()
    elif choice == "2":
        display_options()
    elif choice == "q":
        print("Thanks for visiting!")
    else:
        print("\nWrong input, please choose from the list.")
'''
#Exercises:
#1: #Giving the keys values
animals = {
    "Hanna": "dog",
    "Molly": "rabbit",
    "Lisa": "cat"
}

for key, value in animals.items(): #Using a loop to print out every key and its value from the dictionary
    print(f"{key} is a {value}.")
for key, value in animals.items():
    print(key)
print(animals)
