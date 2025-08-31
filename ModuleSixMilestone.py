# Cathrine Karangi
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# Start the game in the Great Hall
current_room = 'Great Hall'

# Show initial instructions
print("Welcome to the Dragon Text Game!")
print("Commands: go north, go south, go east, go west, or exit")
print("You are currently in the", current_room)

# Gameplay loop
while current_room != 'exit':
    # Show player's status
    print("\nYou are in the", current_room)
    command = input("Enter your command: ").lower().strip()

    if command == 'exit':
        current_room = 'exit'
    elif command in ['go north', 'go south', 'go east', 'go west']:
        direction = command[3:].capitalize()
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!")
    else:
        print("Invalid command! Use go north, go south, go east, go west, or exit.")

# End game message
if current_room == 'exit':
    print("Thanks for playing the game. Hope you enjoyed it!")# Cathrine Karangi
# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# Start the game in the Great Hall
current_room = 'Great Hall'

# Show initial instructions
print("Welcome to the Dragon Text Game!")
print("Commands: go north, go south, go east, go west, or exit")
print("You are currently in the", current_room)

# Gameplay loop
while current_room != 'exit':
    # Show player's status
    print("\nYou are in the", current_room)
    command = input("Enter your command: ").lower().strip()

    if command == 'exit':
        current_room = 'exit'
    elif command in ['go north', 'go south', 'go east', 'go west']:
        direction = command[3:].capitalize()
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!")
    else:
        print("Invalid command! Use go north, go south, go east, go west, or exit.")

# End game message
if current_room == 'exit':
    print("Thanks for playing the game. Hope you enjoyed it!")