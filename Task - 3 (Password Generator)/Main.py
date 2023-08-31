from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image , ImageTk
import requests
from io import BytesIO



main_window = Tk()
main_window.title("Password Generator by Pappu")
main_window.config(background="light pink")
main_window.geometry("490x410")
main_window.resizable(False,False)


get_icon = requests.get("https://imgtr.ee/images/2023/08/30/2a14b6ec98835c0a8667dc11e7a232af.png").content
icon = Image.open(BytesIO(get_icon))
icon_img = ImageTk.PhotoImage(icon)

main_window.iconphoto(True , icon_img)




main_window.mainloop()