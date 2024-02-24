  
""" # Function to draw centers on the image
def draw_centers(image, centers, save_path):
    img_with_centers = image.copy()
    for center in centers:
        center = tuple(map(int, center))  # Convert center coordinates to integers
        cv2.circle(img_with_centers, center, 3, (0, 255, 0), -1)

    # Save the image with centers
    cv2.imwrite(save_path, img_with_centers)

# Generate a random number of cells for the grid
num_cells = np.random.randint(0, total_cells)  # Random number of cells between 5 and 15

# Generate random centers for the specified number of cells
centers = []
for row in range(0, wall_width, cell_side):
    for col in range(0, wall_width, cell_side):
        center = (col + cell_side // 2, row + cell_side // 2)
        centers.append(center)

# Draw centers on the image and save it
output_folder = 'C:\\Users\\OMOLP094\\Desktop\\Dynamic-Programming\\Generated_Routes_Images\\'
os.makedirs(output_folder, exist_ok=True)
output_image_path = os.path.join(output_folder, 'random_centers.png')
draw_centers(wall_img, centers, output_image_path) """