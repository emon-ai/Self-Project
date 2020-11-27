from tkinter import *
window=Tk()
window.title("Calculator")

e=Entry(window,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

def button(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def add():
    first=e.get()
    global num
    global math
    math="add"
    num=int(first)
    e.delete(0,END)

def clear():
    e.delete(0,END)

def equal():
    second=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,num+int(second))
    if math=="sub":
        e.insert(0,num-int(second))
    if math=="multi":
        e.insert(0,num*int(second))
    if math=="div":
        e.insert(0,num/int(second))

def sub():
    first=e.get()
    global num
    global math
    math="sub"
    num=int(first)
    e.delete(0,END)

def multi():
    first=e.get()
    global num
    global math
    math="multi"
    num=int(first)
    e.delete(0,END)

def div():
    first=e.get()
    global num
    global math
    math="div"
    num=int(first)
    e.delete(0,END)

button_1=Button(window,text="1",padx=30,pady=10,command=lambda: button(1))
button_2=Button(window,text="2",padx=30,pady=10,command=lambda: button(2))
button_3=Button(window,text="3",padx=30,pady=10,command=lambda: button(3))
button_4=Button(window,text="4",padx=30,pady=10,command=lambda: button(4))
button_5=Button(window,text="5",padx=30,pady=10,command=lambda: button(5))
button_6=Button(window,text="6",padx=30,pady=10,command=lambda: button(6))
button_7=Button(window,text="7",padx=30,pady=10,command=lambda: button(7))
button_8=Button(window,text="8",padx=30,pady=10,command=lambda: button(8))
button_9=Button(window,text="9",padx=30,pady=10,command=lambda: button(9))
button_0=Button(window,text="0",padx=30,pady=10,command=lambda: button(0))
button_add=Button(window,text="+",padx=30,pady=10,command=add)
button_clear=Button(window,text="Clear",padx=57,pady=10,command=clear)
button_equal=Button(window,text="=",padx=30,pady=31,command=equal)
button_sub=Button(window,text="-",padx=30,pady=10,command=sub)
button_multi=Button(window,text="x",padx=30,pady=10,command=multi)
button_div=Button(window,text="/",padx=30,pady=10,command=div)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_0.grid(row=4,column=0)
button_clear.grid(row=6,column=1,columnspan=2)
button_add.grid(row=4,column=1)
button_equal.grid(row=5,column=0,rowspan=2)
button_sub.grid(row=4,column=2)
button_multi.grid(row=5,column=1)
button_div.grid(row=5,column=2)

window.mainloop()