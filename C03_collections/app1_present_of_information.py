"""Create a string like object that is capable of determining if information is transmitted in a sample of test provided
  - method will return true if there is al least 20% deviation from average"""

from collections import UserString, Counter


class InformationGetter(UserString):

    def information(self):
        my_data = Counter(self.split())
        for key in my_data.keys():
            if len(key) <= 3:
                my_data[key] -= my_data[key]
        print(my_data)


if __name__ == '__main__':
    with open("data.txt") as f:
        file_data = f.read()
    getter = InformationGetter(file_data)
    getter.information()
