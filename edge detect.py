from helper_functions import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#-----------------------FILL IN THE FOLDER WHERE YOUR IMAGE EXISTS--------------------------
datafolder = r"images/"
imgpath = datafolder + "6.jpg" 
#implemented 1
#----------------------------------------STARTER CODE----------------------------------------
# Convert the color image to grayscale and returns the grayscale pixels 
pixel_val = read_colorimg(imgpath)
#implemented 2
# The returned pixel values INCLUDE 2 boundary rows and 2 boundary colns. Therefore,
rows = len(pixel_val) - 2
colm = len(pixel_val[0]) - 2
#
#--------------------------------------START OF THE CODE----------------------------------------
# Create a data structure to store updated pixel information
#temp = [0] * colm
#new_pixel_val = [temp] * rows
# implemented 3
new_pixel_val=[[0]* colm for x_line in range(rows)]
#Here x_line is horizontal axis

# Define the 3 x 3 mask as a tuple of tuples
#implemented 4. Mask 1
mask = ((-1,0,1), (-2,0,2), (-1,0,1))

# Implement a function to slice a part from the image as a 2D list
def get_slice_2d_list(img,x_line,y_line):
    #implemented 5a
    return [r[y_line - 1 : y_line+2] for r in img[x_line -1 : x_line +2]]
#here y_line is vertical axis

# Implement a function to flatten a 2D list or a 2D tuple
def flatten(f):
    return [m for n in f for m in n]
#implemented 5b
# For each of the pixel values, excluding the boundary values
    # Create little local 3x3 box using list slicing
for x_line in range(0,rows+1):
    for y_line in range(0,colm+1):
        neighbour_pixels = get_slice_2d_list(pixel_val,x_line,y_line)
        pixels1D=flatten(neighbour_pixels)
    #here the pixels are converted from 2 dimension to 1 dimension
    # Apply the mask

        mask1D=flatten(mask)
        final = list(map(lambda x_line,y_line: x_line*y_line,pixels1D,mask1D))
        #implemented 5c
        
    # Sum all the multiplied values and set the new pixel value
        outline=sum(final)
        new_pixel_val[x_line-1][y_line-1]=outline
        #implemented 5e
#----------------------------------------CODE ENDED----------------------------------------
#implemented 6
# Verify your result
verify_result(pixel_val, new_pixel_val, mask)

#implemented 7
# View the original image and the edges of the image
view_images(imgpath, new_pixel_val)