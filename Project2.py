from tkinter import *
'''
declaring expression variable globally
'''
expression = ""
'''function to update the expression
 in the entry box
 '''
def press(num):
    global expression
    if (num == "sqrt"):
        num = str(num) + "**0.5"

    expression = expression + str(num)
    equations.set(expression)
'''
function to assess final expression
try and except statements used to handle 
zero division errors
'''
def equals():
    try:
        global expression
        total = str(eval(expression))
        equations.set(total)
        expression = ""

    except:
        equations.set(" error ")
        expression = ""

'''
function used to clear entry box
of text
'''
def clear():
    global expression
    expression = ""
    equations.set("")

'''
creating a GUI window
setting the background color to teal
titling the window as Calculator
sizing the window to 215x190
StringVar() is variable class created by 
equations
creating the text entry box and making it un-editable
grid method for placing widgets at respective locations
'''
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="teal")
    gui.title("Calculator")
    gui.geometry("215x190")
    equations = StringVar()
    expression_field = Entry(gui, textvariable=equations, state='readonly')
    expression_field.grid(columnspan=4, ipadx=5)

    '''
    creating buttons and placing them at a certain spot on the window
    when the button is pressed the command will be operated
    buttons 0-9 are included along with multiplication,division, subtraction, multiplication, square'''

    button1 = Button(gui, text=' 1 ', fg='black', bg='white',command=lambda: press(1), height=1, width=2)
    button1.grid(row=5, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='white',command=lambda: press(2), height=1, width=2)
    button2.grid(row=5, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='white',command=lambda: press(3), height=1, width=2)
    button3.grid(row=5, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='white',command=lambda: press(4), height=1, width=2)
    button4.grid(row=4, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='white',command=lambda: press(5), height=1, width=2)
    button5.grid(row=4, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='white',command=lambda: press(6), height=1, width=2)
    button6.grid(row=4, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='white',command=lambda: press(7), height=1, width=2)
    button7.grid(row=3, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='white',command=lambda: press(8), height=1, width=2)
    button8.grid(row=3, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='white',command=lambda: press(9), height=1, width=2)
    button9.grid(row=3, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='white',command=lambda: press(0), height=1, width=2)
    button0.grid(row=6, column=1)

    plusButton = Button(gui, text=' + ', fg='black', bg='white',command=lambda: press("+"), height=1, width=2)
    plusButton.grid(row=2, column=3)

    minusButton = Button(gui, text=' - ', fg='black', bg='white',command=lambda: press("-"), height=1, width=2)
    minusButton.grid(row=3, column=3)

    multiplicationButton = Button(gui, text=' * ', fg='black', bg='white',command=lambda: press("*"), height=1, width=2)
    multiplicationButton.grid(row=4, column=3)

    divisionButton = Button(gui, text=' / ', fg='black', bg='white',command=lambda: press("/"), height=1, width=2)
    divisionButton.grid(row=5, column=3)

    equalsButton = Button(gui, text=' = ', fg='black', bg='white',command=equals, height=1, width=2)
    equalsButton.grid(row=6, column=3)

    clearButton = Button(gui, text='Clear', fg='black', bg='white',command=clear, height=1, width=2)
    clearButton.grid(row=6, column=2)

    decimalButton = Button(gui, text='.', fg='black', bg='white',command=lambda: press('.'), height=1, width=2)
    decimalButton.grid(row=6, column=0)

    squareRootButton = Button(gui, text=' √ ', fg='black', bg='white',command=lambda: press("**0.5"), height=1, width=2)
    squareRootButton.grid(row=2, column=1)

    piButton = Button(gui, text=' π ', fg='black', bg='white', command=lambda: press("3.1415"), height=1,width=2)
    piButton.grid(row=2, column=2)

    exponentButton = Button(gui, text=' ^ ', fg='black', bg='white', command=lambda: press("**"), height=1, width=2)
    exponentButton.grid(row=2, column=0)

    gui.mainloop()
