import pyautogui, time, os

pyautogui.PAUSE = 2

def new_chat():
    leftupX, leftupY, rightdownX, rightdownY = 989, 190, 1096, 220
    pyautogui.screenshot('new_chat.jpg', region=(leftupX, leftupY, 
                                                 rightdownX - leftupX, 
                                                 rightdownY - leftupY))


def no_results():
    chat_box = pyautogui.locateOnScreen('new_chat.jpg', confidence=0.5)
    chat_box_click = pyautogui.center(chat_box)
    pyautogui.click(chat_box_click)
    pyautogui.typewrite('gibberish')
    leftupX, leftupY, rightdownX, rightdownY = 1211, 252, 1304, 277
    pyautogui.screenshot('no_results.jpg', region=(leftupX, leftupY,
                                                   rightdownX - leftupX, 
                                                   rightdownY - leftupY))
    pyautogui.typewrite(['esc'])
    

def auto_message(user, message):
    print('Sleeping for 4 seconds')
    time.sleep(4)
    chat_box = pyautogui.locateOnScreen('new_chat.jpg', confidence=0.5)
    chat_box_click = pyautogui.center(chat_box)
    pyautogui.click(chat_box_click)

    pyautogui.typewrite(user[:-1])
    try:
        pyautogui.locateOnScreen('no_results.jpg', confidence=0.5)
        print('This person is not in your contacts.')
        pyautogui.typewrite(['esc'])
        return
    except pyautogui.ImageNotFoundException:
        pyautogui.typewrite(['\t'])
        pyautogui.typewrite(['\t'])
        pyautogui.typewrite(['enter'])
        pyautogui.typewrite(message)
        pyautogui.typewrite(['enter'])


if not os.path.exists('new_chat.jpg'):
    new_chat()
if not os.path.exists('no_results.jpg'):
    no_results()

users = ''
while users == '':
    print('Who do you want to message? (e.g. Alice, Blake, Laura)')
    users = input()
users = users.split(',')

message = ''
while message == '':
    print('What message do you want to send? Press enter to send.')
    message = input()

for user in users:
    user = user.strip()
    auto_message(user, message)

print('Done sending messages.')