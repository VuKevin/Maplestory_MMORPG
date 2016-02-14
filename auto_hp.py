# Auto heal Health Points 
while maple.running:
	if maple.GetCharHP() < 3000:
		maple.KeyPress(0x41)
	maple.Sleep(0.1)
