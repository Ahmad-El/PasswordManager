from tkinter import *
from tkinter import messagebox
import pyperclip
from password_generator import create_password
import json

IMAGE_PATE = "logo.png"
DATA_FILE = "data.json"
DEFAULT_LOGIN = "Your@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = create_password()
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# --------------------------- SEARCH PASSWORD ------------------------------ #
def find_password():
    website = website_input.get()
    try:
        with open(DATA_FILE, "r") as file:
            json_data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="No Data File Found")
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title=website, message="No details for the website exists.")

    else:
        if website in json_data:
            messagebox.showinfo(
                title=website,
                message=f"Website: {website}\nLogin: {json_data[website]['email']}\nPassword: {json_data[website]['password']}",
            )
            pyperclip.copy(json_data[website]["password"])

        else:
            messagebox.showinfo(
                title=website, message="No details for the website exists."
            )


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().strip()
    login = login_input.get().strip()
    password = password_input.get().strip()
    new_data = {
        website: {
            "email": login,
            "password": password,
        }
    }
    if len(login) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Empty Field", message="Please dont't leave any fields empty!"
        )
        return
    yes_no = messagebox.askokcancel(
        title=website, message=f"Your login: {login}.\nYour password: {password}\nsave?"
    )
    if not yes_no:
        return

    try:
        with open(DATA_FILE, "r") as file:
            json_data = json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        json_data = new_data
    else:
        json_data.update(new_data)
    finally:
        with open(DATA_FILE, "w") as file:
            json.dump(json_data, file, indent=4)

    website_input.delete(0, END)
    login_input.delete(0, END)
    login_input.insert(0, DEFAULT_LOGIN)
    generate_password()
    website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)


image = PhotoImage(file=IMAGE_PATE)
canvas = Canvas(window, width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)


# Label
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_username_or_email = Label(text="Email/Username:")
label_username_or_email.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Entry
website_input = Entry(width=20)
website_input.focus()
website_input.grid(row=1, column=1)

login_input = Entry(width=35)
login_input.insert(END, DEFAULT_LOGIN)
login_input.grid(row=2, column=1, columnspan=2)
password_input = Entry(width=20)
password_input.grid(row=3, column=1)


# Button
generate_button = Button(text="Generate", width=11, command=generate_password)
generate_password()
generate_button.grid(row=3, column=2)
add_button = Button(text="add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()
