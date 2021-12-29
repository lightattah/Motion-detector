import cv2
import pandas
from datetime import datetime

first_frame = None
video = cv2.VideoCapture(0)
status = None
status_list = [None, None]
entry_times = []
exit_times = []
df = pandas.DataFrame(columns=["Entry Time", "Exit Time"])
#The number 0 above can be changed to 1, 2 etc if there are multiple cameras connected to the PC. Changing the number would change the input device

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    # Converting first frame to grayscale and applying Gaussian Blur improves accuracy of the program

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:
        if cv2.contourArea(contour) < 5000:
            continue
        status = 1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)

    status_list.append(status)
    status_list = status_list[-2:]

    # Capturing the entry and exit times
    if status_list[-1] == 1 and status_list[-2] == 0:
        entry_times.append(datetime.now())

    elif status_list[-1] == 0 and status_list[-2] == 1:
        exit_times.append(datetime.now())

    cv2.imshow("Grey Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Colour Frame", frame)


    key = cv2.waitKey(1)

    if key == ord("q"):
        if status == 1:
            exit_times.append(datetime.now())
        break

print(status_list)
df["Entry Time"] = entry_times
df["Exit Time"] = exit_times

df.to_csv("Times.csv")

print(df)

video.release()
