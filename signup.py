# Imports
import sqlite3
from pathlib import Path
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import re

# Paths set for assets and outputs
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/anishkashahane/Desktop/signup")


# Function to retrieve the path to an asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Function which centers the window on the screen on the user-interface
def center_window(window, width, height):
    # Get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Window geometry is set to the calculated position
    window.geometry(f'{width}x{height}+{x}+{y}')


# Function which validate password requirements,
# this includes password length and at least on numerical value in user password
def validate_password(password):
    # Password is checked to validate that the password is more than 6 characters long
    if len(password) <= 6:
        return False, 'Password must be more than 6 characters long'
    # Password is checked to validate the user password contains at least one number
    if not re.search(r'\d', password):
        return False, 'Password must contain at least one number'
    return True, ''


# Function which validate email format which user has entered into the entry box
def validate_email(email):
    # Validates whether user email entered contains '@' and '.'
    if '@' not in email or '.' not in email:
        return False, 'Invalid email'
    return True, ''


# Function which handle the signup process for users
def main():
    # Get input from entry widgets
    name = entry_name.get()
    lastname = entry_lastname.get()
    email = entry_email.get()
    username = entry_username.get()
    password = entry_password.get()
    re_password = entry_repassword.get()

    # Validates if all entry fields are not empty
    if name != '' and lastname != '' and email != '' and username != '' and password != '' and re_password != '':
        # Check if the username already exists in the database
        cursor.execute('SELECT username FROM users WHERE username=?', (username,))
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', 'Username already exists')
        elif password != re_password:
            messagebox.showerror('Error', 'Your passwords do not match')
        else:
            # Validation of email and password
            is_valid_email, message_email = validate_email(email)
            is_valid_password, message_password = validate_password(password)
            if not is_valid_email:
                messagebox.showerror('Error', message_email)
            elif not is_valid_password:
                messagebox.showerror('Error', message_password)
            else:
                # New user is entered into the database
                cursor.execute('INSERT INTO users (name, username, password, email, lastname) VALUES (?, ?, ?, ?, ?)',
                               (name, username, password, email, lastname))
                conn.commit()
                messagebox.showinfo('Success', 'You have successfully signed up. Please login.')
                window.destroy()  # Signup window is closed
    else:
        messagebox.showerror('Error', 'Please fill out all fields')


# Dimensions of the window set
window_width = 636
window_height = 679

# Initialize signup_window
window = Tk()
window.title("DINE-EZ")
window.geometry("636x679")
window.configure(bg="#FFFFFF")
center_window(window, window_width, window_height)

# Canvas to hold the user-interface elements for the window
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=679,
    width=636,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Set up the SQLite connection with database
conn = sqlite3.connect("restaurants.db")
cursor = conn.cursor()

# Table is created the table it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    lastname TEXT NOT NULL
)
''')


# Placement of labels,buttons and entry widgets on the canvas for user navigation and user input on the user-interface
image_image_logo = PhotoImage(
    file=relative_to_assets("logo.png"))
image_1 = canvas.create_image(
    315.0,
    72.0,
    image=image_image_logo
)

# Text labels on UI for user navigation
# Text label for "USERNAME:"
canvas.create_text(165.0, 366.0, anchor="nw", text="USERNAME:", fill="#000000", font=("Inter ExtraLightItalic", 15))
# Text label for "SIGNUP:"
canvas.create_text(264.0, 106.0, anchor="nw", text="SIGN UP", fill="#000000", font=("Inter ExtraLightItalic", 20))
# Text label for "EMAIL:"
canvas.create_text(165.0, 293.0, anchor="nw", text="EMAIL:", fill="#000000", font=("Inter ExtraLightItalic", 15))
# Text label for "PASSWORD:"
canvas.create_text(165.0, 439.0, anchor="nw",text="PASSWORD ( Must contain at-least 6 \n characters & 1 numeric ) :",
                   fill="#000000", font=("Inter ExtraLightItalic", 15))
# Text label for "RE-TYPE PASSWORD:"
canvas.create_text(165.0, 536.0, anchor="nw", text="RE-TYPE PASSWORD:",
                   fill="#000000", font=("Inter ExtraLightItalic", 15))
# Text label for "FIRST NAME:"
canvas.create_text(165.0, 138.0, anchor="nw", text="FIRST NAME:", fill="#000000",
                   font=("Inter ExtraLightItalic", 15))
# Text label for "LAST NAME:"
canvas.create_text(165.0, 217.0, anchor="nw", text="LAST NAME:",
                   fill="#000000", font=("Inter ExtraLightItalic", 15))

# First name user entry
entry_name_image_1 = PhotoImage(file=relative_to_assets("entry.png"))
entry_bg_1 = canvas.create_image(308.0, 184.0, image=entry_name_image_1)

entry_name = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0)
entry_name.place(x=180.0, y=159.0, width=256.0, height=48.0)

# Lastname user entry
entry_lastname_image_2 = PhotoImage(file=relative_to_assets("entry.png"))
entry_bg_2 = canvas.create_image(308.0, 265.0, image=entry_lastname_image_2)
entry_lastname = Entry(bd=0, bg="#F6F6F5", fg="#000716",highlightthickness=0)
entry_lastname.place(x=180.0, y=240.0, width=256.0, height=48.0)

# Email user entry
entry_email_image_3 = PhotoImage(file=relative_to_assets("entry.png"))
entry_bg_3 = canvas.create_image(308.0, 336.0, image=entry_email_image_3)
entry_email = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0)
entry_email.place(x=180.0, y=311.0, width=256.0, height=48.0)

# Username user entry
entry_username_image_4 = PhotoImage(file=relative_to_assets("entry.png"))
entry_bg_4 = canvas.create_image(308.0, 409.0, image=entry_username_image_4)
entry_username = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0)
entry_username.place(x=180.0, y=384.0, width=256.0, height=48.0)

# Password user entry
entry_password_image_5 = PhotoImage(file=relative_to_assets("entry.png"))
entry_bg_5 = canvas.create_image(308.0, 501.0, image=entry_password_image_5)
entry_password = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0,show="*")
entry_password.place(x=180.0, y=476.0, width=256.0, height=48.0)

# Re-entry password user entry
entry_repassword_image = PhotoImage(file=relative_to_assets("entry.png"))
entry_bg_6 = canvas.create_image(308.0,582.0, image=entry_repassword_image)
entry_repassword = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0, show="*")
entry_repassword.place(x=180.0,y=557.0, width=256.0, height=48.0)

# Submit button
button_image_submit = PhotoImage(file=relative_to_assets("submit.png"))
submit = Button(image=button_image_submit, borderwidth=0, highlightthickness=0,
                command=lambda: main(), relief="flat"  # Sign up function is called when submit button is clicked
)
submit.place(x=234.0, y=622.0, width=166.0, height=49.0)

# Disable window resizing on user interface
window.resizable(False, False)
# Start the Tkinter main loop
window.mainloop()
