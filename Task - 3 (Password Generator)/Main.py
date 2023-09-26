import tkinter as tk
import string
import random as rand

def generate_pass():
    
    pass_length = int(pass_len.get())
    
    alphabets = list(string.ascii_lowercase + string.ascii_uppercase)
    numbers = [str(i) for i in range(10)]
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', ',', '.', '<', '>', '/', '?', '`', '~']

    all_char = alphabets+numbers+special_characters

    password_list = rand.sample(all_char , pass_length)

    password = ""

    for i in range(len(password_list)):
        password += password_list[i]
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    lab1.config(text="  Now copy the password  ")
    


if __name__ == "__main__":

    main_window = tk.Tk()
    main_window.title("Password Generator by Pappu")
    main_window.config(background="light blue")
    main_window.geometry("400x300")
    main_window.resizable(False,False)

    lab1 = tk.Label(main_window, text="Enter Password Length Below",background="light blue")
    lab1.pack(padx=20, pady=20)

    # getting password length
    pass_len = tk.Entry(main_window)
    pass_len.pack(padx=20, pady=20)

    # BUtton for password generation
    gen_but = tk.Button(main_window, text="Generate Password", command=generate_pass)
    gen_but.pack(padx=20, pady=20)

    # displaying the generated password
    password_entry = tk.Entry(main_window)
    password_entry.pack(padx=20, pady=20)
    

    main_window.mainloop()
