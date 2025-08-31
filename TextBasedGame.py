# Cathrine Karangi

def display_message(message):
    """Display a message to the player."""
    print(message)

def show_instructions():
    """Display game instructions and available commands."""
    instructions = [
        "Treasure Hunt Adventure Game",
        "Collect 3 items to win the game, or be captured by the villain.",
        "Move commands: go North, go South, go East, go West",
        "Add to Inventory: get 'item name'"
    ]
    for line in instructions:
        display_message(line)

def update_room(direction, current_room, rooms):
    """Update the player's room based on direction and current room."""
    if direction in rooms[current_room] and rooms[current_room][direction] is not None:
        return rooms[current_room][direction]
    display_message("You can’t go that way!")
    return current_room  # Stay in the same room if direction is invalid or outside map

def show_status(current_room, inventory, rooms):
    """Display the player's current room, inventory, and any item in the room."""
    display_message(f"You are in the {current_room}")
    display_message(f"Inventory: {inventory}")
    if 'Item' in rooms[current_room] and rooms[current_room]['Item'] != 'None':
        display_message(f"You see a {rooms[current_room]['Item']}")
    available_directions = [d for d in ['North', 'South', 'East', 'West'] if d in rooms[current_room] and rooms[current_room][d] is not None]
    display_message(f"Available directions: {', '.join(available_directions)}")
    display_message("---------------------------")
    display_message("Enter your move:")

def main():
    """Main function to handle the game logic and flow."""
    inventory = []  # Player's inventory starts empty
    rooms = {
        'Entrance Hall': {'North': None, 'South': 'Library', 'East': 'Garden', 'West': 'Dining Room', 'Item': 'None'},
        'Library': {'North': 'Entrance Hall', 'South': None, 'Item': 'Book'},
        'Garden': {'West': 'Entrance Hall', 'Item': 'Flower'},
        'Dining Room': {'East': 'Entrance Hall', 'North': 'Treasure Room', 'Item': 'Key'},
        'Treasure Room': {'South': 'Dining Room', 'Boss': True, 'Item': 'None'}
    }

    current_room = 'Entrance Hall'  # Starting room
    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)
        move = input().lower().strip()

        if move == 'quit':  # Allow player to exit the game
            break

        # Handle movement between rooms
        if move.startswith('go '):
            direction = move[3:].capitalize()
            current_room = update_room(direction, current_room, rooms)  # Single call per move

        # Handle getting items from the room
        elif move.startswith('get '):
            item = move[4:].capitalize()
            if 'Item' in rooms[current_room] and rooms[current_room]['Item'] != 'None' and item == rooms[current_room]['Item'] and item not in inventory:
                inventory.append(item)
                display_message(f"{item} retrieved!")
            else:
                display_message("Can’t get that!")

        # Handle invalid commands
        else:
            display_message("Invalid Input!")

        # Check win or lose conditions
        if 'Boss' in rooms[current_room]:
            if len(inventory) == 3:
                display_message("Congratulations! You have collected all items and defeated the villain!")
                display_message("Thanks for playing the game. Hope you enjoyed it.")
                break
            else:
                display_message("The villain captured you...GAME OVER!")
                display_message("Thanks for playing the game. Hope you enjoyed it.")
                break

if __name__ == "__main__":
    main()