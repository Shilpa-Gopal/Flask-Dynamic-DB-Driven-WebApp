from tkinter import *


expression = ''
def value(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)


def equal():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=total
    except:
        equation.set('ERROR-Check Input')
        expression=''

def clear():
    global expression
    expression=''
    equation.set('')

def back():
    global expression
    expression=expression[:-1]
    equation.set(expression)



win=Tk()
win.title("Simple Calculator")
win.configure(background='lightgrey')
win.geometry('470x350')

equation=StringVar()
expression_label=Entry(win,textvariable=equation, font=('Bookman Old Style',15))
expression_label.grid(row=1,columnspan=5,column=0,ipadx=110,ipady=10)



b1=Button(win,text='1',height=2, width=8,bg='black',fg='white',font=('Bookman Old Style',15), command=lambda: value(1), activeforeground='lightgrey')
b1.grid(row=4,column=0)
b2=Button(win,text='2',height=2, width=8,bg='black',fg='white',font=('Bookman Old Style',15),command=lambda: value(2),activeforeground='lightgrey')
b2.grid(row=4,column=1)
b3=Button(win,text='3',height=2, width=8,bg='black',fg='white',font=('Bookman Old Style',15),command=lambda: value(3),activeforeground='lightgrey')
b3.grid(row=4,column=2)
b4=Button(win,text='4',height=2, width=8,bg='black',fg='white',font=('Bookman Old Style',15),command=lambda: value(4),activeforeground='lightgrey')
b4.grid(row=5,column=0)
b5=Button(win,text='5',height=2, width=8,bg='black',fg='white',font=('Bookman Old Style',15),command=lambda: value(5),activeforeground='lightgrey')
b5.grid(row=5,column=1)
b6=Button(win,text='6',height=2, width=8,bg='black',fg='white',font=('Bookman Old Style',15),command=lambda: value(6),activeforeground='lightgrey')
b6.grid(row=5,column=2)
b7=Button(win,text='7',height=2, width=8,bg='black',fg='white',font=('Bookman Old Style',15),command=lambda: value(7),activeforeground='lightgrey')
b7.grid(row=6,column=0)
b8=Button(win,text='8',height=2, width=8,bg='black',fg='white',font=('Bookman Old Style',15),command=lambda: value(8),activeforeground='lightgrey')
b8.grid(row=6,column=1)
b9=Button(win,text='9',height=2, width=8,bg='black',fg='white',font=('Bookman Old Style',15),command=lambda: value(9),activeforeground='lightgrey')
b9.grid(row=6,column=2)
b0=Button(win,text='0',height=2, width=8,bg='black',fg='white',font=('Bookman Old Style',15),command=lambda: value(0),activeforeground='lightgrey')
b0.grid(row=7,column=1)

bplus=Button(win,text='+',height=2, width=8,bg='black',fg='orange',font=('Bookman Old Style',15), command=lambda: value('+'), activeforeground='lightgrey')
bplus.grid(row=4,column=3)
bmins=Button(win,text='-',height=2, width=8,bg='black',fg='orange',font=('Bookman Old Style',15),command=lambda: value('-'),activeforeground='lightgrey')
bmins.grid(row=5,column=3)
bmul=Button(win,text='x',height=2, width=8,bg='black',fg='orange',font=('Bookman Old Style',15),command=lambda: value('*'),activeforeground='lightgrey')
bmul.grid(row=6,column=3)
bdiv=Button(win,text='/',height=2, width=8,bg='black',fg='orange',font=('Bookman Old Style',15),command=lambda: value('/'),activeforeground='lightgrey')
bdiv.grid(row=7,column=3)
bequ=Button(win,text='=',height=2, width=8,bg='black',fg='orange',font=('Bookman Old Style',15),command=equal, activeforeground='lightgrey')
bequ.grid(row=7,column=2)
bdot=Button(win,text='.',height=2, width=8,bg='black',fg='orange',font=('Bookman Old Style',15),command=lambda: value('.'),activeforeground='lightgrey')
bdot.grid(row=7,column=0)
#bclear=Button(win,text='clear',height=1, width=10,bg='black',fg='orange',font=('Bookman Old Style',15), command=clear,activeforeground='lightgrey')
#bclear.grid(row=8,columnspan=3)

bdot=Button(win,text='clear',height=1, width=8,bg='black',fg='orange',font=('Bookman Old Style',15),command=clear, activeforeground='lightgrey')
bdot.grid(row=8,column=1)
bdot=Button(win,text='back',height=1, width=8,bg='black',fg='orange',font=('Bookman Old Style',15),command=back, activeforeground='lightgrey')
bdot.grid(row=8,column=2)
bdot=Button(win,text='close',height=1, width=8,bg='black',fg='orange',font=('Bookman Old Style',15),command=win.destroy, activeforeground='lightgrey')
bdot.grid(row=8,column=3)

win.mainloop()