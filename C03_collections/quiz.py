from collections import UserString, deque, Counter

#
# class MyStr(UserString):
#
#     def __add__(self, other):
#         result = []
#         counter = 0
#         for i in self:
#             result.append(str(other[counter]))
#             counter += 1
#
#         return MyStr('').join(result)
#
#
# a = MyStr('text1')
# b = MyStr('text')
# print(b + a)

#
# class Test:
#     q = deque(maxlen=2)
#
#     def __add__(self, other):
#         self.q.append(other)
#         return self
#
#
# t = Test()
#
# x = t + 1
# y = t + 2
# z = t + 3
# print(z.q.popleft())


from collections import OrderedDict


class Test(Counter):

    def __sub__(self, other):
        for key, value in other.items():
            self[key] -= value


t1 = Test('abbccc')
t2 = Test('abc')
print(t1 - t2)
