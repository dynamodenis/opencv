import cv2

img = cv2.imread('comps.png', 0)

cv2.imshow('images',img)

k=cv2.waitKey(0) & 0xFF
# conditional to estroy window without saving image
if k== 27:
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('comps_copy.png',img)
    cv2.destroyAllWindows()