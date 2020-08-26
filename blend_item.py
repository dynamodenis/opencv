import cv2
import numpy as np



# this diaplay an image
comp = cv2.imread('doha.jpg')
me = cv2.imread('me.jpg')

# this joins the two images together

join_image=np.hstack((comp[:,:256], me[:,256:]))

# The gausian pyramid for the comp
comp_copy = comp.copy()
comp_array = [comp_copy]

for i in range(6):
    comp_copy = cv2.pyrDown(comp_copy)
    comp_array.append(comp_copy)
    
# The gausian pyramid for the me
me_copy = me.copy()
me_array = [me_copy]

for i in range(6):
    me_copy = cv2.pyrDown(me_copy)
    me_array.append(me_copy)
    
# generate a laplasian pyramid for me   
me_copy = me_array[5]
lp_me = [me_copy]

for i in range(5,0,-1):
    gausian_expanded =cv2.pyrUp(me_array[i])
    laplasian = cv2.subtract(me_array[i-1], gausian_expanded)
    lp_me.append(laplasian)
    
# generate a laplasian pyramid for comp
comp_copy = comp_array[5]
lp_comp = [comp_copy]

for i in range(5,0,-1):
    gausian_expanded =cv2.pyrUp(comp_array[i])
    laplasian = cv2.subtract(comp_array[i-1], gausian_expanded)
    lp_comp.append(laplasian)
    
# Now add left and right halves of images in each level
comp_me_pyramid=[]
n=0

for comp_lap, me_lap in zip(comp_array,me_array):
    n+= 1
    cols,rows,ch = comp_lap.shape
    laplasian = np.hstack((comp_lap[:,0:int(cols/2)], me_lap[:,int(col/2):]))
    comp_me_pyramid.append(laplasian)
    
    
# new reconstruct
comp_me_reconstruct= comp_me_pyramid[0]
for i in range(1,6):
    comp_me_reconstruct = cv2.pyrUp(comp_me_reconstruct)
    comp_me_reconstruct = cv2.add(comp_me_pyramid[i], comp_me_reconstruct)

cv2.imshow('blened',comp_me_reconstruct)
# cv2.imshow('comp',comp)
# cv2.imshow('me',me)

    
cv2.waitKey(0)
cv2.destroyAllWindows()