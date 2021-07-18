from collections import deque, OrderedDict

#

my_dq = deque([1, 2, 3], 3)

my_dq.append(4)

print(my_dq)
my_dq.appendleft(0)

print(my_dq)

# ordered dict

dict_1 = {1: '1', 2: '2', 3: '3'}
dict_1[0] = "0"
print(dict_1)

dict_2 = OrderedDict({1: '1', 2: '2', 3: '3'})
dict_2[0] = '0'
print(dict_2)
print(dict_2.popitem(last=True))
dict_2.move_to_end(2)
print(dict_2)
