from tkinter import *
from PIL import Image, ImageTk
import string
import random
import pyperclip

def generate_password():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_chars = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_var.get())

    if choice_var.get() == 1:
        generated_password = ''.join(random.sample(small_alphabets, password_length))
    elif choice_var.get() == 2:
        generated_password = ''.join(random.sample(small_alphabets + capital_alphabets, password_length))
    elif choice_var.get() == 3:
        generated_password = ''.join(random.sample(all_chars, password_length))

    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)

def copy_to_clipboard():
    password_to_copy = password_entry.get()
    pyperclip.copy(password_to_copy)

root = Tk()
root.title("Password Generator")
root.geometry("700x700")  

try:
    background_image = Image.open("1.png")
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    background_label.lower()  
except IOError as e:
    print(f"Error loading background image: {e}")

label_frame = Frame(root)
label_frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)


choice_var = IntVar()
length_var = IntVar(value=12)

font = ('Arial', 12, 'bold')

Label(label_frame, text='Password Generator', font=('Times New Roman', 20, 'bold')).pack(pady=10)
Label(label_frame, text='Select Complexity:', font=font).pack(pady=5)
Label(label_frame, text='Password Length:', font=font).pack(pady=5)

Radiobutton(label_frame, text='Weak', value=1, variable=choice_var, font=font).pack(pady=5)
Radiobutton(label_frame, text='Medium', value=2, variable=choice_var, font=font).pack(pady=5)
Radiobutton(label_frame, text='Strong', value=3, variable=choice_var, font=font).pack(pady=5)

Spinbox(label_frame, from_=5, to=18, textvariable=length_var, font=font, width=5).pack(pady=5)

Button(label_frame, text='Generate Password', font=font, command=generate_password).pack(pady=10)

password_entry = Entry(label_frame, width=25, bd=2, font=font)
password_entry.pack()

Button(label_frame, text='Copy to Clipboard', font=font, command=copy_to_clipboard).pack(pady=10)


root.mainloop()
