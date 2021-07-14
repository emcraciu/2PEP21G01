from app2_time_factorial import timing_timeit
import matplotlib.pyplot as plt



def graph_function(function):
    for_loop, recursive = function()
    fig1, ay1 = plt.subplots(nrows=1, ncols=1, sharex='all')
    print(type(ay1))

    ay1.plot([i for i in range(1, 255)], for_loop, recursive, label='factorial 1 vs factorial 2')
    ay1.legend()
    plt.xlabel("iteration")
    plt.ylabel('time')
    plt.title("factorial")
    plt.show()

graph_function(timing_timeit)