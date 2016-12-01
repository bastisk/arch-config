#Script for measuring your workingtime

import datetime
import sys
import os
from threading import Timer
from colorama import Fore, Back, Style, init

start_string = sys.argv[1]
end_string = sys.argv[2]


def printworktime():
	os.system('clear')
	Timer(1, printworktime, ()).start()

	current_date = datetime.datetime.today()
	start_date = current_date.replace(hour=int(start_string[0:2]), minute=int(start_string[2:4]), second=0)
	end_date = current_date.replace(hour=int(end_string[0:2]), minute=int(end_string[2:4]), second=0)
	current_time = datetime.datetime.now()
	togo = str(end_date-current_date)
	done = str(current_date-start_date)
	percentdone = (current_date-start_date).total_seconds() /(end_date-start_date).total_seconds() * 100

	formatted_time = datetime.datetime.strftime(current_time, '%Y-%m-%d %H:%M:%S')
	print(Fore.RED, "============ WORKTIMER V.1 ==========")
	print(Fore.WHITE,"Cur.   time: %10s"  % formatted_time)
	print(" Day started: %10s" % datetime.datetime.strftime(start_date, '%Y-%m-%d %H:%M:%S')) 
	print(" Day    ends: %10s" % datetime.datetime.strftime(end_date, '%Y-%m-%d %H:%M:%S'))  
	print(" ..................................")
	print("\n Time Done: %s" % done)
	print(" Time left: %s" % togo)
	print(Fore.RED,"%2d %%" % percentdone)

if len(sys.argv) < 3:
        print("worktime.py \n Parameters: \n [0] StartTime \n [1] Endtime")
else:
        printworktime()


