from subprocess import *


class Play:

    def __init__(self, path):
        self.mp3Path = path
        self.process = None

    def play(self):
        p = Popen(["mpg123", "-vC", self.mp3Path], stdin=PIPE,
                  stdout=PIPE, stderr=PIPE)
        self.process = p

    def stop(self):
        self.process.kill()
