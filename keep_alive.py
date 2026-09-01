import time
import random
import pyautogui as pag

pag.FAILSAFE = True

try:
    while True:
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pag.moveTo(x, y, 3)

        for _ in range(20):
            pag.moveRel(0,0)
            time.sleep(0.5)

except KeyboardInterrupt:
    print("Script stopped by user - keyboard interrupt.")

except pag.FailSafeException:
    print("Script stopped by user - failsafe triggered.")
  