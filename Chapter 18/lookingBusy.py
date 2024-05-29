import pyautogui, time

print('Active, press Ctrl-C to quit.')

try:
    while True:
        pyautogui.moveRel(1, 0)
        time.sleep(10)
        pyautogui.moveRel(-1, 0)
        time.sleep(10)
except KeyboardInterrupt:
    print('Done')