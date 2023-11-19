import pyautogui as pt
import time

limit = int(input("Say: "))
message = input("message: ")
interval = float(input("Enter the interval between messages in seconds: "))
time.sleep(5)

i = 0

while i < limit:
    pt.write(message)
    pt.press("enter")
    i = i + 1
    print(i)

    time.sleep(interval)
