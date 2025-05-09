import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Cannot access webcam. Check the index or if another app is using the camera.")
    exit()

while True:
    ret, frame = video.read()
    if not ret:
        print("Failed to read frame from webcam.")
        break

    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow('Object Detection', output_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()