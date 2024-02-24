""" import cv2
import numpy as np

# Function to get user input for wall dimensions in centimeters
def get_wall_dimensions():
    length_cm = float(input("Enter the length of the wall in centimeters: "))
    breadth_cm = float(input("Enter the breadth of the wall in centimeters: "))
    return length_cm, breadth_cm

# Load the image
image_path = 'path/to/your/image.jpg'  # Replace with the actual image path
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection to find contours
edges = cv2.Canny(gray_image, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get user input for wall dimensions
length_cm, breadth_cm = get_wall_dimensions()

# Calculate pixel dimensions based on user input
height, width, _ = image.shape
pixels_per_cm_length = int(length_cm / width)
pixels_per_cm_breadth = int(breadth_cm / height)

# Draw contours on the image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Display wall dimensions on the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, f'Length: {length_cm} cm', (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(image, f'Breadth: {breadth_cm} cm', (10, 70), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Display the image with dimensions
cv2.imshow('Climbing Wall with Dimensions', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
 """

""" import cv2
import numpy as np

# Function to get user input for wall dimensions in centimeters
def get_wall_dimensions():
    length_cm = float(input("Enter the length of the wall in centimeters: "))
    breadth_cm = float(input("Enter the breadth of the wall in centimeters: "))
    return length_cm, breadth_cm

# Get user input for wall dimensions
length_cm, breadth_cm = get_wall_dimensions()

# Convert centimeters to pixels (assuming a scale factor)
pixels_per_cm = 10  # Adjust this scale factor based on your image resolution
length_pixels = int(length_cm * pixels_per_cm)
breadth_pixels = int(breadth_cm * pixels_per_cm)

# Create a white canvas representing the climbing wall
wall_image = np.ones((breadth_pixels, length_pixels, 3), dtype=np.uint8) * 255

# Display the wall dimensions on the canvas
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(wall_image, f'Length: {length_cm} cm', (10, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(wall_image, f'Breadth: {breadth_cm} cm', (10, 70), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

# Display the generated climbing wall
cv2.imshow('Generated Climbing Wall', wall_image)
cv2.waitKey(0)
cv2.destroyAllWindows() """


""" import cv2
import numpy as np

# Function to get user input for wall dimensions in centimeters and inclination angle
def get_wall_details():
    length_cm = float(input("Enter the length of the wall in centimeters: "))
    breadth_cm = float(input("Enter the breadth of the wall in centimeters: "))
    inclination_angle = float(input("Enter the inclination angle in degrees (0 for vertical): "))
    return length_cm, breadth_cm, inclination_angle

# Function to generate an inclined climbing wall image
def generate_inclined_wall(length_pixels, breadth_pixels, inclination_angle):
    wall_image = np.ones((breadth_pixels, length_pixels, 3), dtype=np.uint8) * 255

    # Convert inclination angle to radians
    inclination_angle_rad = np.radians(inclination_angle)

    # Calculate new width after applying inclination
    new_width = int(length_pixels / np.cos(inclination_angle_rad))

    # Define points for the climbing wall outline
    wall_outline = np.array([[0, 0], [length_pixels, 0], [new_width, breadth_pixels], [0, breadth_pixels]])

    # Rotate the wall outline to match the inclination angle
    rotation_matrix = cv2.getRotationMatrix2D((0, 0), inclination_angle, 1)
    rotated_outline = cv2.transform(np.array([wall_outline]), rotation_matrix).astype(int)[0]

    # Draw the inclined climbing wall on the canvas
    cv2.drawContours(wall_image, [rotated_outline], 0, (0, 0, 0), -1)

    return wall_image

# Get user input for wall details
length_cm, breadth_cm, inclination_angle = get_wall_details()

# Convert centimeters to pixels (assuming a scale factor)
pixels_per_cm = 10  # Adjust this scale factor based on your image resolution
length_pixels = int(length_cm * pixels_per_cm)
breadth_pixels = int(breadth_cm * pixels_per_cm)

# Generate the inclined climbing wall image
inclined_wall = generate_inclined_wall(length_pixels, breadth_pixels, inclination_angle)

# Display the inclined climbing wall
cv2.imshow('Inclined Climbing Wall', inclined_wall)
cv2.waitKey(0)
cv2.destroyAllWindows()
 """

""" import cv2
import numpy as np

# Function to get user input for wall dimensions in centimeters
def get_wall_dimensions():
    length_cm = float(input("Enter the length of the wall in centimeters: "))
    breadth_cm = float(input("Enter the breadth of the wall in centimeters: "))
    return length_cm, breadth_cm

# Get user input for wall dimensions
length_cm, breadth_cm = get_wall_dimensions()

# Convert centimeters to pixels (assuming a scale factor)
pixels_per_cm = 10  # Adjust this scale factor based on your image resolution
length_pixels = int(length_cm * pixels_per_cm)
breadth_pixels = int(breadth_cm * pixels_per_cm)

# Create a white canvas representing the climbing wall
wall_image = np.ones((breadth_pixels, length_pixels, 3), dtype=np.uint8) * 255

# Display the wall dimensions on the canvas
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(wall_image, f'Length: {length_cm} cm', (10, 30), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(wall_image, f'Breadth: {breadth_cm} cm', (10, 70), font, 1, (0, 0, 0), 2, cv2.LINE_AA)

# Display the generated climbing wall
cv2.imshow('Generated Climbing Wall', wall_image)
cv2.waitKey(0)
cv2.destroyAllWindows() """


""" import cv2
import numpy as np

# Function to get user input for wall dimensions in centimeters
def get_wall_dimensions():
    length_cm = float(input("Enter the length of the wall in centimeters: "))
    breadth_cm = float(input("Enter the breadth of the wall in centimeters: "))
    return length_cm, breadth_cm

# Get user input for wall dimensions
length_cm, breadth_cm = get_wall_dimensions()

# Convert centimeters to pixels (assuming a scale factor)
pixels_per_cm = 10  # Adjust this scale factor based on your image resolution
length_pixels = int(length_cm * pixels_per_cm)
breadth_pixels = int(breadth_cm * pixels_per_cm)

# Create a brown canvas representing the climbing wall (grid)
wall_image = np.ones((breadth_pixels, length_pixels, 3), dtype=np.uint8) * 165  # RGB values for brown

# Draw horizontal grid lines in white color
for i in range(0, breadth_pixels, int(breadth_pixels / )):
    cv2.line(wall_image, (0, i), (length_pixels, i), (255, 255, 255), 1)

# Draw vertical grid lines in white color
for j in range(0, length_pixels, int(length_pixels / 2)):
    cv2.line(wall_image, (j, 0), (j, breadth_pixels), (255, 255, 255), 1)

# Display the wall dimensions on the canvas
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(wall_image, f'Length: {length_cm} cm', (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(wall_image, f'Breadth: {breadth_cm} cm', (10, 70), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Display the generated climbing wall
cv2.imshow('Generated Climbing Wall', wall_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
 """

""" import cv2
import numpy as np

# Function to get user input for wall dimensions in centimeters
def get_wall_dimensions():
    length_cm = float(input("Enter the length of the wall in centimeters: "))
    breadth_cm = float(input("Enter the breadth of the wall in centimeters: "))
    return length_cm, breadth_cm

# Get user input for wall dimensions
length_cm, breadth_cm = get_wall_dimensions()

# Convert centimeters to pixels (assuming a scale factor)
pixels_per_cm = 10  # Adjust this scale factor based on your image resolution
length_pixels = int(length_cm * pixels_per_cm)
breadth_pixels = int(breadth_cm * pixels_per_cm)

# Create a brown canvas representing the climbing wall (grid)
wall_image = np.ones((breadth_pixels, length_pixels, 3), dtype=np.uint8) * 165  # RGB values for brown

# Draw horizontal grid lines in white color
for i in range(0, breadth_pixels, int(breadth_pixels / 100)):
    cv2.line(wall_image, (0, i), (length_pixels, i), (255, 255, 255), 1)

# Draw vertical grid lines in white color
for j in range(0, length_pixels, int(length_pixels / 100)):
    cv2.line(wall_image, (j, 0), (j, breadth_pixels), (255, 255, 255), 1)

# Display the wall dimensions on the canvas
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(wall_image, f'Length: {length_cm} cm', (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(wall_image, f'Breadth: {breadth_cm} cm', (10, 70), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Get the screen width and height
screen_width, screen_height = (1366, 768)  # Change these values to your screen resolution

# Resize the wall image to fit the screen
scaled_wall_image = cv2.resize(wall_image, (screen_width, screen_height))

# Display the generated climbing wall
cv2.imshow('Generated Climbing Wall', scaled_wall_image)
cv2.waitKey(0)
cv2.destroyAllWindows() """


""" import cv2
import numpy as np

# Function to get user input for wall dimensions in centimeters
def get_wall_dimensions():
    length_cm = float(input("Enter the length of the wall in centimeters: "))
    breadth_cm = float(input("Enter the breadth of the wall in centimeters: "))
    return length_cm, breadth_cm

# Get user input for wall dimensions
length_cm, breadth_cm = get_wall_dimensions()

# Convert centimeters to pixels (assuming a scale factor)
pixels_per_cm = 10  # Adjust this scale factor based on your image resolution
length_pixels = int(length_cm * pixels_per_cm)
breadth_pixels = int(breadth_cm * pixels_per_cm)

# Create a brown canvas representing the climbing wall (grid)
wall_image = np.ones((breadth_pixels, length_pixels, 3), dtype=np.uint8) * 165  # RGB values for brown

# Draw horizontal grid lines in white color
for i in range(0, breadth_pixels, int(breadth_pixels / 10)):
    cv2.line(wall_image, (0, i), (length_pixels, i), (255, 255, 255), 1)

# Draw vertical grid lines in white color
for j in range(0, length_pixels, int(length_pixels / 10)):
    cv2.line(wall_image, (j, 0), (j, breadth_pixels), (255, 255, 255), 1)

# Display the climbing wall
cv2.imshow('Generated Climbing Wall', wall_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Obtain length and breadth in pixels
print(f"Length in pixels: {length_pixels}")
print(f"Breadth in pixels: {breadth_pixels}")

# Calculate pixel-to-cm conversion factor
pixel_to_cm_conversion_factor = pixels_per_cm
print(f"Pixel to cm conversion factor: {pixel_to_cm_conversion_factor}")
 """


import cv2
import numpy as np

# Function to get user input for wall dimensions in centimeters
def get_wall_dimensions():
    length_cm = float(input("Enter the length of the wall in centimeters: "))
    breadth_cm = float(input("Enter the breadth of the wall in centimeters: "))
    return length_cm, breadth_cm

# Function to get user input for grid difficulty level
def get_difficulty_level():
    difficulty_level = input("Enter difficulty level (easy, medium, hard): ").lower()
    if difficulty_level not in ["easy", "medium", "hard"]:
        print("Invalid difficulty level. Using 'medium' as default.")
        difficulty_level = "medium"
    return difficulty_level

# Get user input for wall dimensions and difficulty level
length_cm, breadth_cm = get_wall_dimensions()
difficulty_level = get_difficulty_level()

# Convert centimeters to pixels (assuming a scale factor)
pixels_per_cm = 10  # Adjust this scale factor based on your image resolution
length_pixels = int(length_cm * pixels_per_cm)
breadth_pixels = int(breadth_cm * pixels_per_cm)

# Create a brown canvas representing the climbing wall
wall_image = np.ones((breadth_pixels, length_pixels, 3), dtype=np.uint8) * 165  # RGB values for brown

# Draw a grid on the wall
grid_size = 100  # Adjust the grid size based on your preference
cell_size = length_pixels // grid_size

for i in range(0, breadth_pixels, cell_size):
    cv2.line(wall_image, (0, i), (length_pixels, i), (255, 255, 255), 1)

for j in range(0, length_pixels, cell_size):
    cv2.line(wall_image, (j, 0), (j, breadth_pixels), (255, 255, 255), 1)

# Display the climbing wall with grid
cv2.imshow('Climbing Wall with Grid', wall_image)
cv2.waitKey(0)

# Calculate the size of the cells in centimeters
cell_size_cm = float(cell_size) / pixels_per_cm
print(f"Size of each cell in the grid: {cell_size_cm:.2f} cm")

# Draw points representing holds positions based on difficulty level
holds_positions = []
for i in range(0, breadth_pixels, cell_size):
    for j in range(0, length_pixels, cell_size):
        holds_positions.append((j, i))

# Draw points on the image based on difficulty level
if difficulty_level == "easy":
    holds_color = (0, 255, 0)  # Green for easy holds
elif difficulty_level == "medium":
    holds_color = (0, 0, 255)  # Red for medium holds
else:
    holds_color = (255, 0, 0)  # Blue for hard holds

for position in holds_positions:
    cv2.circle(wall_image, position, 5, holds_color, -1)

# Display the climbing wall with holds
cv2.imshow('Climbing Wall with Holds', wall_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

