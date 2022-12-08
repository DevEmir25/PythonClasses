import pyautogui

screenWidth, screenHeight = pyautogui.size()
print("Screen Resolution = ",screenWidth,screenHeight)

# Mouse Location
currentMouseX, currentMouse = pyautogui.position()