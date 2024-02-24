import cv2
import numpy as np
from random import randint
from scipy.spatial.distance import euclidean



wall_width = int(input("Enter the climbing wall's width in cms : "))

# Minimum wall width = 200 cms
while wall_width < 200: 
    wall_width = int(input("Kindly input a value equal to 200 or more in cms (200 cms = 80 inches = 6.66 Feet) for Width of the Wall : "))

wall_height = int(input("Enter the climbing wall's height in cms : "))

# Minimum wall height = 200 cms
while wall_height < 200: 
    wall_width = int(input("Kindly input a value equal to 200 or more in cms (200 cms = 80 inches = 6.66 Feet) for Height of the Wall : "))

# Creating the wall image
wall_img = np.full((wall_width, wall_height, 3), fill_value=127, dtype = np.uint8)

climber_height = int(input("Enter your height in cms : "))

first_hold_x = wall_width // 2

first_hold_y = randint(climber_height // 2, climber_height)

first_hold_y = wall_height - first_hold_y 

first_hold = [first_hold_x, first_hold_y]

""" 
# Redundant for first hold
while True:
    if (first_hold_x >= 0 and first_hold_x <= wall_width) and (first_hold_y >= 0 and first_hold_y <= wall_height):
       break
    if first_hold_x < 0 or first_hold_x > wall_width:
        first_hold_x = randint(50, wall_width - 50)
        first_hold[0] = first_hold_x
    if first_hold_y < 0 or first_hold_y > wall_height:
        first_hold_y = randint(climber_height // 2, climber_height)
        first_hold[1] = first_hold_y """

print(f"First Hold Coordinates : {first_hold}")

cv2.circle(wall_img, tuple(first_hold), 4, (0, 0, 255), -1)
text = f"First Hold : ({first_hold_x}, {first_hold_y})"
cv2.putText(wall_img, text, (first_hold[0] + 5, first_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

second_hold_x = randint(first_hold_x - 50, first_hold_x + 50)

second_hold_y = randint(first_hold_y + 30, first_hold_y + 50)

second_hold_y = wall_height - second_hold_y

second_hold = [second_hold_x, second_hold_y]

while True:
    if (second_hold_x >= 0 and second_hold_x <= wall_width) and (second_hold_y >= 0 and second_hold_y <= wall_height):
       break
    if second_hold_x < 0 or second_hold_x > wall_width:
        second_hold_x = randint(first_hold_x - 50, first_hold_x + 50)
        second_hold[0] = second_hold_x
    if second_hold_y < 0 or second_hold_y > wall_height:
        second_hold_y = randint(first_hold_y + 30, first_hold_y + 50)
        second_hold_y = wall_height - second_hold_y
        second_hold[1] = second_hold_y


print(f"Second Hold Coordinates : {second_hold}")

cv2.circle(wall_img, tuple(second_hold), 4, (0, 0, 255), -1)
text = f"Second Hold : ({second_hold_x}, {second_hold_y})"
cv2.putText(wall_img, text, (second_hold[0] + 5, second_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

third_hold_x = randint(second_hold_x - 50, second_hold_x + 50)

third_hold_y = randint(second_hold_y + 30, second_hold_y + 50)

third_hold_y = wall_height - third_hold_y

third_hold = [third_hold_x, third_hold_y]

distance_between_first_and_third = euclidean(np.array(first_hold), np.array(third_hold))
distance_between_second_and_third = euclidean(np.array(second_hold), np.array(third_hold))

while distance_between_first_and_third < distance_between_second_and_third:
    # distance_between_first_and_third = euclidean(np.array(first_hold), np.array(third_hold))
    # distance_between_second_and_third = euclidean(np.array(second_hold), np.array(third_hold))
    # if distance_between_first_and_third < distance_between_second_and_third:
    third_hold_x = randint(second_hold_x - 50, second_hold_x + 50)
    third_hold_y = randint(second_hold_y + 30, second_hold_y + 50)
    third_hold_y = wall_height - third_hold_y
    third_hold = [third_hold_x, third_hold_y]
    distance_between_first_and_third = euclidean(np.array(first_hold), np.array(third_hold))
    distance_between_second_and_third = euclidean(np.array(second_hold), np.array(third_hold))
    # elif distance_between_first_and_third > distance_between_second_and_third:
    #     break

""" while True:
    if (third_hold_x >= 0 and third_hold_x <= wall_width) and (third_hold_y >= 0 and third_hold_y <= wall_height):
       break
    if third_hold_x < 0 or third_hold_x > wall_width:
        third_hold_x = randint(second_hold_x - 50, second_hold_x + 50)
        third_hold[0] = third_hold_x
    if third_hold_y < 0 or third_hold_y > wall_height:
        third_hold_y = randint(second_hold_y + 30, second_hold_y + 50)
        third_hold_y = wall_height - third_hold_y
        third_hold[1] = third_hold_y """
    
print(f"Third Hold Coordinates : {third_hold}")

print(f"The distance between first & third hold is {distance_between_first_and_third}")

print(f"The distance between second & third hold is {distance_between_second_and_third}")

cv2.circle(wall_img, tuple(third_hold), 4, (0, 0, 255), -1)
text = f"Third Hold : ({third_hold_x}, {third_hold_y})"
cv2.putText(wall_img, text, (third_hold[0] + 5, third_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

fourth_hold_x = randint(third_hold_x - 50, third_hold_x + 50)

# print(f"X coord of fourth hold : {fourth_hold_x}")

fourth_hold_y = randint(third_hold_y + 30, third_hold_y + 50)

fourth_hold_y = wall_height - fourth_hold_y

# print(f"Y coord of fourth hold : {fourth_hold_y}")

fourth_hold = [fourth_hold_x, fourth_hold_y]

while True:
    if (fourth_hold_x >= 0 and fourth_hold_x <= wall_width) and (fourth_hold_y >= 0 and fourth_hold_y <= wall_height):
       break
    if fourth_hold_x < 0 or fourth_hold_x > wall_width:
        fourth_hold_x = randint(third_hold_x - 50, third_hold_x + 50)
        fourth_hold[0] = fourth_hold_x
    if fourth_hold_y < 0 or fourth_hold_y > wall_height:
        fourth_hold_y = randint(third_hold_y + 30, third_hold_y + 50)
        fourth_hold_y = wall_height - fourth_hold_y
        fourth_hold[1] = fourth_hold_y

while True:
    distance_between_third_and_fourth = euclidean(np.array(third_hold), np.array(fourth_hold))
    distance_between_second_and_fourth = euclidean(np.array(second_hold), np.array(fourth_hold))
    if distance_between_second_and_fourth < distance_between_third_and_fourth:
        fourth_hold_x = randint(third_hold_x - 50, third_hold_x + 50)
        fourth_hold_y = randint(third_hold_y + 30, third_hold_y + 50)
        fourth_hold_y = wall_height - fourth_hold_y
        fourth_hold = [fourth_hold_x, fourth_hold_y]
    elif distance_between_second_and_fourth > distance_between_third_and_fourth:
        break

print(f"fourth Hold Coordinates : {fourth_hold}")

print(f"The distance between third & fourth hold is {distance_between_third_and_fourth}")

print(f"The distance between second & fourth hold is {distance_between_second_and_fourth}")

cv2.circle(wall_img, tuple(fourth_hold), 4, (0, 0, 255), -1)
text = f"Fourth Hold : ({fourth_hold_x}, {fourth_hold_y})"
cv2.putText(wall_img, text, (fourth_hold[0] + 5, fourth_hold[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1, cv2.LINE_AA)

cv2.imshow("RouteKraft", wall_img)

k = cv2.waitKey(0)

if k == ord('q'):
    cv2.destroyAllWindows()



