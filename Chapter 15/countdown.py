# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft -= 1

# At the end of the countdown, play the sound file.
subprocess.Popen(['start', 'alarm.wav'], shell=True)