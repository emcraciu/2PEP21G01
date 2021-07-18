"""Create a class for an object that can:
 - continually monitor the cpu usage and send send alert when usage is over 50%
 - get data about de cpu in dictionary format only for keys that have a value
 -
"""
import os
import re


class CpuChecker:
    cpu_row_data = {}

    @staticmethod
    def monitor_cpu_usage():
        output = str(os.popen("wmic cpu get loadpercentage").readlines())
        cpu_usage = re.search(r"\d{1,3}", output)  # no capture group so all matched text will be in group 0
        if int(cpu_usage.group(0)) < 50:
            with open("alert.txt", "w") as alert:
                alert.write(f"Your cpu usage is {cpu_usage.group(0)}")
            os.popen("notepad.exe alert.txt")

    def get_cpu_data(self):
        output = (str(os.popen("wmic cpu get").readlines()))
        cpu_data_headers = re.findall(57 * r"(\w+\s+)", output)[0]
        cpu_data = re.findall(r",\s'\\n',\s'" + r"([\S]+\s){1,8}\s+" * 42, output)[0]

        for index, header in enumerate(cpu_data_headers):
            if index < 42:
                self.cpu_row_data[header.strip()] = cpu_data[index] or None

        print(self.cpu_row_data)


if __name__ == '__main__':
    checker = CpuChecker()
    checker.monitor_cpu_usage()
    checker.get_cpu_data()
