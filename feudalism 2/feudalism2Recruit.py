import pyautogui as mouse
from pynput import keyboard
import winsound as sound

blockedState = True

def on_press(key):
    global blockedState
    if (key == keyboard.Key.caps_lock):
        blockedState = not blockedState
        if(blockedState == False):
            sound.Beep(5000, 200)
            sound.Beep(4000, 200)
            print("Activated")
        if (blockedState == True):
            sound.Beep(1000, 500)
            print("deactivated")
    if(blockedState == True):
        return
    if(key == keyboard.KeyCode.from_char('p')): #recruit
        currentPosition = mouse.position()
        mouse.dragTo(616,747,0.1)
        mouse.moveTo(currentPosition)
    if(key == keyboard.KeyCode.from_char('o')): #delete
        currentPosition = mouse.position()
        mouse.dragTo(823, 310, 0.1)
        mouse.moveTo(currentPosition)
    if(key == keyboard.KeyCode.from_char('i')): #buy item
        currentPosition = mouse.position()
        mouse.dragTo(655, 670, 0.1)
        mouse.moveTo(currentPosition)
    if (key == keyboard.KeyCode.from_char('c')):  #clic
        mouse.click()

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


if __name__ == '__main__':
    while(True):
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
