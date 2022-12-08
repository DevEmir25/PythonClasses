import pyautogui

pyautogui.moveTo(799,466, duration=2,tween=pyautogui.easeInOutQuad)
pyautogui.click()
for i in range(100):
    pyautogui.write("Hello World", interval=0.01)
    pyautogui.press('enter')