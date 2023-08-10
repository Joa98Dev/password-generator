#Importing Libraries
from tkinter import *
from random import randint

#GUI
root = Tk()
root.title("Password Generator")
root.geometry("500x300")
root.resizable(0,0)

#Set icon path
icon_path = "icon.ico"
root.iconbitmap(icon_path)

#Function that generate random passwords
def new_rand():
    #Clears the entry before generating a new password
    password_entry.delete(0, END)
    #Determine the length of the password and convert any value into an integer
    password_lenght = int(my_entry.get())
    #Stored the created password
    my_password = ''
    #Iterates the password_lenght a number of times, depending of the lenght specified by the user
    for i in range(password_lenght):
        my_password = chr(randint(33,126))
        password_entry.insert(0, my_password)

#Function that copy the password generated into the OS clipboard
def clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())

#Make a Tkinter widget and sets its title
label_frame = LabelFrame(root, text="Password Lenght")
label_frame.pack(pady=20)

#Make a text input field and specified its font
my_entry = Entry(label_frame, font=("Roboto", 24))
my_entry.pack(pady=20, padx=20)

#Create a stylized input field, background color and font
password_entry = Entry(root, text='', font=("Roboto", 24), bd=0, bg="systembuttonface")
password_entry.pack(pady=20)

#Container widget to maintian organized other widgets
my_frame = Frame(root)
my_frame.pack(pady=20)

#Create a button to copy the generated password into the OS clipboard
copy_button = Button(my_frame, text="Copy Password", command=clipboard)
copy_button.grid(row=0, column=1, padx=10)

#Create a button to generate a random password
password_button = Button(my_frame, text="Generate Password", command=new_rand)
password_button.grid(row=0, column=0, padx=10)

#Tkinter event loop
root.mainloop()