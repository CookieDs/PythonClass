'''
_____________________________________
|             |            |        |
|   Bedroom     Living R.           |
|__________  _|____  ______| Garage |
|             |                     |
|   Kitchen       Hallway  |________| 
|_____________|              Toilet |
              |____---_____|________|        
-----------------------------------------------------------------
'''


def start_menu():
    print('''
    --------------------------------------------------
     _____ _   _ _____   _   _  ___  _   _ ____  _____ 
    |_   _| | | | ____| | | | |/ _ \| | | / ___|| ____|
      | | | |_| |  _|   | |_| | | | | | | \___ \|  _|  
      | | |  _  | |___  |  _  | |_| | |_| |___) | |___ 
      |_| |_| |_|_____| |_| |_|\___/ \___/|____/|_____|
                                               
    --------------------------------------------------
    ''')
    '''
    This function displays the start menu for the game.
    Menu will look like this:
    --------------------------------------------------
     _____ _   _ _____   _   _  ___  _   _ ____  _____ 
    |_   _| | | | ____| | | | |/ _ \| | | / ___|| ____|
      | | | |_| |  _|   | |_| | | | | | | \___ \|  _|  
      | | |  _  | |___  |  _  | |_| | |_| |___) | |___ 
      |_| |_| |_|_____| |_| |_|\___/ \___/|____/|_____|
                                               
    --------------------------------------------------
    1. Start game
    2. Quit game
    --------------------------------------------------
    
    Use a list to store the options.
    '''
    options = ["Start game", "Quit game"]
    choice = ""

    while choice != "1":    
        for i, option in enumerate(options):
            print(str(i+1) + ". " + option) # TODO: Print the options for user to choose from (5 points)
        choice = input("Please choose an index: ")
        if choice == "1":
            pass
        elif choice == "2":
            print("Thanks for playing!")
            exit()
        else:
            print("Error. Choice was invalid, please choose again.")

    # TODO: Get the user's choice and store it in a variable (5 points)
    # Hint: Use the input function

    # TODO: Use a conditional statement to check if the 
    # user's choice is valid and if not, display an error
    # message and ask the user to choose again. If user 
    # chooses to quit, exit the game. (5 points)
    # Hint: Use the while loop
    # Hint: Use exit() function to exit the game


def house_init():
    '''
    This function initializes the house. Sets up all the rooms
    and the items - what they do.
    Returns to the dictionary of the house.
    '''
    # TODO: Complete the house dictionary. Every room must have
    # at least 3 tools and all the exits (check the map for the exits). 
    # The tools can be either pickable or not.
    # Every tool must have a description, a statement that
    # says if the tool is pickable or not, and action that
    # the player can do with the tool. You can edit the description
    # and the action as the story progresses. (20 points)
    house = {
        "Living Room": {
            "Description": "You are in the living room. You see a fireplace, a torch, a window, and a blood stain on the floor.",
            "Fireplace": {
                "description": "Fireplace seems to be off, if only there was something to light it up...",
                "pickable": False,
                "action": "Find a way to light the fire."
            },
            "Torch": {
                "description": "You see a torch laying on the floor next to the fireplace.",
                "pickable": True,
                "action": "Use it to set a fire in the fireplace."
            },
            "Window": {
                "description": "You see a covered up window.",
                "pickable": False,
                "action": "Investigate it.",

                "Window Close Up": {
                    "description": "You see planks nailed over the window and you understand that you do't have a way to get through them.",
                    "pickable": False,
                    "action": "None, go back."
                }
            },
            "Blood Stain": {
                "description": "You see some dark red, sticky blood on the floor.",
                "pickable": False,
                "action": "Investigate it.",

                "Carpet": {
                    "description": "You see that the blood is staining a carpet and even going through it.",
                    "pickable": False,
                    "action": "Lift the carpet to see what's underneath.",

                    "Key": {
                        "description": "You see a key laying there on the floor under the carpet.",
                        "pickable": True,
                        "action": "Pick it up and put it in your pocket."
                    }
                }
            },
            "Exits": ["Hallway", "Garage", "Bedroom"],
        },
        "Bedroom": {
            "Description": "You're in the bedroom. You see a bed, broken mirror, and a closet.",
            "Bed": {
                "description": "There is a bed in the corner.",
                "pickable": False,
                "action": "Lift the blanket.",

                "Mobile Phone": {
                    "description": "There is a cracked mobile phone laying underneath the covers but it seems to be off.",
                    "pickable": True,
                    "action": "None, it's out of function."
                },
            },
            "Broken Mirror": {
                "description": "You see glass on the floor from a broken mirror by the bed.",
                "pickable": False,
                "action": "Touch it." #If you do so you will cut yourself.
            },
            "Closet": {
                "description": "There is a closet that is slightly open.",
                "pickable": False,
                "action": "Open it up.",

                "Dead Body": {
                    "description": "Among the clothes in the closet you see a dead body laying there.",
                    "pickable": False,
                    "action": "Leave it alone and close the closet's doors."
                }
            },
            "Exits": ["Living Room", "Kitchen"]
        },
        "Kitchen": {
            "Description": "You are in the kitchen. You see a fridge, drawers, oven and a sink.",
            "Fridge": {
                "description": "There is a fridge by the entrance.",
                "pickable": False,
                "action": "Open the fridge.",

                "Yoghurt": {
                    "description": "There's some yoghurt in the fridge. Maybe use a spoon to eat it?",
                    "pickable": True,
                    "action": "Eat it."
                },
                "Eggs": {
                    "description": "There are some eggs in the fridge.",
                    "pickable": True,
                    "action": "Throw them at someone or something.", #Add "with eggs on it." on the item's description or name after they throw the eggs on it.
                }
            },
            "Drawers": {
                "description": "There are drawers under the counters.",
                "pickable": False,
                "action": "Open the drawers.",

                "Spoon": {
                    "description": "There is a spoon in the drawers.",
                    "pickable": True,
                    "action": "Use it to eat.",
                },
                "Flashlight": {
                    "description": "There is a flashlight in the drawers.", # but it doesn't have any batteries.",
                    "pickable": True,
                    "action": "Turn it on/off.", #Only works if you put batteries in.
                }
            },
            "Oven": {
                "description": "There is an oven by the sink.",
                "pickable": False,
                "action": "Turn it on."
            },
            "Sink": {
                    "description": "There is a sink.",
                    "pickable": False,
                    "action": "Turn the faucet on.",
                },
            "Exits": ["Hallway", "Bedroom"],
        },
        "Hallway": {
            "Description": "You are in the hallway. You see a carpet and shoes on the floor and a lock in the door.",
            "Carpet": {
                "description": "There is a carpet on the floor with mud stains on it.",
                "pickable": False,
                "action": "Lift the carpet.",

                "Cockroaches": {
                    "description": "You see some cockroaches under the carpet, nothing else.",
                    "pickable": True,
                    "action": "Crush them."
                },
            },
            "Shoes": {
                "description": "There are pairs of shoes on the floor by the door.",
                "pickable": True,
                "action": "Wear a pair."
            },
            "Lock": {
                "description": "There's a lock on the door.",
                "pickable": False,
                "action": "Put a key in it and unlock it."
            },
            "Exits": ["Kitchen", "Garage", "Living Room", "Bathroom", "Outside"],
        },
        "Garage": {
            "Description": "You are in the garage. You see a cabinet, tires and a tool box.",
            "Cabinet": {
                "description": "There is an old cabinet in the corner.",
                "pickable": False,
                "action": "Open it.",

                "Batteries": {
                    "description": "You found batteries laying in the cabinet.",
                    "pickable": True,
                    "action": "Put them in the flaslight.",
                },
                "Gun": {
                    "description": "There is a gun laying in the cabinet.",
                    "pickable": True,
                    "action": "Shoot!"
                },
            },
            "Tires": {
                "description": "There are some tires on the floor.",
                "pickable": False,
                "action": "Attempt to turn them over, they are heavy though."
            },
            "Tool Box": {
                "description": "There is a tool box on the floor.",
                "pickable": False,
                "action": "Open it.",

                "Screwdriver": {
                    "description": "There is a screwdriver to unscrew screws.",
                    "pickable": True,
                    "action": "Unscrew screws."
                },
                "Hammer":{
                    "description": "There is a hammer in the tool box.",
                    "pickable": True,
                    "action": "Hit it."
                },
                "Nails":{
                    "description": "There are nails in the tool box.",
                    "pickable": True,
                    "action": "Nail them to the wall using a hammer."
                }
            },
            "Exits": ["Hallway", "Living Room"],
        },
        "Bathroom": {
            "Description": "You are in the bathroom. You see a toilet, sink, cabinet over the sink and a laundry basket.",
            "Toilet": {
                "description": "There is a toilet.",
                "pickable": False,
                "action": "Flush the toilet."
            },
            "Sink": {
                "description": "There is a sink next to the toilet.",
                "pickable": False,
                "action": "Turn the faucet on."
            },
            "Laundry Basket": {
                "description": "There's a laundry basket that smells...",
                "pickable": False,
                "action": "Open the laundry basket.",

                "Stained Cloths": {
                    "description": "You see blood-stained cloths in the laundry basket.",
                    "pickable": True,
                    "action": "Put them on.", #I don't know why you would do that but it's your choice.
                }
            },
            "Cabinet Over Sink": {
                "description": "There's a cabinet over the sink that has blood stains on.",
                "pickable": False,
                "action": "Open it.",

                "Pills": {
                    "description": "You see flipped over pill bottles with pills everwhere.",
                    "pickable": True,
                    "action": "Take them." #Not a smart decision but I give the option. #In the story, if he takes the pills: After swallowing the pills, you hear steps behind you and you start feeling unwell. You fall unconsious. Game over. Exit game.
                },
            },
            "Exits": ["Hallway"],
        }
    }

    return house

def display_story(house, current_room):
    '''
    This function displays the story of the game given player's
    and house's information.
    '''
    room = house[current_room]
    print("\n" + room["Description"])
    #print("Exits: " + str(room["Exits"]))
    
    for key, value in room.items():
        if key != "Description":
            print(key)
    
    
    # TODO: Display items in the room (9 points)
    
    print("\n")


def examine_item(house, current_room, item, player_inventory):
    '''
    Given the house and the current room, this function will
    examine the selected item.
    '''
    room = house[current_room]
    items = room[item]
    print("\n" + items["description"])
    if items["pickable"] == True:
        print(f"\n{item} is pickable.")
    elif items["pickable"] == False:
        print(f"\n{item} is not pickable.")
    
    if items["pickable"] == True:
        pick = input("Do you want to pick up the item, yes or no?")
        if pick == "yes":
            player_inventory.append(pick)
        elif pick == "no":
            pass
        else:
            print("yes or no?")
    
        
    
    # TODO: Complete the function (40 points)
    # Hint: Use the house dictionary to get the item's description
    # Hint: Use the house dictionary to get the item's pickable status
    


def play_game(house):
    '''
    This function plays the game given the player and house
    information.
    '''
    print("Welcome to the game!")
    # clearing the screen
    print("\n" * 100)
    
    # Story starts here
    # -Name- wakes up with a unbearable pain in the back of his head.
    # He doesn't remember how he got there. He's not sure how long he
    # was laying there on the floor. It is pitch black and he can't see
    # anything. He tries to turn on the light, but it doesn't work...
    print("You wake up with a unbearable pain in the back of your head.")
    print("You don't remember how you got there.") 
    print("You're not sure how long you were laying there on the floor.")
    print("It is pitch black and you can't see anything.")
    print("You try to turn on the light, but it doesn't work...")
    print("\n")

    current_room = "Bedroom"
    player_inventory = {}
    choice = ''
    room = house[current_room]

    # Continue the story until the player reaches the end or exits the game
    while choice != 'quit':
        display_story(house, current_room)
        action = input("What do you want to do? ")
        choice = action.title().strip()
        if choice == "Exits":
            print("Exits: " + room["Exits"])
            go = input("Where do you want to go?")
            if go in room["Exits"]:
                current_room = go
            elif go == "return":
                return
            else:
                print("Choose one of the exits or return.")
                return       
        elif choice in room: #If an item if selected
            examine_item(house, current_room, choice, player_inventory)
        elif choice == "quit":
            exit()
        elif choice == "Outside": #To win
            if current_room == "Hallway":
                #if lock 
                print("You got out of the house, congratulations!")
                exit()
        elif choice in player_inventory:
            print(player_inventory)
            choice_inventory = input(f"Do you want to use {choice}?")
            if choice_inventory.lower().strip() == "yes":
                print(choice["action"])
            elif choice_inventory.lower().strip() == "no":
                return
        else:
            print("Error. The action was not valid, choose again.")


        # TODO: Check if the action is valid. If not, display an error 
        # message and ask the user to choose again. If user chooses to quit,
        # exit the game. (5 points)

        # TODO: The player can either move to a new room or examine an item.
        # If the player moves to a new room, update the current_room. If the
        # player examines an item, call the examine_item function. Update the
        # player's inventory if necessary. (5 points)
        # Hint: Use the if-elif-else statement

        # TODO: If the player is out of the house, display a message
        # and exit the game. (5 points)
        

def main():
    # main function
    # This is where the logic of the game will be.
    
    # Starting menu for the game displayed
    start_menu()
    print("Welcome to my game, The House.")
    # TODO: Greet the player. (1 point)

    # Initialize the house
    house = house_init()

    # play the game
    play_game(house)

    # Greetings and goodbye
    print("Thank you for playing!")
    print("Goodbye!")

print(main())