import tkinter as tk


### This Create a Window on the Screen Using Tkinter Library of Python ###
calci = tk.Tk()
calci.title("Calculator")



### This is the Acutal Functions Which Perform All The Basic Mathematical Calculation ###
def numberClick(number):
    global operators
    operators = operators + str(number)
    userInput.set(operators)

def clearScreen():
    global operators
    operators = ""
    userInput.set(operators)

def addition():
    global operators
    operators = str(eval(operators))
    userInput.set(operators)



### Variables Which Will be Used for Calulation ###
operators = ""
userInput = tk.StringVar()



### This is for Entry Field of User Input ### 
display = tk.Entry(calci,font=('arial',20,'bold'),bd=25,textvar=userInput,justify="right")
display.grid(columnspan=5)



### First Row of Numbers i.e. 7 8 9 ###
button7 = tk.Button(calci,text="7",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(7))
button7.grid(row=1,column=0)

button8 = tk.Button(calci,text="8",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(8))
button8.grid(row=1,column=1)

button9 = tk.Button(calci,text="9",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(9))
button9.grid(row=1,column=2)



### Second Row of Numbers i.e 4 5 6 ###
button4 = tk.Button(calci,text="4",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(5))
button4.grid(row=2,column=0)

button5 = tk.Button(calci,text="5",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(5))
button5.grid(row=2,column=1)

button6 = tk.Button(calci,text="6",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(6))
button6.grid(row=2,column=2)



### Third Row of Numbers i.e 1 2 3 ###
button1 = tk.Button(calci,text="1",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(1))
button1.grid(row=3,column=0)

button2 = tk.Button(calci,text="2",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(2))
button2.grid(row=3,column=1)

button3 = tk.Button(calci,text="3",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(3))
button3.grid(row=3,column=2)



### Fourth Row of Numbers i.e 0 . Clear ###
button0 = tk.Button(calci,text="0",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(0))
button0.grid(row=4,column=0)

buttonDot = tk.Button(calci,text=".",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick("."))
buttonDot.grid(row=4,column=1)

buttonclear = tk.Button(calci,text="C",font=('arial',20,'bold'),bd=5,padx=10,command=clearScreen)
buttonclear.grid(row=4,column=2)



### This Block Represent All Operators i.e   + - * / i.e Column Number 4 ###
buttonPlus = tk.Button(calci,text="+",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick("+"))
buttonPlus.grid(row=1,column=4)

buttonMinus = tk.Button(calci,text="-",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick("-"))
buttonMinus.grid(row=2,column=4)

buttonMultiply = tk.Button(calci,text="*",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick("*"))
buttonMultiply.grid(row=3,column=4)

buttonDivision = tk.Button(calci,text="/",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick("/"))
buttonDivision.grid(row=4,column=4)



### This  Block Contain Last Block of Display ### i.e (, ), Quit, =  ###
buttonRBracket = tk.Button(calci,text="(",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick("("))
buttonRBracket.grid(row=5,column=0)


buttonRBracket = tk.Button(calci,text=")",font=('arial',20,'bold'),bd=5,padx=10,command=lambda : numberClick(")"))
buttonRBracket.grid(row=5,column=1)


buttonExit= tk.Button(calci,text="X",font=('arial',20,'bold'),bd=5,padx=10,command= quit)
buttonExit.grid(row=5,column=2)

buttonEqual = tk.Button(calci,text="=",font=('arial',20,'bold'),bd=5,padx=10,command=addition)
buttonEqual.grid(row=5,column=4)


### This is Used to Hold Output Window on the Screen ###
calci.mainloop()