# Calculate experience points and estimate next amount of hours to get to level up
import time
otime = time.time()
texp = 1e-11
oexp = maple.GetCharEXP()
while maple.running:
	exp = maple.GetCharEXP()
	if exp > oexp:
		texp += exp - oexp
	oexp = exp
	dt = time.time()-otime
	maple.log("%EXP/s is "+str(texp/dt)+", "+str(dt/texp*100/60/60)+" hours to get 100%")
