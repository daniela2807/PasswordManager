from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or password == "":
        messagebox.showerror(title="Error",message="Please dont leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Title", message=f"These are the details entered: \n Email: {email} \n Password: {password} \n Is it ok to save? ")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{website} | {email} | {password} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            f.close()





# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
filename = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=filename)
canvas.grid(row=0, column=1)

#-----------WebSite-----------

website_label = Label(text="Website: ", font=("Arial",13))
website_label.grid(row=1, column=0)

website_entry = Entry()
website_entry.focus()
website_entry.grid(row=1, column=1,columnspan=2, sticky="EW")

#-----------Email-----------
email_label = Label(text="Email/Username: ", font=("Arial",13))
email_label.grid(row=2, column=0)

email_entry = Entry()
email_entry.insert(0,"angela@gmail.com")

email_entry.grid(row=2, column=1,columnspan=2, sticky="EW")

#-----------Password-----------

password_label = Label(text="Password: ", font=("Arial",13))
password_label.grid(row=3, column=0)

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

#-----------Buttons----------------

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save_data)
add_button.grid(row=4,column=1,columnspan=2, sticky="EW")


window.mainloop()