import threading
ilock = threading.Lock()
ilock.acquire()
out = None

def rask(message='', parent=None, default_value=''):
	global out
	dlg = wx.TextEntryDialog(parent, message, defaultValue=default_value)
	dlg.ShowModal()
	out = dlg.GetValue()
	dlg.Destroy()
	while not ilock.locked():
		pass
	ilock.release()

def ask(message=''):
	wx.CallAfter(rask, message)
	ilock.acquire()
	maple.log(message, out)
	return str(out)

maple.SetAutoLogin(ask("Email"), ask("Password"), int(ask("World number (Scania = 0)")), int(ask("Channel number (channel 1 = 0)")), int(ask("Character number (first character = 0)")), ask("PIC"))

maple.WaitUntilStop()
