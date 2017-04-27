from tkinter import *


class Calculator():
    def __init__(self):
        self.total = 0
        self.current_val = ""
        self.new_num = True
        self.func_pending = False
        self.func = ""
        self.equals = False


    def press_num(self, num):
        self.equals = False
        hold = text_box.get()
        hold2 = str(num)
        if self.new_num:
            self.current_val = hold2
            self.new_num = False
        else:
            if hold2 == '.':
                if hold2 in hold:
                    return
            self.current_val = hold + hold2
        self.display(self.current_val)

    def calculate_total(self):
        self.equals = True
        self.current_val = float(self.current_val)
        if self.func_pending == True:
            self.find_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def find_sum(self):
        if self.func == "addition":
            self.total += self.current_val
        if self.func == "subtraction":
            self.total -= self.current_val
        if self.func == "multiplication":
            self.total *= self.current_val
        if self.func == "division":
            self.total /= self.current_val
        self.new_num = True
        self.func_pending = False
        self.display(self.total)

    def function(self, func):
        self.current_val = float(self.current_val)
        if self.func_pending:
            self.find_sum()
        elif not self.equals:
            self.total = self.current_val
        self.new_num = True
        self.func_pending = True
        self.func = func
        self.equals = False

    def cancel(self):
        self.equals = False
        self.current_val = "0"
        self.display(0)
        self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.total = 0

    def sign(self):
        self.equals = False
        self.current_val = -(float(text_box.get()))
        self.display(self.current_val)
    
    def backspace(self):
        self.equals = False
        self.current_val = (text_box.get()[:-1])
        self.display(self.current_val)


sumA = Calculator()
root = Tk()
root.grid()
displayFrame = Frame(root)
displayFrame.pack()
buttonsFrame = Frame(root)
buttonsFrame.pack()

for r in range (0,5):
    Grid.rowconfigure(root, r, weight=1)
for c in range (0,3):
    Grid.columnconfigure(root, c, weight=1)


root.title("Calculator Application")
text_box = Entry(displayFrame, justify=RIGHT, relief=FLAT)
text_box.grid(row = 0, column = 0, columnspan = 3)
text_box.insert(0, "0")

num_grid = "789456123"
n = 0
b_list = []
for i in range (2,5):
    for f in range(3):
        b_list.append(Button(buttonsFrame, text = num_grid[n], relief=FLAT))
        b_list[n].grid(row = i, column = f)
        b_list[n]["command"] = lambda x = num_grid[n]: sumA.press_num(x)
        n += 1

b_0 = Button(buttonsFrame, text="0", relief=FLAT)
b_0["command"] = lambda: sumA.press_num(0)
b_0.grid(row=5, column=1)

b_divide = Button(buttonsFrame, text= chr(247), relief=FLAT)
b_divide["command"] = lambda: sumA.function("division")
b_divide.grid(row = 1, column = 3)

b_multiply = Button(buttonsFrame, text="x", relief=FLAT)
b_multiply["command"] = lambda: sumA.function("multiplication")
b_multiply.grid(row = 2, column = 3)

b_subtract = Button(buttonsFrame, text="-", relief=FLAT)
b_subtract["command"] = lambda: sumA.function("subtraction")
b_subtract.grid(row = 3, column = 3)

b_addition = Button(buttonsFrame, text="+", relief=FLAT)
b_addition["command"] = lambda:sumA.function("addition")
b_addition.grid(row = 4, column = 3)

b_decimal = Button(buttonsFrame, text=".", relief=FLAT)
b_decimal["command"] = lambda: sumA.press_num(".")
b_decimal.grid(row = 5, column = 2)

b_sign = Button(buttonsFrame, text="+/-", relief=FLAT)
b_sign["command"] = sumA.sign
b_sign.grid(row = 5, column = 0)

b_clear = Button(buttonsFrame, text="C", relief=FLAT)
b_clear["command"] = sumA.cancel
b_clear.grid(row = 1, column = 1)

b_clearAll = Button(buttonsFrame, text="CE", relief=FLAT)
b_clearAll["command"] = sumA.all_cancel
b_clearAll.grid(row = 1, column = 0)

b_equals = Button(buttonsFrame, text = "=", relief=FLAT)
b_equals["command"] = sumA.calculate_total
b_equals.grid(row = 5, column = 3)

b_backspace = Button(buttonsFrame, text = "<-", relief=FLAT)
b_backspace["command"] = sumA.backspace
b_backspace.grid(row = 1, column = 2)

root.mainloop()
