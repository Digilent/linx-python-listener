import ctypes

myLib = ctypes.cdll.LoadLibrary('/usr/lib/liblinxdevice.so')

success = myLib.LinxOpen()

deviceNameLen = myLib.LinxGetDeviceNameLen()

testVar = " " * deviceNameLen

print myLib.LinxGetDeviceName(testVar)

print testVar

print myLib.LinxGetDeviceId()

myLib.LinxClose()