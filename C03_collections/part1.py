from collections import UserString, Counter


class MyStr(UserString):

    def my_method(self, text):
        if text in self:
            print('text is there')


my_str = MyStr('initial string')
print(my_str)

my_str.my_method('str')
print(my_str.data)

my_text = 'the fox is in the tree'

counter = Counter()

for word in my_text.split():
    counter[word] += 1

my_new_text = 'there is no fox in the'

for word in my_new_text.split():
    counter[word] -= 1

print(counter)

# information

x = 1, 2, 3
y0 = 1, 2, 3, 1, 2, 3
y1 = 4, 2, 5, 4, 2, 5
