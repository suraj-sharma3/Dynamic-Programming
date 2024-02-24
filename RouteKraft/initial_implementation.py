import random

# Function to generate random hold types for demonstration purposes
def generate_hold_type(category):
    if category == "Beginner":
        return random.choice(["Jug", "Crimp", "Pocket"])
    elif category == "Intermediate":
        return random.choice(["Sloper", "Edge", "Pinch"])
    elif category == "Expert":
        return random.choice(["Volume", "Gaston", "Undercling"])

# Function to generate holds based on user inputs
def generate_climbing_wall(rectangular_dimensions, climber_experience, climber_height):
    wall_width, wall_height = rectangular_dimensions

    # Assume a simple grid for hold placement (you can modify this based on your algorithm)
    hold_positions = [(i, j) for i in range(wall_width) for j in range(wall_height)]

    # Determine hold category based on climber's experience
    if climber_experience == "Beginner":
        hold_category = "Easy"
    elif climber_experience == "Intermediate":
        hold_category = "Medium"
    elif climber_experience == "Expert":
        hold_category = "Hard"

    # Generate and print holds for each position
    for position in hold_positions:
        x, y = position
        hold_type = generate_hold_type(hold_category)
        print(f"Place {hold_type} hold at position ({x}, {y}) for {climber_experience} climber.")

# Example usage
rectangular_dimensions = (5, 5)  # Example: 5 meters by 5 meters wall
climber_experience = "Intermediate"
climber_height = 180  # Example: 180 cm

generate_climbing_wall(rectangular_dimensions, climber_experience, climber_height)
