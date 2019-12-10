import cv2
cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cascade_eye=cv2.CascadeClassifier('haarcascade_eye.xml')
def detect(gray,frame):
    faces=cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=cascade_eye.detectMultiScale(roi_gray,1.3,20) #If I replace gray with roi_gray then it will be faster but cant detect image for side view
        for (x1,y1,w1,h1) in eyes:
            cv2.rectangle(roi_color,(x1,y1),(x1+w1,y1+h1),(5,150,150),2)
    return frame
video_capture=cv2.VideoCapture(0) #If you are using external webcam change 0 to 1
while True:
    _,frame=video_capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas=detect(gray,frame)
    cv2.imshow('Video',canvas)
    if cv2.waitKey(1) and 0xFF ==ord('a'):
        break
video_capture.release()
cv2.destroyAllWindows()
        
