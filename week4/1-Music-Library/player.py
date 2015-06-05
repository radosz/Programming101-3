from subprocess import *


def play(mp3Path):
    p = Popen(["mpg123", "-vC", mp3Path], stdin=PIPE,
              stdout=DEVNULL, stderr=STDOUT)
    return p


def stop(process):
    process.kill()
