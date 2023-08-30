
# Importing all the functions

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image , ImageTk
import requests
from io import BytesIO



# setting up main Canvas

main_window = Tk()
main_window.title("Calculator by Pappu")
main_window.config(background="magenta")
main_window.geometry("490x410")
main_window.resizable(False,False)


# Creating Lines 

canvas = Canvas(main_window, width=470, height=390 , bg="pink" , highlightthickness=0)
canvas.place(x=10 ,y= 10)
line = canvas.create_line(10,305,450,305, fill="blue", width=2)
line2 = canvas.create_line(367,80,367,375, fill="blue", width=2)


# Setting up Window Icon

# getting icon from www.flaticon.com

get_calc_icon = requests.get("https://cdn-icons-png.flaticon.com/128/2995/2995909.png").content
calc_icon = Image.open(BytesIO(get_calc_icon))
icon_img = ImageTk.PhotoImage(calc_icon)

main_window.iconphoto(True , icon_img)



# global variable that will get updated and set on the label

z = ""




# Calculaotr Funtioncs

# update() is called when a numeric or decimal button is clicked

def update(x):
    global z
    z += x
    eqn.set(z)


# solve() is called when "=" button is clicked to solve the equation using eval()

def solve():
    try:
        global z
        eqn.set(eval(z))
        z = str(eval(z))
    except:
        messagebox.showwarning("Error" , "Division by zero NOT possible")
        z = ""
        eqn.set(z)


# backspace() is called when backspace button is pressed to erase the last character

def backspace():
    global z
    z = z[:-1]
    eqn.set(z)


# clear_all() is called when "C" button is pressed to erase all the characters in the label

def clear_all():
    global z
    z = ""
    eqn.set(z)





# Font and size of the texts

eqn = StringVar()

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=20 , weight="bold" , family="Consolas")


# creating main equation label i.e. needed to be solved

Label1 = Label(main_window , highlightthickness=2 , textvariable = eqn )
Label1.config(highlightcolor="green" , highlightbackground= "red" , width=60 )
Label1.pack(padx=20 ,pady=20 )



# BUttons Configuratino

style = ttk.Style()


# Number Buttons configuration

style.configure("TButton", borderwidth=10, padding=8, relief="sunken", background="magenta")
style.map("TButton", background=[('pressed', 'black'), ('active', 'white')] , foreground=[('pressed', 'red'), ('active', 'blue')])


# Operator Buttons Configuration

style.configure("C.TButton", borderwidth=10, padding=8, relief="sunken", background="red")
style.map("C.TButton", background=[('pressed', 'black'), ('active', 'white')] , foreground=[('pressed', 'red'), ('active', 'blue')])


style.configure("Default.TButton", borderwidth=10, padding=8, relief="sunken", background="dark green")
style.map("C.TButton", background=[('pressed', 'black'), ('active', 'white')] , foreground=[('pressed', 'red'), ('active', 'blue')])




# Numeric Buttons

b1 = ttk.Button(main_window , text="1",  command= lambda : update("1") , width = 4  , style="TButton" ).place(x=20 , y=90)

b2 = ttk.Button(main_window , text="2" , command= lambda : update("2") , width = 4 , style="TButton").place(x=110 , y=90)

b3 = ttk.Button(main_window , text="3" , command= lambda : update("3"), width = 4 ,  style="TButton").place(x=200 , y=90)

b4 = ttk.Button(main_window , text="4" , command= lambda : update("4"), width = 4 ,  style="TButton").place(x=290 , y=90)

b5 = ttk.Button(main_window , text="5" , command= lambda : update("5"), width = 4 ,  style="TButton").place(x=20 , y=170)

b6 = ttk.Button(main_window , text="6" , command= lambda : update("6"), width = 4 ,  style="TButton").place(x=110 , y=170)

b7 = ttk.Button(main_window , text="7" , command= lambda : update("7"), width = 4 ,  style="TButton").place(x=200 , y=170)

b8 = ttk.Button(main_window , text="8" , command= lambda : update("8"), width = 4 ,  style="TButton").place(x=290 , y=170)

b9 = ttk.Button(main_window , text="9" , command= lambda : update("9"), width = 4 ,  style="TButton").place(x=110 , y=250)

b10 = ttk.Button(main_window , text="0" , command= lambda : update("0"), width = 4 ,  style="TButton").place(x=200 , y=250)

b11 =ttk.Button(main_window , text="00" , command= lambda : update("00"), width = 4 ,  style="TButton").place(x=20 , y=250)




# Decimal Button

b12 = ttk.Button(main_window , text="." , command= lambda :update("."), width = 4 ,  style="TButton")
b12.place(x=290 , y=250)




# basic Operators BUttons

b13 = ttk.Button(main_window , text="+" , command= lambda : update("+"), width = 4 ,  style="C.TButton").place(x=20 , y=330)


b14 = ttk.Button(main_window , text="-" , command= lambda : update("-"), width = 4 ,  style="C.TButton").place(x=110 , y=330)


b15 = ttk.Button(main_window , text="x" , command= lambda : update("*"), width = 4 ,  style="C.TButton").place(x=200 , y=330)


b16 = ttk.Button(main_window , text="÷" , command= lambda : update("/"), width = 4 ,  style="C.TButton").place(x=290 , y=330)


b19 = ttk.Button(main_window , text="%" , command= lambda : update("%"), width = 4 ,  style="C.TButton").place(x=380 , y=250)




# clear All button

b16 = ttk.Button(main_window , text="C" , command= lambda : clear_all(), width = 4 ,  style="C.TButton").place(x=380 , y=170)




# Solve Button

b18 = ttk.Button(main_window , text="=" , command= lambda : solve(), width = 4 ,  style="Default.TButton").place(x=380 , y=330)




# Backspace Button

get_bksp_icon = requests.get("https://imgtr.ee/images/2023/08/30/edd9aa67ab6954290cc90eb635c9cfb1.png").content
bksp_icon = Image.open(BytesIO(get_bksp_icon))
bksp_img = ImageTk.PhotoImage(bksp_icon)

b17 = ttk.Button(main_window , text="" , command= lambda : backspace() ,  style="C.TButton" , image=bksp_img).place(x=380 , y=90)


# messagebox is used 

messagebox.showinfo("Message!", "Please make sure you have Internet Connection!")

main_window.mainloop()
