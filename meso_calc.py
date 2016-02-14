# Calculate the number of mesos (in-game currency) made
import time
otime = time.time()
tmesos = 1
omesos = maple.GetMesos()
while maple.running:
	mesos = maple.GetMesos()
	if mesos > omesos:
		tmesos += mesos - omesos
	omesos = mesos
	dt = time.time()-otime
	mh = tmesos/dt*60*60
	maple.log("Mesos/h is {:,}, {:,} hours for 1bn".format(int(mh), float(1000000000/mh)))
