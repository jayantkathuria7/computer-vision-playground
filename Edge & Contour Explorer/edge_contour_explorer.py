import cv2 as cv
import numpy as np

def auto_canny(gray):
    median = np.median(gray)
    lower = int(max(0,0.67 * median))
    upper = int(min(255,1.33 * median))
    return lower, upper

def manual_canny(blur):
    def nothing(x):
        pass

    cv.namedWindow('Canny Paramters Tuning')

    cv.createTrackbar('lower', 'Canny Paramters Tuning', 0, 255, nothing)
    cv.createTrackbar('upper', 'Canny Paramters Tuning', 0, 255, nothing)

    while True:
        lower = cv.getTrackbarPos('lower', 'Canny Paramters Tuning')
        upper = cv.getTrackbarPos('upper', 'Canny Paramters Tuning')

        canny = cv.Canny(blur, lower, upper)

        kernel = np.ones((3,3), np.uint8)
        canny = cv.dilate(canny, kernel, iterations=1)

        cv.imshow('Canny Parameter Tuning',canny)

        key = cv.waitKey(1) & 0xFF

        if key==ord('s'):
            break
    return lower, upper

img = cv.imread('Edge & Contour Explorer/sample_images/sample2.jpg')
assert img is not None, "Image Path doesn't exist"
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Original Image',img)
blur = cv.GaussianBlur(gray, (5,5), 0)
canny_img = False
while True:
    key = cv.waitKey(1) & 0xFF 
    if key==ord('q'):
        break
    elif key==ord('o'):
        cv.imshow('Output',img)
    elif key==ord('e'):
        lower, upper = auto_canny(blur)
        canny = cv.Canny(blur, lower, upper)
        kernel = np.ones((3,3), np.uint8)
        canny = cv.dilate(canny, kernel, iterations=1)
        canny_img = True
        cv.imshow('Output',canny)
    elif key==ord('c') and canny_img:
        contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        contour_img = img.copy()
        areas = [cv.contourArea(c) for c in contours]
        threshold = np.percentile(areas,10)
        count = 0
        for i, contour in enumerate(contours):
            area = cv.contourArea(contour)
            parent = hierarchy[0][i][3]
            if area>threshold and parent == -1:
                count+=1
                cv.drawContours(contour_img, [contour], -1, (0,0,255), 3)
                x, y, w, h = cv.boundingRect(contour)
                cv.rectangle(contour_img, (x,y), (x+w,y+h), (255,0,0),2)
        h, w = contour_img.shape[:2]
        font_scale = w / 1000
        thickness = int(w/500)
        text = f"Total {count} items"
        (font_w, font_h), baseline = cv.getTextSize(text, cv.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
        cv.putText(contour_img, text, (20,20), cv.FONT_HERSHEY_SIMPLEX, font_scale,(0,0,0), thickness)
        cv.imshow('Output',contour_img)
cv.imwrite("Edge & Contour Explorer/output_images/output2.jpg",contour_img)
cv.waitKey(0)
cv.destroyAllWindows()