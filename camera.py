import cv2

class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self, capture=None):
        ret, frame = self.video.read()
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()