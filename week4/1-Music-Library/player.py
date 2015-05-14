from subprocess import *


def play(mp3Path):
    p = Popen(["mpg123", "-vC", mp3Path], stdin=PIPE,
              stdout=DEVNULL, stderr=STDOUT)
    return p


def stop(process):
    process.kill()

# p  = play("/home/rado_sz/Programming101-3/probni/Metalica - Nithing Else Metters.mp3")
