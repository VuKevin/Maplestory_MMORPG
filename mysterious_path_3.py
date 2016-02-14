import time

buffs = [[0x41, 90, 2, 0]]#[0x21, 80, 2, 0], [0x2E, 180, 2, 0], [0x23, 300, 2, 0], [0x22, 180, 2, 0]]

def buff():
	first = True
	for buff in buffs:
		cTime = time.time()
		if cTime > buff[3]:
			if first:
				first = False
				maple.Sleep(1)
			maple.KeyPress(buff[0])
			maple.Sleep(buff[2])
			buff[3] = cTime + buff[1]

def up():
	oy = maple.GetCharY()
	while maple.GetCharY() == oy and maple.running:
		maple.KeyPress(0x20)
		maple.Sleep(2)

s = True
while(maple.running):
	buff()
	maple.KeySpam(0x5A)
	if(s):
		maple.MoveX(1050)
	s = not s
	maple.MoveX(-50)
	up()
	maple.MoveX(285)
	maple.KeyPress(0x12)
	maple.Sleep(0.5)
	maple.KeyUp(0x5A)
	maple.FaceLeft()
	maple.KeyDown(0x11)
	maple.Sleep(5)
	maple.KeyUp(0x11)

	maple.KeySpam(0x5A)
	maple.MoveX(400)
	up()
	maple.MoveX(850)
	maple.FaceLeft()
	maple.KeyPress(0x12)
	maple.KeyUp(0x5A)
	maple.KeyDown(0x11)
	maple.Sleep(10)
	maple.KeyUp(0x11)
	maple.KeySpam(0x5A)
	maple.MoveX(1250)
	maple.KeyUp(0x5A)

	maple.KeySpam(0x5A)
	maple.MoveX(650)
	maple.Sleep(0.5)
	maple.KeyUp(0x5A)
	#maple.FaceLeft()
	maple.KeyDown(0x11)
	maple.Sleep(10)
	maple.KeyUp(0x11)
