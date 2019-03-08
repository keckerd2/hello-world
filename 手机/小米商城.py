import os
import time

while True:
    # click(970,1050)
    os.system('adb -s 9bd545f0 shell input tap 970 1050')
    #小米5
    # os.system('adb -s dcf372d0 shell input tap 540 1530')
    time.sleep(0.1)
