import sys, time
import donrobot, telerobot, audioprocessor

TOKEN = sys.argv[1] 

voice = audioprocessor.Audioprocessor();
donRobot = donrobot.Donrobot(voice)
telerobot.Telerobot(TOKEN,donRobot)

while 1:
    time.sleep(10)
