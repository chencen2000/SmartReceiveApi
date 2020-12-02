import win32api
import win32event

evt = win32event.CreateEvent(None, False, False, "test")
win32event.SetEvent(evt)
win32api.CloseHandle(evt)