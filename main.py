import cv2
import numpy as np
def nothing(x):
    pass
cv2.namedWindow("Tracking")
cv2.createTrackbar("Lh","Tracking",0,255,nothing)
cv2.createTrackbar("Ls","Tracking",0,255,nothing)
cv2.createTrackbar("Lv","Tracking",0,255,nothing)
cv2.createTrackbar("Hh","Tracking",255,255,nothing)
cv2.createTrackbar("Hs","Tracking",255,255,nothing)
cv2.createTrackbar("Hv","Tracking",255,255,nothing)

while True:
    frame=cv2.imread("smarties.png")
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos("Lh","Tracking")
    l_s = cv2.getTrackbarPos("Ls", "Tracking")
    l_v = cv2.getTrackbarPos("Lv", "Tracking")
    h_h = cv2.getTrackbarPos("Hh", "Tracking")
    h_s = cv2.getTrackbarPos("Hs", "Tracking")
    h_v = cv2.getTrackbarPos("Hv", "Tracking")

    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([h_h,h_s,h_v])

    mask=cv2.inRange(frame,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('image',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)

    k=cv2.waitKey(0)
    if k==ord('q'):
        break
cv2.destroyAllWindows()




