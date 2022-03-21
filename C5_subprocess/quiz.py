import subprocess
#print(subprocess.run(['dir'], shell=False, text=True, capture_output=True))


ping_var = subprocess.Popen(['ping', '8.8.4.4'])
stdout, stderr = ping_var.communicate(timeout=1)


"https://www.classmarker.com/a/tests/test/?test_id=1798649&trk=edittest_settingsresults"