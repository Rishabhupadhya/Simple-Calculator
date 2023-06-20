from tkinter import *

def get_digit(digit):
    current = result_label["text"]
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text=' ')

def get_operator(op):
     global first_number,operator
     first_number = int(result_label['text'])
     operator = op
     result_label.config(text='')

def get_result():
    global first_number,second_number,operator
    
    second_number = int(result_label["text"])

    if operator == "+":
        result_label.config(text=str(first_number + second_number))
    elif operator == "-":
        result_label.config(text=str(first_number - second_number))
    elif operator == "*":
        result_label.config(text=str(first_number * second_number))
    elif operator == "/":
        if second_number == 0:
            result_label.config(text="Error")
        else:
            result_label.config(text=str(first_number / second_number))
        



root = Tk()
root.title("Calculator")
root.geometry("380x300")
root.resizable(False,False)
root.configure(bg="white")

val =" "
text_input = StringVar()

result_label = Label(root,text="",bg="white",fg="black",font=("arial",30,"bold"),anchor="e",justify="right")
result_label.grid(row=0,column=0,columnspan=10)
Button7 = Button(root,text="7",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :get_digit(7))
Button7.grid(row=1,column=1)

Button8 = Button(root,text="8",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :get_digit(8))
Button8.grid(row=1,column=2)

Button9 = Button(root,text="9",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :get_digit(9))
Button9.grid(row=1,column=3)

Button4 = Button(root,text="4",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :get_digit(4))
Button4.grid(row=2,column=1)

Button5 = Button(root,text="5",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :get_digit(5))
Button5.grid(row=2,column=2)

Button6 = Button(root,text="6",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :get_digit(6))
Button6.grid(row=2,column=3)

Button1 = Button(root,text="1",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :get_digit(1))
Button1.grid(row=3,column=1)

Button2 = Button(root,text="2",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :get_digit(2))
Button2.grid(row=3,column=2)

Button3 = Button(root,text="3",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :get_digit(3))
Button3.grid(row=3,column=3)

Button0 = Button(root,text="0",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :get_digit(0))
Button0.grid(row=4,column=2)

Buttonc = Button(root,text="C",font=("arial",12,"bold"),bd=12,width=6,height=2,command=lambda :clear())
Buttonc.grid(row=4,column=1)

Buttonequal = Button(root,text="=",font=("arial",12,"bold"),bd=12,width=6,height=2,command=get_result)
Buttonequal.grid(row=4,column=3)

Buttonplus = Button(root,text="+",font=("arial",12,"bold"),bd=12,width=6,height=2,command= lambda: get_operator("+"))
Buttonplus.grid(row=1,column=4)

Buttonminus = Button(root,text="-",font=("arial",12,"bold"),bd=12,width=6,height=2,command= lambda: get_operator("-"))
Buttonminus.grid(row=2,column=4)

Buttonmultiply = Button(root,text="*",font=("arial",12,"bold"),bd=12,width=6,height=2,command= lambda: get_operator("*"))
Buttonmultiply.grid(row=3,column=4)

Buttondivide = Button(root,text="/",font=("arial",12,"bold"),bd=12,width=6,height=2,command= lambda: get_operator("/"))
Buttondivide.grid(row=4,column=4)

root.mainloop()