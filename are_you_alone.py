# Detects if there is another person within the map
while maple.running:
	if maple.GetPeopleCount() != 6:
		print "There's someone in the map!!"
