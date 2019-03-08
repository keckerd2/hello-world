import os
import time

def click_ok():
    os.system("adb shell input keyevent 23")
    # time.sleep(0.5)

def swipe_down(x1=200,y1=1200,x2=200,y2=600):
    os.system("adb shell input swipe "+str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2))
    # time.sleep(0.5)

def click_power():
    os.system("adb shell input keyevent 26")
    # time.sleep(0.5)

def click(x,y):
    # os.system(adb_path + "adb shell input tap "+str(x)+" "+str(y))
    os.system("adb shell input tap "+str(x)+" "+str(y))
    # time.sleep(0.5)

def click_home():
    os.system("adb shell input keyevent 3")
    # time.sleep(0.5)

#百度摇奖用的

# while True:
#     # click(540,1700)
#
#     #mix
#     os.system('adb -s 9bd545f0 shell input tap 540 1700')
#     #小米5
#     os.system('adb -s dcf372d0 shell input tap 540 1530')
#     time.sleep(0.5)


