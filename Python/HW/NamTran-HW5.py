from tkinter import *
from tkmacosx import Button
from turtle import width
import re

class LexGUI:

    def __init__(self, root):
        self.counter = 0
        self.master = root
        self.master.title("Lexer for TinyPie")
        # first setup
        self.input_code = Label(self.master, text="Source Code: ")
        self.input_code.grid(row=0, column=0, sticky=W, padx=35, pady=5)

        self.input_txt = Text(self.master, height=18, width=35,font=("Calibri", 15))
        self.input_txt.grid(row=1, column=0, sticky=W, padx=35, pady=5)
        self.input_txt.config(
            highlightbackground="ORANGE", highlightthickness=1)

        self.input_counter = Label(
            self.master, text="Current Processing Line: ")
        self.input_counter.grid(row=2, column=0, sticky=W, padx=35)

        self.counter_entry = Entry(self.master, width=2)
        self.counter_entry.grid(row=2, column=0, sticky=E, padx=200)
        self.counter_entry.config({"background": "YELLOW"})
        self.counter_entry.delete(0, END)
        self.counter_entry.insert(0, self.counter)
        # next line button
        self.next_button = Button(
            self.master, text="Next Line", bg='BLUE', fg='WHITE', command=self.next_line)
        self.next_button.grid(row=3, column=0, sticky=W, padx=35, pady=5)
        # second setup
        self.output_code = Label(self.master, text="Tokens: ")
        self.output_code.grid(row=0, column=1, sticky=W, padx=35, pady=1)

        self.output_txt = Text(self.master, height=18, width=35, font=("Calibri", 15))
        self.output_txt.grid(row=1, column=1, sticky=W, padx=35, pady=1)
        self.output_txt.config(
            highlightbackground="BLUE", highlightthickness=1)
        # quit button
        self.quit_button = Button(
            self.master, text="Exit", bg='BLUE', fg='WHITE', command=quit)
        self.quit_button.grid(row=3, column=1, sticky=E, padx=35, pady=5)

    def next_line(self):
        splitted_lis = []
        input = self.input_txt.get("1.0", END)
        if(input):
            splitted_lis = input.splitlines()
            for j in self.cutonelinetokens(splitted_lis[self.counter]):
                self.output_txt.insert(INSERT, j + "\n")
            self.counter += 1
            self.counter_entry.delete(0, END)
            self.counter_entry.insert(0, self.counter)

            if (self.counter >= len(splitted_lis)):
                text = "\n**End of code**.\n"
                self.output_txt.insert(INSERT, text)
                self.counter = 0

    def cutonelinetokens(self, string):
        result = []
        string = string.lstrip()
        while(string):
            keyw_reg = re.compile(r"(\bif\b)|(\belse\b)|(\bfloat\b)|(\bint\b)")
            ope_reg = re.compile(r"\+|\*|=|>")
            sep_reg = re.compile(r"\(|\)|:|\"|;|\“|\”")
            id_reg = re.compile(r"([A-Za-z]+\d+)|([A-Za-z]+)")
            int_reg = re.compile(r"(?<![\d.])[0-9]+(?![\d.])")
            float_reg = re.compile(r"\d+\.\d+")
            string_reg = re.compile(r'^[\w\s\d]+(?=”)')

            keyw_token = keyw_reg.match(string)
            ope_token = ope_reg.match(string)
            sep_token = sep_reg.match(string)
            id_token = id_reg.match(string)
            int_token = int_reg.match(string)
            float_token = float_reg.match(string)
            string_token = string_reg.match(string)
            # keyword
            if(keyw_token != None):
                new_string = "<keyword, " + keyw_token.group(0) + ">"
                result.append(new_string)
                string = string.replace(keyw_token.group(0), ' ', 1)
                string = string.lstrip()
            # operator
            elif(ope_token != None):
                new_string1 = "<operator, " + ope_token.group(0) + ">"
                result.append(new_string1)
                string = string.replace(ope_token.group(0), ' ', 1)
                string = string.lstrip()
            # seperator
            elif(sep_token != None):
                new_string2 = "<seperator, " + sep_token.group(0) + ">"
                result.append(new_string2)
                string = string.replace(sep_token.group(0), ' ', 1)
                string = string.lstrip()
            # string lit
            elif(string_token != None):
                new_string6 = "<string literal, " + string_token.group(0) + ">"
                result.append(new_string6)
                string = string.replace(string_token.group(0), '', 1)
                string = string.lstrip()
            # identifier
            elif(id_token != None):
                new_string3 = "<identifier, " + id_token.group(0) + ">"
                result.append(new_string3)
                string = string.replace(id_token.group(0), '', 1)
                string = string.lstrip()
            # integer lit
            elif(int_token != None):
                new_string4 = "<integer literal, " + int_token.group(0) + ">"
                result.append(new_string4)
                string = string.replace(int_token.group(0), '', 1)
                string = string.lstrip()
            # float lit
            elif(float_token != None):
                new_string5 = "<float literal, " + float_token.group(0) + ">"
                result.append(new_string5)
                string = string.replace(float_token.group(0), '', 1)
                string = string.lstrip()
            else:
                print("Cannot process input: ")
                print(string)
                string = ""
        return result


if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = LexGUI(myTkRoot)
    myTkRoot.mainloop()
