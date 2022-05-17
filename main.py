import numpy as np
import cv2 as cv

path = 'example.jpg'
img = cv.imread(path)
pointList = []

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),5,(155,0,0),-1)
        pointList.append([x,y])
        numPoints = len(pointList)
        if numPoints % 3 == 0 and numPoints > 0:
            calculateAngle(pointList)
        if numPoints % 3 != 1 and numPoints > 0:
            cv.line(img,tuple(pointList[-2]),(x,y),(0,0,255),2)

def calculateAngle(pointList):
    pt1, pt2, pt3 = np.array(pointList[-3:])
    a1 = np.arctan2(-(pt1[1]-pt2[1]),(pt1[0]-pt2[0]))
    a2 = np.arctan2(-(pt3[1]-pt2[1]),(pt3[0]-pt2[0]))
    angle = round((np.abs(a1 - a2)) * 180 / np.pi,1)
    cv.putText(img, str(angle), (pt2[0] + 20, pt2[1] + 30), cv.FONT_HERSHEY_COMPLEX,
                1, (0, 0, 255), 2)
    print(angle)

# Create a black image, a window and bind the function to window
cv.namedWindow('image')

cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(1) & 0xFF == ord('r'):
        pointList = []
        img = cv.imread(path)
    elif cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()