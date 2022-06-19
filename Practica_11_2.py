import cv2
cap = cv2.VideoCapture('videoplayback_Trim.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    if ret == False: break
    fgmask = fgbg.apply(frame)
    
    cv2.imshow('fgmask',fgmask)
    cv2.imshow('frame',frame)
    
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
