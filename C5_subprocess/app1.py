"""
* get IP address from OS
"""
import os
import re
import time
import subprocess


class Utils:

    def get_ip_adress(self):
        result = subprocess.Popen(['ipconfig'], text=True, stdout=subprocess.PIPE)
        output = result.communicate()[0]
        matches = re.finditer(r'(Ethernet|Wireless)(\s\w+)+', output)
        interfaces = []
        for match in matches:
            interfaces.append(match.group())
        ip_matches = re.finditer(r"disconnected|(?<=(Address. . . . . . . . . . . : ))(\d+\.)+\d+", output)
        ip_addresses = []
        for ip_match in ip_matches:
            ip_addresses.append(ip_match.group())
        dict = {interfaces[i]: ip_addresses[i] for i in range(len(interfaces))}
        return dict

    def connect_ssh(self, ip: str):
        ssh = subprocess.Popen(['ssh', '-T',  ip], shell=True)
        stdout, stderr = ssh.communicate(input=b'ls')

    def allow_user_to_enter_message(self):
        notepad = subprocess.Popen(['notepad.exe', 'file.txt'])
        time.sleep(10)
        stdout, stderr = notepad.communicate(input=b'yes')
        notepad.terminate()

    def ping(self, ip_address):
        ping_var = subprocess.Popen(['ping', ip_address], stderr=subprocess.PIPE)
        try:
            stdout, stderr = ping_var.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            subprocess.T
            ping_var.send_signal(9)
            stdout, stderr = ping_var.communicate()
        print(stderr)

    def search_for_erors(self, level='ERROR', path=''):
        if os.path.isfile(path):
            cat = subprocess.Popen(['cat', path], stdout=subprocess.PIPE)
            grep = subprocess.Popen(['grep', level], stdin=cat.stdout, stdout=subprocess.PIPE)
            cat.stdout.close()
            output = grep.communicate()[0]
        if os.path.isdir(path):
            output = run(['dir'], shell=True, text=True, capture_output=True, cwd=path)
            files = output.stdout
            output2 = re.search(files, r"\d+\/\d+\/\d+\s+\d+:\d+\s\w+\s+(\d+,?){0,5}\s(?P<file>.*)")
            print(output2)
            cat = Popen(['cat', '/var/log/wifi.log'], stdout=subprocess.PIPE)
            grep = Popen(['grep', level], stdin=cat.stdout, stdout=subprocess.PIPE)
            cat.stdout.close()
            output = grep.communicate()[0]
            print(output)
