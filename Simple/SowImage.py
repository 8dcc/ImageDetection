#
# Based on https://github.com/ClarityCoders/ComputerVision-OpenCV
# Based on https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html
# Tested on windows

import cv2, os, numpy

#-------------------------------------------------------------------------------
# Variables
path_separator = "\\"
# Get the script path in case you execute it from another path
script_path = "/".join(os.path.realpath(__file__).split(path_separator)[:-1])
image_path = "/../Images/003.jpg"  # Relative
show_resized = False  # If you want to skip steps
# ------------------------------------------------------------------------------

# Define a function for closing the windows on a user input
def wait_user_key():
    key = cv2.waitKey(0)
    print(f"User pressed key: {chr(key)}")
    cv2.destroyAllWindows()

# Read the image from the file
img = cv2.imread(f"{script_path}{image_path}")

# Check that the image exists
if img is None:
    exit("The file type is None. Check the path...")

#...............................................................................

# Big picture
print()
print(f"Printing original image with shape: {img.shape}")
cv2.imshow("Original", img)
wait_user_key()

if show_resized:
    # Resize the picture to half
    small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    print()
    print(f"Printing small image with shape: {small.shape}")
    cv2.imshow("Small!", small)
    wait_user_key()

    # Resize the picture to x2
    big = cv2.resize(img, (0,0), fx=2, fy=2)
    print()
    print(f"Printing big image with shape: {big.shape}")
    cv2.imshow("Big!", big)
    wait_user_key()

#...............................................................................
# https://gist.github.com/r4v10l1/86a7904fabe11695b7f326654e2c555b

# Drawing lines
img4lines = cv2.imread(f"{script_path}{image_path}")  # Clean image
cv2.line(img4lines,(200,200),(611,511),(10,10,255),3)  # StartPos, EndPos, Color in BGR, Thickness
cv2.line(img4lines,(500,100),(200,550),(10,10,255),3)  # StartPos, EndPos, Color in BGR, Thickness
print()
print("Printing original image with diagonal line...")
cv2.imshow("Original with line", img4lines)
wait_user_key()

# Drawing a rectangle (Cool kids call it CatESP)
img4esp = cv2.imread(f"{script_path}{image_path}")
cv2.rectangle(img4esp,(19,22),(576,579),(0,255,0),2)
# Drawing text
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img4esp,'CatHooks v1',(250,18), font, 0.5,(20,20,20),1,cv2.LINE_AA)

# I was too lazy so I resized the final result, you can add the rectangles
# and the text to the resized image for a better result.
img4esp_res = cv2.resize(img4esp, (0,0), fx=1.3, fy=1.3)

print()
print("Printing original image with rectangle...")
cv2.imshow("Original with rectangle", img4esp_res)
wait_user_key()

#...............................................................................

exit("")  # Epic enter line
