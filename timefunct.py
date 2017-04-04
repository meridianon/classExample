from tkinter import *
import Characters_klass as ck
import time,datetime
# Timer Start
i = 0
mas = []
def start():
	return 20
def timer():
	k = 0
	i = 0
	while 1:
		if k == 10:
			break
		else:
			time.sleep(0.5)
			k += 1
			return start()