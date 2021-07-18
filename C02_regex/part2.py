import os

output = str(os.popen('wmic cpu get loadpercentage').readlines())
print(output)
