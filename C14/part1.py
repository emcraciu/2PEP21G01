import os
import tkinter
import tkinter.messagebox

from C11_UI.app2 import LoginWindow


class MenuWindow:

    def __init__(self, username😒

        tr):
    self.username = username
    root_window =


tkinter.Tk
()
root_window.title('menu')
self.root_window = root_window

main_menu =
tkinter.Menu
(root_window)
self.root_window.config(menu=main_menu)

file_menu =
tkinter.Menu
(main_menu)
main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=self.file_new_menu)
file_menu.add_separator()
file_menu.add_command(label='Edit', command=self.file_edit_menu)
file_menu.add_separator()
file_menu.add_command(label='Close', command=self.file_close_menu)

edit_menu =
tkinter.Menu
(main_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)

view_menu =
tkinter.Menu
(main_menu)
main_menu.add_cascade(label='View', menu=view_menu)

send_menu =
tkinter.Menu
(main_menu)
main_menu.add_cascade(label='Send', menu=send_menu)

self.frame1 = tkinter.Frame(self.root_window, width=100, height=300)
self.frame1.pack(side=tkinter.LEFT)
refresh_button = tkinter.Button(self.frame1, text='Refresh', command=self.get_directory)
refresh_button.pack(
    side=tkinter.TOP
)

self.frame2 = tkinter.Frame(self.root_window)
self.frame2.pack(side=tkinter.RIGHT)


def get_directory(self):
    for dir in os.listdir():
        label = tkinter.Label(self.frame1, text=str(dir))
        label.pack()


def run(self):
    self.root_window.mainloop()


def file_new_menu(self):
    print('Creating new file ...')
    main_window =


tkinter.Tk
()
main_window.title('copy of menu')
menu = MenuWindow(main_window)

menu.run
()


def file_edit_menu(self):
    print('Editing new file ...')
    self.text = tkinter.Text(self.frame2, height=25, width=80)
    destination = tkinter.Label(self.frame2, text='To: ')
    destination.grid(row=0, column=1, sticky=tkinter.E)
    subject = tkinter.Label(self.frame2, text='Subject: ')
    subject.grid(row=1, column=1, sticky=tkinter.E)
    self.dest_entry = tkinter.Entry(self.frame2)
    self.dest_entry.grid(row=0, column=2, sticky=tkinter.W)
    self.subj_entry = tkinter.Entry(self.frame2)
    self.subj_entry.grid(row=1, column=2, sticky=tkinter.W)
    send_button = tkinter.Button(self.frame2, text='Send', command=self.send_message)
    send_button.grid(row=0, rowspan=2, column=3)
    search_button = tkinter.Button(self.frame2, text='Search', command=self.search_message)
    search_button.grid(row=3, column=1)
    self.search_entry = tkinter.Entry(self.frame2)
    self.search_entry.grid(row=3, column=2, columnspan=2, sticky=tkinter.E + tkinter.W)
    self.text.grid(row=2, columnspan=4)


def search_message(self):


self.search
= self.search_entry.get()
self.result =
self.text.search
(
    self.search
    , '0.0', tkinter.END)
print(self.result)
self.text.tag_add('selection', self.result,
                  self.result.split(".")[0] + '.' + str(int(self.result.split('.')[1]) + len(
                      self.search
                  )))
self.text.tag_config('selection', background='yellow')


def send_message(self):
    if not self.dest_entry.get():
        tkinter.messagebox.showinfo('Warning', 'Missing destination')
        return
    if not self.subj_entry.get():
        tkinter.messagebox.showinfo('Warning', 'Missing subject')
        return
    if not self.text.get('0.0', tkinter.END).strip():
        tkinter.messagebox.showinfo('Warning', 'Missing text')
        return

    answ = tkinter.messagebox.askquestion('Confirmation', 'Are you sure you want to send?')
    if answ == 'yes':
        print('Running code...')
    else:
        print('Canceling...')


def file_close_menu(self):
    self.root_window.quit()


login = LoginWindow()
login.run
()
# print(login.logn_info)

menu = MenuWindow(login.login_info)
menu.run
()
()