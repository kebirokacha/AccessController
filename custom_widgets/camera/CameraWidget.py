import time

import cv2 as cv
import face_recognition
from PySide6.QtCore import QThread, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import  QWidget
from .Camera_ui import Ui_Camera
from databasemanager import DataBaseManager

class CameraWidget(Ui_Camera ,QWidget):

    def __init__(self):
        super(CameraWidget, self).__init__()
        self.setupUi(self)
        self.th = Thread(self)
        self.th.update_frame.connect(self.setImage)
        self.th.start()

    def closeEvent(self, event):
        self.killThread()
        event.accept()

    

    @Slot()
    def setImage(self, image):
        self.cameraLabel_01.setPixmap(QPixmap.fromImage(image))

    @Slot()
    def killThread(self):

        self.th.status = False  # Set the status flag to stop the thread
        self.th.quit()
        self.th.wait()  # Wait for the thread to finish
        self.th = None


class Thread(QThread):
    update_frame = Signal(QImage)

    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.status = True
        database_manager = DataBaseManager()
        self.known_embeddings = database_manager.getEncodingArray()
        self.names = database_manager.getPersonNames()
        self.capture = cv.VideoCapture(0)
        self.capture.set(cv.CAP_PROP_FPS ,30)
        self.counter = 0
        self.skip_frames = 5  # skip each 5 frame

        self.frame_counter = 0
        self.start_time = time.time()

        self.last_recognition_time = time.time()
    def run(self):
        while self.status:
            ret, frame = self.capture.read()
            if not ret:
                continue
            self.counter += 1

            # Calculate the elapsed time since the last face recognition
            elapsed_time = time.time() - self.last_recognition_time
            # Increment the frame counter
            self.frame_counter += 1

            # Calculate FPS
            if time.time() - self.start_time >= 1:
                fps = self.frame_counter / (time.time() - self.start_time)
                print(f"FPS: {fps:.2f}")
                self.frame_counter = 0
                self.start_time = time.time()

            if elapsed_time >= .5:
                # Update the last recognition time to the current time
                self.last_recognition_time = time.time()
                small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
                # Locate all faces in the frame
                faces = face_recognition.face_locations(small_frame )
                for face in faces:
                    # x, y, w, h = face # use the face tuple directly
                    top, right, bottom, left = [x * 4 for x in face]  # use the same format as face_recognition 
                    # top, right, bottom, left = face   
                    # Use face_recognition to get the face encoding
                    unknown_encoding = face_recognition.face_encodings(frame, [(top, right, bottom, left)])[0]
                    # Compare the unknown embedding with the known embeddings
                    matches = face_recognition.compare_faces(self.known_embeddings,
                                                            unknown_encoding)  # get a list of boolean values
                    # indicating matches
                    name = "Unknown"  # default name
                    if True in matches:  # if there is at least one match
                        match_index = matches.index(True)  # get the index of the first match
                        name = self.names[match_index]  # get the name from the names list
                    self.drawRectangle(frame, name, top, right, bottom, left)

            # Update the frame with no rectangle
            color_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            height, width, channel = color_frame.shape
            image = QImage(color_frame.data, width, height, QImage.Format_RGB888)
            self.update_frame.emit(image)

    def drawRectangle(self, frame, name, top, right, bottom, left):
        red, green = (0, 0, 255), (0, 255, 0)
        rectangle_color = green if name != "Unknown" else red

        # Draw a rectangle around the face
        cv.rectangle(frame, (left, top), (right, bottom), rectangle_color, 2)
