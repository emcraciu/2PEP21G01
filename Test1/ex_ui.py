import tkinter
from Questions import qst
main_window = tkinter.Tk()
main_window.title("Exam")


class ExamWindow():
    def __init__(self, root_window: tkinter.Tk):
        self.root_window = root_window
        for i in range(1, 10):
            self.__setattr__("label" + str(i),
                             tkinter.Label(self.root_window, text="Exam" + str(i), width=20, height=2, bg="lightblue"))
        self.__getattribute__("label1").grid(row=0, column=0)
        self.__getattribute__("label2").grid(row=0, column=1)
        self.__getattribute__("label3").grid(row=0, column=2)
        self.__getattribute__("label4").grid(row=2, column=0)
        self.__getattribute__("label5").grid(row=2, column=1)
        self.__getattribute__("label6").grid(row=2, column=2)
        self.__getattribute__("label7").grid(row=4, column=0)
        self.__getattribute__("label8").grid(row=4, column=1)
        self.__getattribute__("label9").grid(row=4, column=2)
        button1 = tkinter.Button(self.root_window, text="START", height=3, highlightbackground="green", width=10,
                                 command=lambda: self.new_exam("Exam1",1))
        button2 = tkinter.Button(self.root_window, text="START", height=3, highlightbackground="green", width=10,
                                 command=lambda: self.new_exam("Exam2",2))
        button3 = tkinter.Button(self.root_window, text="START", height=3, highlightbackground="green", width=10,
                                 command=lambda: self.new_exam("Exam3",3))
        button4 = tkinter.Button(self.root_window, text="START", height=3, highlightbackground="green", width=10,
                                 command=lambda: self.new_exam("Exam4",4))
        button5 = tkinter.Button(self.root_window, text="START", height=3, highlightbackground="green", width=10,
                                 command=lambda: self.new_exam("Exam5",5))
        button6 = tkinter.Button(self.root_window, text="START", height=3, highlightbackground="green", width=10,
                                 command=lambda: self.new_exam("Exam6",6))
        button7 = tkinter.Button(self.root_window, text="START", height=3, highlightbackground="green", width=10,
                                 command=lambda: self.new_exam("Exam7",7))
        button8 = tkinter.Button(self.root_window, text="START", height=3, highlightbackground="green", width=10,
                                 command=lambda: self.new_exam("Exam8",8))
        button9 = tkinter.Button(self.root_window, text="START", height=3, highlightbackground="green", width=10,
                                 command=lambda: self.new_exam("Exam9",9))

        button1.grid(row=1, column=0)
        button2.grid(row=1, column=1)
        button3.grid(row=1, column=2)
        button4.grid(row=3, column=0)
        button5.grid(row=3, column=1)
        button6.grid(row=3, column=2)
        button7.grid(row=5, column=0)
        button8.grid(row=5, column=1)
        button9.grid(row=5, column=2)

    def new_exam(self, exam_num: str,nr):
        exam_window = tkinter.Tk()
        exam_window.title(f"{exam_num}")
        exam = TestWindow(exam_window,nr)
        exam.run()

    def run(self):
        self.root_window.mainloop()

def switch(leng,arg):
    switcher = {}
    for i in range(1, leng):
        switcher[i] = str(i)

    return(switcher[arg])



class TestWindow():
    def __init__(self,root_window:tkinter.Tk,nr):
        self.test_window=root_window
        self.test_label1=tkinter.Label(self.test_window,text=qst(1),justify=tkinter.LEFT)
        self.test_label2 = tkinter.Label(self.test_window,text=qst(2),justify=tkinter.LEFT)
        self.test_label3 = tkinter.Label(self.test_window, text=qst(3),justify=tkinter.LEFT)
        self.test_label4= tkinter.Label(self.test_window,  text=qst(4),justify=tkinter.LEFT)
        self.test_label5 = tkinter.Label(self.test_window, text=qst(5),justify=tkinter.LEFT)
        self.test_label6 = tkinter.Label(self.test_window, text=qst(6),justify=tkinter.LEFT)


        self.test_label1.grid(row=0,column=0,sticky=tkinter.S)
        self.test_label2.grid(row=1, column=0,sticky=tkinter.NW)
        self.test_label3.grid(row=2, column=0,sticky=tkinter.NW)
        self.test_label4.grid(row=3, column=0,sticky=tkinter.NW)
        self.test_label5.grid(row=4, column=0,sticky=tkinter.NW)
        self.test_label6.grid(row=5, column=0,sticky=tkinter.NW)


    def run(self):
        self.test_window.mainloop()


exam = ExamWindow(main_window)
exam.run()