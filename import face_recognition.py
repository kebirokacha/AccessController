import cv2
import face_recognition
from ultralytics import YOLO
import threading

model = YOLO('resources/yolov8n-face.pt')
images = [
		cv2.imread('person_images/IMG_00000004.jpg') , 
		cv2.imread('person_images/IMG_00000007.jpg') ,
		cv2.imread('person_images/IMG_00000009.jpg') ,
		cv2.imread('person_images/IMG_00000011.jpg'),
		cv2.imread('person_images/IMG_000000011.jpg'),
		cv2.imread('person_images/IMG_00000005.jpg'),

	]
encoding = []

def faceProcess(fram):
	results = model.predict(fram ,verbose=False)
	for info in results:
		for box in info.boxes:
			x1, y1, x2, y2 = box.xyxy[0]
			x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
			matches = face_recognition.compare_faces(encoding ,face_recognition.face_encodings(fram ,[(y1, x2, y2 ,x1)])[0] )
			if True in matches:
				print('hello Mohamed')
			if False in matches:
				print('who are identify your self!')


for image in images:
	results = model.predict(image ,verbose=False)
	for info in results:
		for box in info.boxes:
			x1, y1, x2, y2 = box.xyxy[0]
			x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
			encoding.append(face_recognition.face_encodings(image ,[(y1, x2, y2 ,x1)])[0])

capture = cv2.VideoCapture(0)
while True:
	ret ,frame = capture.read()
	if ret:
		threading.Thread(target=faceProcess, args=(frame,)).start()
		cv2.imshow('camera' ,frame)
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
