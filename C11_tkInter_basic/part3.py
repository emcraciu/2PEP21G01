import tkinter
import time


def do_something():
    print(time.time())


main_window = tkinter.Tk()
main_window.title('Python M2 UI')

button1 = tkinter.Button(main_window, text='Just Print', command=do_something)
button1.grid(row=0, column=0)

main_window.mainloop()
