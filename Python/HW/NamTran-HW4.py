from tkinter import *
from tkmacosx import Button
from turtle import width


class LexGUI:

    def __init__(self, root):
        self.counter = 0
        self.master = root
        self.master.title("Lexical Analyzer for TinyPie")
        # first setup
        self.input_code = Label(self.master, text="Source Code Input: ")
        self.input_code.grid(row=0, column=0, sticky=W, padx=35, pady=5)

        self.input_txt = Text(self.master, height=18, width=35)
        self.input_txt.grid(row=1, column=0, sticky=W, padx=35, pady=5)
        self.input_txt.config(
            highlightbackground="ORANGE", highlightthickness=1)

        self.input_counter = Label(
            self.master, text="Current Processing Line: ")
        self.input_counter.grid(row=2, column=0, sticky=W, padx=35)

        self.counter_entry = Entry(self.master, width=2)
        self.counter_entry.grid(row=2, column=0, sticky=E, padx=200)
        self.counter_entry.delete(0, END)
        self.counter_entry.insert(0, self.counter)
        # next line button
        self.next_button = Button(
            self.master, text="Next Line", bg='GREEN', fg='WHITE', command=self.next_line)
        self.next_button.grid(row=3, column=0, sticky=W, padx=35, pady=5)
        # second setup
        self.output_code = Label(self.master, text="Lexical Analyzed Result: ")
        self.output_code.grid(row=0, column=1, sticky=W, padx=35, pady=1)

        self.output_txt = Text(self.master, height=18, width=35)
        self.output_txt.grid(row=1, column=1, sticky=W, padx=35, pady=1)
        self.output_txt.config(
            highlightbackground="ORANGE", highlightthickness=1)
        # quit button
        self.quit_button = Button(
            self.master, text="Quit", bg='GREEN', fg='WHITE', command=quit)
        self.quit_button.grid(row=3, column=1, sticky=E, padx=35, pady=5)

    def next_line(self):
        splitted_lis = []
        input = self.input_txt.get("1.0", END)
        if(input):
            splitted_lis = input.splitlines()
            self.output_txt.insert(INSERT, splitted_lis[self.counter]+'\n')
            self.counter_entry.delete(0, END)
            self.counter_entry.insert(0, self.counter+1)
            self.counter += 1
            if (self.counter >= len(splitted_lis)):
                text = "\n**End of code**.\n"
                self.output_txt.insert(INSERT, text)
                self.counter = 0


if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = LexGUI(myTkRoot)
    myTkRoot.mainloop()
