import timeit
import matplotlib.pyplot as plt

result1 = timeit.timeit('f"numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; Numbers are:{[1,2,3,4,5,6,7,8,9,10]}"')
result2 = timeit.timeit('"numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; Numbers are:{}.format([1,2,3,4,5,6,7,8,9,10])"')

l1, l2 = [], []


def ceva():
    for _ in range(100):
        result1 = timeit.timeit('f"Numbers are:{[1,2,3,4,5,6,7,8,9,10]}"', number=100)
        l1.append(result1)
        result2 = timeit.timeit('"Numbers are:{}.format([1,2,3,4,5,6,7,8,9,10])"', number=100)
        l2.append(result2)
    return l1, l2


def remove_spikes(y1, y2):
    s1 = 0
    s2 = 0
    for i in range(0, len(y1)):
        s1 += y1[i]
        s2 += y2[i]
    m1 = s1 / len(y1)
    m2 = s2 / len(y2)

    for i in range(0, len(y1)):
        if y1[i] >= 2 * m1:
            del (y1[i])

        if y2[i] >= 2 * m2:
            del (y2[i])

    return y1, y2


y1, y2 = ceva()
y1, y2 = remove_spikes(y1, y2)

fig1, (ay1, ay2) = plt.subplots(nrows=2, ncols=1, sharex='all')
fig1.dpi = 200.0

ay1.plot([i for i in range(100)], y1)
ay2.plot([i for i in range(100)], y2)

plt.show()
