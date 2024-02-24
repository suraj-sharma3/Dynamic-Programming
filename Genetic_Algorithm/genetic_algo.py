''' def generate_hold_positions(num_holds, wall_height, wall_width, current_position=[]):
    """
    Generate all possible positions for a certain number of holds on a climbing wall.

    Parameters:
    - num_holds: Number of holds to be placed on the wall.
    - wall_height: Height of the climbing wall.
    - wall_width: Width of the climbing wall.
    - current_position: Current position being considered during recursion.

    Returns:
    A list of lists, where each inner list represents a valid hold configuration.
    """
    # Base case: If the number of holds to place is zero, return the current position.
    if num_holds == 0:
        return [current_position]

    # Recursive case: Try placing a hold at each possible position.
    all_positions = []
    for height in range(wall_height):
        for width in range(wall_width):
            # Ensure the hold is placed within the wall boundaries.
            if (height, width) not in current_position:
                # Recursively explore the next hold position.
                next_positions = generate_hold_positions(
                    num_holds - 1,
                    wall_height,
                    wall_width,
                    current_position + [(height, width)],
                )
                all_positions.extend(next_positions)

    return all_positions

# Example usage:
num_holds = 3
wall_height = 4
wall_width = 5
hold_positions = generate_hold_positions(num_holds, wall_height, wall_width)

# Print the generated hold positions
for position in hold_positions:
    print(position)
'''
'''
def generate_hold_positions_in_grid(num_holds, wall_height, wall_width, grid_size, current_position=[]):
    """
    Generate all possible positions for a certain number of holds on a climbing wall grid.

    Parameters:
    - num_holds: Number of holds to be placed on the wall.
    - wall_height: Height of the climbing wall.
    - wall_width: Width of the climbing wall.
    - grid_size: Size of each grid cell (side length of a square cell).
    - current_position: Current position being considered during recursion.

    Returns:
    A list of lists, where each inner list represents a valid hold configuration.
    """
    # Calculate the number of cells in the height and width directions
    num_cells_height = wall_height // grid_size
    num_cells_width = wall_width // grid_size

    # Base case: If the number of holds to place is zero, return the current position.
    if num_holds == 0:
        return [current_position]

    # Recursive case: Try placing a hold at each possible position within the grid.
    all_positions = []
    for cell_height in range(num_cells_height):
        for cell_width in range(num_cells_width):
            # Calculate the actual position in the wall based on the grid cell
            height = cell_height * grid_size
            width = cell_width * grid_size

            # Ensure the hold is placed within the wall boundaries.
            if (height, width) not in current_position:
                # Recursively explore the next hold position.
                next_positions = generate_hold_positions_in_grid(
                    num_holds - 1,
                    wall_height,
                    wall_width,
                    grid_size,
                    current_position + [(height, width)],
                )
                all_positions.extend(next_positions)

    return all_positions

# Example usage:
num_holds = 3
wall_height = 4
wall_width = 6
grid_size = 2
hold_positions = generate_hold_positions_in_grid(num_holds, wall_height, wall_width, grid_size)

# Print the generated hold positions
for position in hold_positions:
    print(position)
'''

def generate_hold_positions_in_grid(num_holds, wall_height, wall_width, grid_size, current_position=[]):
    """
    Generate all possible positions for a certain number of holds on a climbing wall grid.

    Parameters:
    - num_holds: Number of holds to be placed on the wall.
    - wall_height: Height of the climbing wall.
    - wall_width: Width of the climbing wall.
    - grid_size: Size of each grid cell (side length of a square cell).
    - current_position: Current position being considered during recursion.

    Returns:
    A list of lists, where each inner list represents a valid hold configuration.
    """



def generate_hold_positions_in_grid(num_holds, wall_height, wall_width, grid_size, current_position=[]):
    """
    Generate all possible positions for a certain number of holds on a climbing wall grid.

    Parameters:
    - num_holds: Number of holds to be placed on the wall.
    - wall_height: Height of the climbing wall.
    - wall_width: Width of the climbing wall.
    - grid_size: Size of each grid cell (side length of a square cell).
    - current_position: Current position being considered during recursion.

    Returns:
    A list of lists, where each inner list represents a valid hold configuration.
    """
    # Calculate the number of cells in the height and width directions
    num_cells_height = wall_height // grid_size
    num_cells_width = wall_width // grid_size

    # Base case: If the number of holds to place is zero, return the current position.
    if num_holds == 0:
        return [current_position]

    # Recursive case: Try placing a hold at each possible position within the grid.
    all_positions = []
    for cell_height in range(num_cells_height):
        for cell_width in range(num_cells_width):
            # Calculate the actual position in the wall based on the grid cell
            height = cell_height * grid_size
            width = cell_width * grid_size

            # Ensure the hold is placed within the wall boundaries.
            if (height, width) not in current_position:
                # Recursively explore the next hold position.
                next_positions = generate_hold_positions_in_grid(
                    num_holds - 1,
                    wall_height,
                    wall_width,
                    grid_size,
                    current_position + [(height, width)],
                )
                all_positions.extend(next_positions)

    return all_positions

def print_grid_information(wall_height, wall_width, grid_size):
    num_cells_height = wall_height // grid_size
    num_cells_width = wall_width // grid_size

    cell_side_length = grid_size
    cell_area = cell_side_length ** 2

    total_grid_area = wall_height * wall_width

    print(f"Grid Information:")
    print(f"Number of Cells (Rows x Columns): {num_cells_height} x {num_cells_width}")
    print(f"Side Length of Each Cell: {cell_side_length}")
    print(f"Area of Each Cell: {cell_area}")
    print(f"Area of the Entire Grid: {total_grid_area}")
    print(f"Relation between Cell Area and Grid Area: {cell_area}/{total_grid_area}")

# Example usage:
num_holds = 50
wall_height = 400
wall_width = 400
grid_size = 20
hold_positions = generate_hold_positions_in_grid(num_holds, wall_height, wall_width, grid_size)

# Print the generated hold positions
print("Hold Positions:")
for position in hold_positions:
    print(position)

# Print grid information
print("\n")
print_grid_information(wall_height, wall_width, grid_size)


