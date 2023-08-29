from tkinter import *
import tkinter.font as tkFont


main_canvas = Tk()
main_canvas.title("------CodSoft Calculator------")
main_canvas.config(background="black")
main_canvas.geometry("390x500")
main_canvas.resizable(False,False)
icon_img = PhotoImage(file= "C:\\Users\\Pappy\\OneDrive\\Documents\\Codsoft\\CODSOFTJUNE\\Task1 (Calculator)\\calculator_icon.png")
main_canvas.iconphoto(True , icon_img)

z = ""  

def update(x):
    global z
    z += x
    eqn.set(z)

    

eqn = StringVar()

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=20 , weight="bold" , family="Consolas")


Label1 = Label(main_canvas , highlightthickness=2 , textvariable = eqn )
Label1.config(highlightcolor="green" , highlightbackground= "red")
Label1.pack(padx=20 ,pady=20)

b1 = Button(main_canvas , text="1",  command= lambda : update("1") , width = 4 , bg="orange" )
b1.place(x=20 , y=90)

b2 = Button(main_canvas , text="2" , command= lambda : update("2") , width = 4 , bg="orange")
b2.place(x=110 , y=90)

b3 = Button(main_canvas , text="3" , command= lambda : update("3"), width = 4 ,  bg="orange")
b3.place(x=200 , y=90)

b4 = Button(main_canvas , text="4" , command= lambda : update("4"), width = 4 ,  bg="orange")
b4.place(x=290 , y=90)

b5 = Button(main_canvas , text="5" , command= lambda : update("5"), width = 4 ,  bg="orange")
b5.place(x=20 , y=170)

b6 = Button(main_canvas , text="6" , command= lambda : update("6"), width = 4 ,  bg="orange")
b6.place(x=110 , y=170)

b7 = Button(main_canvas , text="7" , command= lambda : update("7"), width = 4 ,  bg="orange")
b7.place(x=200 , y=170)

b8 = Button(main_canvas , text="8" , command= lambda : update("8"), width = 4 ,  bg="orange")
b8.place(x=290 , y=170)

b9 = Button(main_canvas , text="9" , command= lambda : update("9"), width = 4 ,  bg="orange")
b9.place(x=110 , y=250)

b10 = Button(main_canvas , text="0" , command= lambda : update("0"), width = 4 ,  bg="orange")
b10.place(x=200 , y=250)

main_canvas.mainloop()