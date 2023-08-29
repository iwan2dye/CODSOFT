import tkinter as tk

if __name__ == "__main__":
    main_canvas = tk.Tk()
    main_canvas.title("Calculator !!")
    main_canvas.config(background="black" , width= 400 , height= 400)
    text_box = tk.Text(main_canvas, wrap="word" , background= "grey" , )
    text_box.pack()
    # text_box.insert("1.0" , "LOL")
    
    
    
    
    main_canvas.mainloop()