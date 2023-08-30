from tkinter import *
from tkinter import ttk
from tkinter import simpledialog , messagebox
from PIL import Image , ImageTk
import requests
from io import BytesIO


main_window = Tk()
main_window.title("To-do List by Pappu")
main_window.geometry("500x300")
main_window.resizable(False , False)
main_window.configure(bg="light blue")



get_icon = requests.get("https://imgtr.ee/images/2023/08/30/2a14b6ec98835c0a8667dc11e7a232af.png").content
icon = Image.open(BytesIO(get_icon))
icon_img = ImageTk.PhotoImage(icon)

main_window.iconphoto(True , icon_img)



text = StringVar()

def add_box():
    item = entry1.get()
    if item:
        list1.insert(END, "-> "+str(item))
        entry1.delete(0,END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")



def del_box():
    if list1.curselection():
        list1.delete(list1.curselection())


def del_all():
    list1.delete(0,END)



def check_mark():
    sel_txt = list1.curselection()
    item_index = list1.index(sel_txt)
    list_item = str(list1.get(item_index))


    if sel_txt:
        if (" -Done" in list_item):
            messagebox.showwarning("Warning", "Task Already Marked")
        else:
            list1.delete(item_index)
            new = list_item + " -Done"
            list1.insert(item_index, new)



entry1 = Entry(main_window , textvariable = text ,highlightbackground="blue")
entry1.configure(background="light grey" , foreground= "dark green" )
entry1.place(x= 30 , y=30)


style = ttk.Style()

style.configure("TButton", borderwidth=5, background="magenta")
style.map("TButton", background=[('pressed', 'black'), ('active', 'white')] , foreground=[('pressed', 'red'), ('active', 'blue')])


button1 = ttk.Button(main_window, text="Add" , command= lambda : add_box(), style="TButton")
button1.place(x = 200 , y=20)

button2 = ttk.Button(main_window, text="Delete",command= lambda : del_box() ,style="TButton")
button2.place(x = 200 , y =100)

button3 = ttk.Button(main_window, text="Marked",command= lambda: check_mark(), style="TButton")
button3.place(x = 200 , y =180)

button4 = ttk.Button(main_window, text="Delete All", command = lambda : del_all() , style="TButton")
button4.place(x = 200 , y =260)

list1 = Listbox(main_window)
list1.configure(bg="light green", foreground="blue")
list1.place(x = 320 , y =20)


main_window.mainloop()

