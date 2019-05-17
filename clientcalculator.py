from tkinter import *
from tkinter import ttk
import socket


class Calculator:

    cal_value = ""
    operation = ""

    div_trigger = False
    mult_trigger = False
    add_trigger = False
    substract_trigger = False

    host = "127.0.0.1"
    port = 8000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    def button_press(self, value):
        #get current value
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, entry_val)


    def math_button_press(self, value):
        self.div_trigger = False
        self.mult_trigger = False
        self.add_trigger = False
        self.substract_trigger = False

        self.cal_value = float(self.entry_value.get())
        if value == "/":
            self.div_trigger = True
            self.operation = "/"
        elif value == "+":
            self.add_trigger = True
            self.operation = "+"
        elif value == "-":
            self.substract_trigger = True
            self.operation = "-"
        else:
            self.mult_trigger = True
            self.operation = "*"

        self.number_entry.delete(0, "end")

    def equal_button_press(self):

        if self.add_trigger or self.substract_trigger or self.div_trigger or self.mult_trigger:
            if self.add_trigger:
                self.s.sendall(str(self.cal_value).encode('utf-8'))
                val1 = self.s.recv(1024)
                pval1 = str(val1.decode('utf-8'))
                self.s.sendall(self.operation.encode('utf-8'))
                val2 = self.s.recv(1024)
                pval2 = str(val2.decode('utf-8'))
                self.s.sendall(str(self.entry_value.get()).encode('utf-8'))

            elif self.substract_trigger:
                self.s.sendall(str(self.cal_value).encode('utf-8'))
                val1 = self.s.recv(1024)
                pval1 = str(val1.decode('utf-8'))
                #print("value 1: " + pval1)
                self.s.sendall(self.operation.encode('utf-8'))
                val2 = self.s.recv(1024)
                pval2 = str(val2.decode('utf-8'))
                #print("value 2: " + pval2)
                self.s.sendall(str(self.entry_value.get()).encode('utf-8'))

            elif self.div_trigger:
                self.s.sendall(str(self.cal_value).encode('utf-8'))
                val1 = self.s.recv(1024)
                pval1 = str(val1.decode('utf-8'))
                #print("value 1: " + pval1)
                self.s.sendall(self.operation.encode('utf-8'))
                val2 = self.s.recv(1024)
                pval2 = str(val2.decode('utf-8'))
                #print("value 2: " + pval2)
                self.s.sendall(str(self.entry_value.get()).encode('utf-8'))

            elif self.mult_trigger:
                self.s.sendall(str(self.cal_value).encode('utf-8'))
                val1 = self.s.recv(1024)
                pval1 = str(val1.decode('utf-8'))
                #print("value 1: "+ pval1)
                self.s.sendall(self.operation.encode('utf-8'))
                val2 = self.s.recv(1024)
                pval2 = str(val2.decode('utf-8'))
                #print("value 2: " + pval2)
                self.s.sendall(str(self.entry_value.get()).encode('utf-8'))

            solution = self.s.recv(1024)
            psolution = float(solution.decode('utf-8'))
            print(self.cal_value, "  ", float(self.entry_value.get()), "  ", psolution)
            self.number_entry.delete(0,"end")
            self.number_entry.insert(0, psolution)


    def __init__(self, root):
        self.entry_value = StringVar(root, value="")
        root.title("Calculator")
        root.geometry("600x250")
        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton",
                        font = "Serif 15",
                        padding=10)
        style.configure("TEntry",
                        font="Serif 15",
                        padding=10)

        self.number_entry = ttk.Entry(root,
                                      textvariable= self.entry_value, width = 50)
        self.number_entry.grid(row = 0, columnspan =4)

        #1st row

        self.button7 = ttk.Button(root, text = "7",
                                  command = lambda : self.button_press('7')).grid(row = 1, column = 0)
        self.button8 = ttk.Button(root, text="8",
                                  command=lambda: self.button_press('8')).grid(row=1, column=1)
        self.button9 = ttk.Button(root, text="9",
                                  command=lambda: self.button_press('9')).grid(row=1, column=2)
        self.button_div = ttk.Button(root, text="/",
                                  command=lambda: self.math_button_press('/')).grid(row=1, column=3)

        # 2nd row

        self.button4 = ttk.Button(root, text="4",
                                  command=lambda: self.button_press('4')).grid(row=2, column=0)
        self.button5 = ttk.Button(root, text="5",
                                  command=lambda: self.button_press('5')).grid(row=2, column=1)
        self.button6 = ttk.Button(root, text="6",
                                  command=lambda: self.button_press('6')).grid(row=2, column=2)
        self.button_mul = ttk.Button(root, text="*",
                                     command=lambda: self.math_button_press('*')).grid(row=2, column=3)

        # 3th row

        self.button1 = ttk.Button(root, text="1",
                                  command=lambda: self.button_press('1')).grid(row=3, column=0)
        self.button2 = ttk.Button(root, text="2",
                                  command=lambda: self.button_press('2')).grid(row=3, column=1)
        self.button3 = ttk.Button(root, text="3",
                                  command=lambda: self.button_press('3')).grid(row=3, column=2)
        self.button_add = ttk.Button(root, text="+",
                                     command=lambda: self.math_button_press('+')).grid(row=3, column=3)
        # 4th row

        self.button0 = ttk.Button(root, text="0",
                                  command=lambda: self.button_press('0')).grid(row=4, column=0)
        #self.button_clear = ttk.Button(root, text="AC",
        #                          command=lambda: self.button_press('AC')).grid(row=4, column=1)
        self.button_sub = ttk.Button(root, text="=",
                                     command=lambda: self.equal_button_press()).grid(row=4, column=2)
        self.button_equal = ttk.Button(root, text="-",
                                     command=lambda: self.math_button_press('-')).grid(row=4, column=3)









root = Tk()

calc = Calculator(root)

root.mainloop()



