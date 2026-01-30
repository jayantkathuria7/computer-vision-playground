import cv2 as cv
import sys

if len(sys.argv)<2:
    print("Error: Missing required 'filepath' argument.")
    print("Usage: python script.py <filepath>")
    sys.exit(1)
filepath = sys.argv[1]
original_image = cv.imread(filepath)
if original_image is None:
    print("Error: Image not found")
    exit()
img = original_image.copy()
print(img)
cv.putText(img,'r-->rotate image by 90 degree clockwise',(20,25),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,0))
cv.putText(img,'b->Apply Guassian Blur',(20,40),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,0))
cv.putText(img,'g-->Conert image to grayscale',(20,60),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,0))
cv.putText(img,'c-->Crop image',(20,80),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,0))
cv.putText(img,'e-->Perform Canny Edge Detection',(20,100),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,0))
cv.putText(img,'u-->Undo last change',(20,120),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,0))
cv.putText(img,'o-->Revert to original image',(20,140),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,0))
cv.putText(img,'s-->Save the modified image',(20,160),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,0))
cv.putText(img,'q-->Quit the playground',(20,180),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=0.8,color=(0,0,0))
cv.imshow('Image',img)
gray_check=''
last_copies = []
while True:
    change=0
    key = cv.waitKey(0) & 0xFF
    if key == ord('q'):
        break
    elif key==ord('r'): # rotate by 90degree clockwise
        img = cv.rotate(img,rotateCode=cv.ROTATE_90_CLOCKWISE)
        change=1
    elif key==ord('b'): #blur
        title='blured'
        img = cv.GaussianBlur(img,(5,5),10)
        change=1
    elif key==ord('g') and not gray_check: #grascale
        gray_check=True
        img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        change=1
    elif key==ord('c'):  #crop
        height, width = img.shape[:2]
        img = img[20:height-20, 20:width-20]
        change=1
    elif key==ord('e'): #canny edge detection
        if len(img.shape) == 3:
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        else:
            gray = img
        img = cv.Canny(gray, 150, 255)
        change=1
    elif key==ord('u') and last_copies: #undo
        img = last_copies[-1].copy()
        last_copies.pop()
    elif key==ord('o'): #revert to original
        img = original_image.copy()
    elif key==ord('s'): #save image
        cv.imwrite('modified.jpeg',img)
    if change:
        last_copies.append(img.copy())
    cv.imshow('modified.jpg',img)

cv.waitKey(0)
cv.destroyAllWindows()
