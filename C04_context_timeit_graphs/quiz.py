# from contextlib import contextmanager
#
#
# @contextmanager
# def test(value):
#     try:
#         yield value.pop()
#     except Exception:
#         yield True
#     finally:
#         pass
#
#
# with test("test") as t:
#     print(t)
# import timeit
#
#
# def test():
#     print('testing...')
#
#
# for _ in range(10):
#     timeit.timeit(f"test()",
#                   setup=f'from __main__ import test',
#                   number=100)

import matplotlib.pyplot as plt
fig1, (a, b) = plt.subplots(nrows=1, ncols=2, sharey='all')
a.plot([i for i in range(10)])
b.plot([1 for i in range(10)])
plt.show()