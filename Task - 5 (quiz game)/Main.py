from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image , ImageTk
import requests
from io import BytesIO


main_window = Tk()
main_window.title("Quiz Game")
main_window.config(background="black" )
main_window.geometry("1280x720")
main_window.resizable(False,False)



default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=15 , weight="bold" , family="Consolas")



get_icon = requests.get("https://cdn-icons-png.flaticon.com/128/3261/3261308.png").content
icon = Image.open(BytesIO(get_icon))
icon_img = ImageTk.PhotoImage(icon)

main_window.iconphoto(True , icon_img)



canvas = Canvas(main_window, width=1280, height=720 , borderwidth=-5 , bd=0)
canvas.pack()

get_banner = requests.get("https://imgtr.ee/images/2023/08/30/a2dd5787e01aee2d7938b3066fc1faec.png").content
banner = Image.open(BytesIO(get_banner))
banner_img = ImageTk.PhotoImage(banner)


canvas.create_image(640, 360, image=banner_img)

# canvas.attributes('-alpha',0.7)


total_score = 0

def next_question(button):
    desc_Label.config(text="")
    q_Label.config(text = "what is maths ??")
    button




questions = StringVar()

desc_Label = Label(canvas , foreground="#02f2ea" ,background="black",text = "You will be given 10 questions related to space choose the correct option to get one point")
desc_Label.place(x = 145 , y = 360)


start_but = ttk.Button(canvas , width=10 , text="Start !" , command=lambda: next_question(start_but) )
start_but.place(x = 600 , y = 500)

q_Label = Label(canvas , text = "" , background="black" , foreground="#02f2ea")
q_Label.place(x = 600 , y = 360)
















main_window.mainloop()