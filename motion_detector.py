import cv2, time
first_frame = None
video = cv2.VideoCapture(0)
#The number 0 above can be changed to 1, 2 etc if there are multiple cameras connected to the PC. Changing the number would change the input device

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        #We want to ignore any motion less than 1000 pixels(100*10, 32*32 etc), as they are too small in this instance
        #This number is purely based on taste, and could be different for a security camera, for example; as this has a much higher range and moving objects would be much smaller.  
        
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3) #The colour could be changed by altering the values in the 3*1 BGR tuple. I chose blue here.
        #draws bounding square/rectangle around moving object 

    cv2.imshow("Grey Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Colour Frame", frame)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
