from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image , ImageTk
import requests
from io import BytesIO


# setting up main Canvas

main_canvas = Tk()
main_canvas.title("CodSoft Calculator by Pappu Manna")
main_canvas.config(background="magenta")
main_canvas.geometry("490x410")
main_canvas.resizable(False,False)




# Creating Lines 

canvas = Canvas(main_canvas, width=470, height=390 , bg="pink" , highlightthickness=0)
canvas.place(x=10 ,y= 10)
line = canvas.create_line(10,305,450,305, fill="blue", width=2)
line2 = canvas.create_line(367,80,367,375, fill="blue", width=2)


# Setting up Window Icon

get_calc_icon = requests.get("https://cdn-icons-png.flaticon.com/128/2995/2995909.png").content
calc_icon = Image.open(BytesIO(get_calc_icon))
icon_img = ImageTk.PhotoImage(calc_icon)

main_canvas.iconphoto(True , icon_img)

z = ""  


# Calculaotr Funtioncs

def update(x):
    global z
    z += x
    eqn.set(z)



def solve():
    global z
    eqn.set(eval(z))
    z = str(eval(z))


def backspace():
    global z
    z = z[:-1]
    eqn.set(z)



def clear_all():
    global z
    z = ""
    eqn.set(z)





# Font and size of the texts

eqn = StringVar()

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=20 , weight="bold" , family="Consolas")


Label1 = Label(main_canvas , highlightthickness=2 , textvariable = eqn )
Label1.config(highlightcolor="green" , highlightbackground= "red" , width=60 )
Label1.pack(padx=20 ,pady=20 )



# BUttons Configuratino

style = ttk.Style()


style.configure("TButton", borderwidth=10, padding=8, relief="sunken", background="magenta")
style.map("TButton", background=[('pressed', 'black'), ('active', 'white')] , foreground=[('pressed', 'red'), ('active', 'blue')])



style.configure("C.TButton", borderwidth=10, padding=8, relief="sunken", background="red")
style.map("C.TButton", background=[('pressed', 'black'), ('active', 'white')] , foreground=[('pressed', 'red'), ('active', 'blue')])


style.configure("Default.TButton", borderwidth=10, padding=8, relief="sunken", background="dark green")
style.map("C.TButton", background=[('pressed', 'black'), ('active', 'white')] , foreground=[('pressed', 'red'), ('active', 'blue')])




# Numeric Buttons

b1 = ttk.Button(main_canvas , text="1",  command= lambda : update("1") , width = 4  , style="TButton" )
b1.place(x=20 , y=90)

b2 = ttk.Button(main_canvas , text="2" , command= lambda : update("2") , width = 4 , style="TButton")
b2.place(x=110 , y=90)

b3 = ttk.Button(main_canvas , text="3" , command= lambda : update("3"), width = 4 ,  style="TButton")
b3.place(x=200 , y=90)

b4 = ttk.Button(main_canvas , text="4" , command= lambda : update("4"), width = 4 ,  style="TButton")
b4.place(x=290 , y=90)

b5 = ttk.Button(main_canvas , text="5" , command= lambda : update("5"), width = 4 ,  style="TButton")
b5.place(x=20 , y=170)

b6 = ttk.Button(main_canvas , text="6" , command= lambda : update("6"), width = 4 ,  style="TButton")
b6.place(x=110 , y=170)

b7 = ttk.Button(main_canvas , text="7" , command= lambda : update("7"), width = 4 ,  style="TButton")
b7.place(x=200 , y=170)

b8 = ttk.Button(main_canvas , text="8" , command= lambda : update("8"), width = 4 ,  style="TButton")
b8.place(x=290 , y=170)

b9 = ttk.Button(main_canvas , text="9" , command= lambda : update("9"), width = 4 ,  style="TButton")
b9.place(x=110 , y=250)

b10 = ttk.Button(main_canvas , text="0" , command= lambda : update("0"), width = 4 ,  style="TButton")
b10.place(x=200 , y=250)

b11 =ttk.Button(main_canvas , text="00" , command= lambda : update("00"), width = 4 ,  style="TButton")
b11.place(x=20 , y=250)


# Decimal Button

b12 = ttk.Button(main_canvas , text="." , command= lambda :update("."), width = 4 ,  style="TButton")
b12.place(x=290 , y=250)


# basic Operators BUttons

b13 = ttk.Button(main_canvas , text="+" , command= lambda : update("+"), width = 4 ,  style="C.TButton")
b13.place(x=20 , y=330)


b14 = ttk.Button(main_canvas , text="-" , command= lambda : update("-"), width = 4 ,  style="C.TButton")
b14.place(x=110 , y=330)


b15 = ttk.Button(main_canvas , text="x" , command= lambda : update("*"), width = 4 ,  style="C.TButton")
b15.place(x=200 , y=330)


b16 = ttk.Button(main_canvas , text="÷" , command= lambda : update("/"), width = 4 ,  style="C.TButton")
b16.place(x=290 , y=330)


b19 = ttk.Button(main_canvas , text="%" , command= lambda : update("%"), width = 4 ,  style="C.TButton")
b19.place(x=380 , y=250)



# clear All button

b16 = ttk.Button(main_canvas , text="C" , command= lambda : clear_all(), width = 4 ,  style="C.TButton")
b16.place(x=380 , y=170)


# Solve Button

b18 = ttk.Button(main_canvas , text="=" , command= lambda : solve(), width = 4 ,  style="Default.TButton")
b18.place(x=380 , y=330)


# Backspace Button


get_bksp_icon = requests.get("https://imgtr.ee/images/2023/08/30/edd9aa67ab6954290cc90eb635c9cfb1.png").content
bksp_icon = Image.open(BytesIO(get_bksp_icon))
bksp_img = ImageTk.PhotoImage(bksp_icon)


b17 = ttk.Button(main_canvas , text="" , command= lambda : backspace() ,  style="C.TButton" , image=bksp_img)
b17.place(x=380 , y=90)



messagebox.showinfo("Message!", "Please make sure you have Internet Connection!")

main_canvas.mainloop()
