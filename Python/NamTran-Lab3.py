# This is an example of using the tkinter python extension to create a basic window with button

from tkinter import *


class CatDatabase():
    def __init__(self):
        self.lis = []

    def add_cat(self, cat_info):
        self.lis.append(cat_info)

    def print_cat_database(self):
        format = "Output Format:\n\n**********************\n\nMy Cat Registration System\n\n**********************\nCat Name, Cat ID\n"
        if (self.lis):
            print(format)
            for i in self.lis:
                print(i[0]+","+i[1])
        else:
            print("No info")


class MyFirstGUI:  # class definition
    # This is the initialize function for a class.
    # Variables belonging to this class will get created and initialized in this function
    # What is the self parameter? It represents this class itself.
    # By using self.functionname, you can call functions belonging to this class.
    # By using self.variablename, you can create and use variables belonging to this class.
    # It needs to be the first parameter of all the functions in your class
    def __init__(self, root):
        # Master is the default prarent object of all widgets.
        # You can think of it as the window that pops up when you run the GUI code.
        self.master = root
        self.master.title("My Cat Registration System")
        self.catDatabase = CatDatabase()
        # grid function puts a widget at a certain location
        # return value is none, please do not use it like self.label=Label().grad()
        # it will make self.label=none and you will no longer be able to change the label's content
        self.name_label = Label(self.master, text="Cat Name: ")
        self.name_label.grid(row=0, column=0, sticky=E)
        self.reg_name_label = Label(self.master, text="Registered cat name: ")
        self.reg_name_label.grid(row=1, column=0, sticky=E)
        self.cat_id_label = Label(self.master, text="Cat ID: ")
        self.cat_id_label.grid(row=0, column=2, sticky=E)
        self.reg_id_label = Label(self.master, text="Registered ID: ")
        self.reg_id_label.grid(row=1, column=2, sticky=E)

        self.catnameentry = Entry(self.master)
        self.catnameentry.grid(row=0, column=1, sticky=E)
        self.cat_name_output_entry = Entry(self.master)
        self.cat_name_output_entry.grid(row=1, column=1, sticky=E)
        self.cat_id_entry = Entry(self.master)
        self.cat_id_entry.grid(row=0, column=3, sticky=E)
        self.reg_id_entry = Entry(self.master)
        self.reg_id_entry.grid(row=1, column=3, sticky=E)

        self.submitbutton = Button(
            self.master, text="Submit Cat", command=self.submitname)
        self.submitbutton.grid(row=0, column=4, sticky=E)
        self.print_database_button = Button(
            self.master, text="Print Database", command=self.print_database)
        self.print_database_button.grid(row=1, column=4, sticky=E)

    def submitname(self):
        if (self.catnameentry.get() and self.cat_id_entry.get()):
            self.cat_name_output_entry.delete(0, END)
            self.cat_name_output_entry.insert(0, self.catnameentry.get())
            self.reg_id_entry.delete(0, END)
            self.reg_id_entry.insert(0, self.cat_id_entry.get())
            tuple = (self.catnameentry.get(), self.cat_id_entry.get())
            self.catDatabase.add_cat(tuple)
        else:
            print("Error: Please enter both name and id")

    def print_database(self):
        self.catDatabase.print_cat_database()


if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyFirstGUI(myTkRoot)
    myTkRoot.mainloop()
