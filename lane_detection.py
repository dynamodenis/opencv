import matplotlib.pylab as plt
import cv2
import numpy as np

image = cv2.imread('roads.jpeg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

# region of interest
region_of_interest_vertices = [
    # width and height
    (0,height),
    (width/2, height/2),
    (width,height),
]
# create a function
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, vertices,match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image
# draw the lines

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0],img.shape[1],3), dtype=np.uint8)
    
    # loop through the lines
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image,(x1,y1),(x2,y2), ( 0,255,0), thickness=3)
            
    # merge the blank_imge to the img
    img = cv2.addWeighted(img, 0.8,blank_image,1,0.0)
    return img
    
# turn image to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
canny_image = cv2.Canny(gray_image,100,200)

# call the function
cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

# draw lines
lines = cv2.HoughLinesP(cropped_image,
                        rho=6,
                        theta=np.pi/60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=25)
# call the draw the lines method
image_with_lines= draw_the_lines(image,lines)
plt.imshow(image_with_lines)
plt.show()