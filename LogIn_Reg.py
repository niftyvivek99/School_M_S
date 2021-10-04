from tkinter import *
import os
from tkinter import messagebox
from Student_FrontEnd import *


def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.iconbitmap("C:/Users/97798/Downloads/logo.ico")
    screen3.geometry("150x100")
    messagebox.showinfo("Login", "Login Successful", parent=screen3)
    screen3.destroy()
    screen2.destroy()
    screen.destroy()

    root = Tk()
    obj = Std_info(root)
    root.mainloop()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.iconbitmap("C:/Users/97798/Downloads/logo.ico")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK").pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.iconbitmap("C:/Users/97798/Downloads/logo.ico")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK").pack()


def register_user():
    print("working")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.iconbitmap("C:/Users/97798/Downloads/logo.ico")
    screen1.geometry("400x350")
    Label(screen1, text="Please enter details below", bg='#99c2ff', width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen1, text="").pack()

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()


    Label(screen1, text="Username * ").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.iconbitmap("C:/Users/97798/Downloads/logo.ico")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login", bg='#99c2ff', width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password *").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("550x200")
    screen.title("Login Registration Page")
    screen.iconbitmap("C:/Users/97798/Downloads/logo.ico")
    Label(text="Login Registration Page", bg='#99c2ff', width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()





