import sys, time
import donrobot, telerobot

TOKEN = sys.argv[1] 

DonRobot = donrobot.Donrobot()
telerobot.Telerobot(TOKEN,DonRobot)

while 1:
    time.sleep(10)
