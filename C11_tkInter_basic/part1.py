import tkinter

main_window = tkinter.Tk()
main_window.title('Python M2 UI')

label1 = tkinter.Label(main_window, text='Red Label', bg='red')
label1.pack()
label2 = tkinter.Label(main_window, text='Green Label', bg='green')
label2.pack(fill=tkinter.X)
label3 = tkinter.Label(main_window, text='Blue Label', bg='blue')
label3.pack(side=tkinter.LEFT, fill=tkinter.Y)


main_window.mainloop()
print('All done')
