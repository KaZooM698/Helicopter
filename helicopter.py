from utils import randcell

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.h = h
        self.w = w
        self.x = rx
        self.y = ry

    def move(self, dx, dy):
        nx, ny = dx + self.x, dx + self.y      
        if (nx >= 0 and ny >=0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny