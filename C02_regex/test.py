import os
print(os.getcwd().rsplit('\\')[0])
print(os.listdir(os.getcwd().rsplit('\\', maxsplit=1)[0]))



import os

# Getting all memory using os.popen()
x = os.popen('wmic cpu get caption, deviceid, name, numberofcores, maxclockspeed, status')
y = os.popen('wmic cpu get loadpercentage')
z = os.popen('notepad.exe')
# Memory usage
print(y.readlines())

# import psutils
#
# psutil.cpu_percent()
# psutil.virtual_memory()
