from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image , ImageTk
import random

questions =[
    ["What is the largest planet in our solar system?", "Mars", "Jupiter", "Saturn", "Venus", 2],
    ["Which famous space telescope was launched in 1990?", "Hubble Space Telescope", "Kepler Space Telescope", "Chandra X-ray Observatory", "Spitzer Space Telescope", 1],
    ["What is the name of the first artificial satellite launched into Earth's orbit?", "Voyager 1", "Apollo 11", "Sputnik 1", "Cassini", 3],
    ["Which galaxy is part of the Local Group and is the closest to the Milky Way?", "Andromeda Galaxy", "Triangulum Galaxy", "Whirlpool Galaxy", "Sombrero Galaxy", 1],
    ["What phenomenon occurs when a star collapses under gravity, resulting in an incredibly dense object?", "Supernova", "Black Hole", "Neutron Star", "White Dwarf", 2]
]

random.shuffle(questions)

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

# get_banner = requests.get("https://imgtr.ee/images/2023/08/30/a2dd5787e01aee2d7938b3066fc1faec.png").content
# banner = Image.open(fi)
banner_img = ImageTk.PhotoImage(file="C:\Users\Pappy\OneDrive\Documents\Codsoft\CODSOFTJUNE\Task - 5 (quiz game)\Quiz Game.png")


canvas.create_image(640, 360, image=banner_img)

# canvas.attributes('-alpha',0.7)


total_score = 0

def next_question(button):
    desc_Label.config(text="")
    q_Label.config(text = questions[i])
    button




questions = StringVar()

desc_Label = Label(canvas , foreground="#02f2ea" ,background="black",text = "You will be given 10 questions related to space choose the correct option to get one point")
desc_Label.place(x = 145 , y = 360)


start_but = ttk.Button(canvas , width=10 , text="Start !" , command=lambda: next_question(start_but) )
start_but.place(x = 600 , y = 500)

q_Label = Label(canvas , text = "" , background="black" , foreground="#02f2ea")
q_Label.place(x = 600 , y = 360)








main_window.mainloop()