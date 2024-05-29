from tkinter import *

expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":

    Calc = Tk()
    Calc.configure(background="black")
    Calc.title("Calculator")
    Calc.geometry('300x400')

    equation = StringVar()
    expression_field = Entry(Calc, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=20)

    button1 = Button(Calc, text='1', fg='white', bg='black',
                 command=lambda: press(1), height=5, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(Calc, text='2', fg='white', bg='black',
                 command=lambda: press(2), height=5, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(Calc, text='3', fg='white', bg='black',
                 command=lambda: press(3), height=5, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(Calc, text='4', fg='white', bg='black',
                 command=lambda: press(4), height=5, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(Calc, text='5', fg='white', bg='black',
                 command=lambda: press(5), height=5, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(Calc, text='6', fg='white', bg='black',
                 command=lambda: press(6), height=5, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(Calc, text='7', fg='white', bg='black',
                 command=lambda: press(7), height=5, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(Calc, text='8', fg='white', bg='black',
                 command=lambda: press(8), height=5, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(Calc, text='9', fg='white', bg='black',
                 command=lambda: press(9), height=5, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(Calc, text='0', fg='white', bg='black',
                 command=lambda: press(0), height=5, width=7)
    button0.grid(row=5, column=0)

    plus = Button(Calc, text='+', fg='white', bg='black',
                  command=lambda: press("+"), height=5, width=7)
    plus.grid(row=2, column=3)

    minus = Button(Calc, text='-', fg='white', bg='black',
                  command=lambda: press("-"), height=5, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(Calc, text='*', fg='white', bg='black',
                  command=lambda: press("*"), height=5, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(Calc, text='/', fg='white', bg='black',
                  command=lambda: press("/"), height=5, width=7)
    divide.grid(row=5, column=3)

    equal = Button(Calc, text='=', fg='white', bg='black',
                  command=equalpress, height=5, width=7)
    equal.grid(row=5, column=2)

    clear = Button(Calc, text='Clear', fg='white', bg='black',
                   command=clear, height=5, width=7)
    clear.grid(row=5, column=1)

    decimal = Button(Calc, text='.', fg='white', bg='black',
                     command=lambda: press('.'), height=5, width=7)
    decimal.grid(row=5, column=4)

Calc.mainloop()