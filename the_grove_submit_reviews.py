from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import sqlite3
import os
import subprocess


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("/Users/anishkashahane/Desktop/write_reviews")


# Define paths for output and assets
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Function to center the window on the screen
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


# Fetch user ID from environment variables
user_idnum = os.getenv('user_idnum')
if user_idnum is not None:
    user_id = int(user_idnum)
else:
    user_id = 1  # Default user_id if environment variable is not set

offset = user_id - 1


# Function to fetch the username from the database based on offset
def get_usernames():
    global offset
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    try:
        query = f'SELECT username FROM users LIMIT 1 offset {offset}'
        cursor.execute(query)
        data = cursor.fetchone()
        if data:
            return data[0]
        else:
            return None
    finally:
        conn.close()


# Function to open the review submission script
def open_reviews():
    subprocess.Popen(['python', 'the_grove_submit_reviews.py'])


# Function to check if the review submission script exists and open it
def open_submit_reviews():
    print("Opening submit reviews...")
    script_path = 'the_grove_submit_reviews.py'
    if os.path.exists(script_path):
        print("Script found.")
        window.destroy()
        subprocess.Popen(['python', script_path])
    else:
        print("Script not found.")


# Function which handles review submission
def submit_review():
    review_text = user_review.get()
    username = get_usernames()

    if review_text != '' and username:
        review_with_quotes = f':  " {review_text} "'
        conn = sqlite3.connect('restaurants.db')
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO the_grove_reviews (username, user_review) VALUES (?, ?)
            ''', (username, review_with_quotes))
            conn.commit()
        finally:
            conn.close()
            user_review.delete(0, 'end')  # Clear the entry after submission
            response = messagebox.askquestion("Choose an option", "REVIEW SUBMITTED! \n "
                                                                  "Would you like to submit another review?")
            if response == 'yes':
                open_reviews()

            elif response == 'no':
                window.destroy()
    else:
        messagebox.showerror('Error', 'Please write a review')


# Initialize main window
window = Tk()
window.title("DINE-EZ")
window.geometry("545x446")
window.configure(bg="#FFFFFF")

# Connect to the reviews database and create the reviews table if it doesn't exist
conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS the_grove_reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        user_review TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

# Tkinter canvas and widgets setup
canvas = Canvas(window, bg="#FFFFFF", height=446, width=545, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# Load and place the image on the canvas
image_image_logo = PhotoImage(file=relative_to_assets("logo.png"))
image_logo = canvas.create_image(273.0, 72.0, image=image_image_logo)

# Create and place the "REVIEWS" text on the canvas
canvas.create_text(
    228.0, 106.0, anchor="nw", text="REVIEWS", fill="#000000", font=("Inter ExtraLightItalic", 20)
)

# Load and place the entry background image
entry_image = PhotoImage(file=relative_to_assets("entry_background_image.png"))
entry_bg = canvas.create_image(273.0, 270.0, image=entry_image)

# Create and place the entry widget for review input
user_review = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0)
user_review.place(x=111.0, y=241.0, width=324.0, height=56.0)

# Load and place the submit button image
submit_button_image = PhotoImage(file=relative_to_assets("submit_button.png"))
submit_button = Button(image=submit_button_image, borderwidth=0, highlightthickness=0,
                       command=submit_review, relief="flat")
submit_button.place(x=201.0, y=313.0, width=166.0, height=49.0)

# Create and place the "WRITE A REVIEW :" text on the canvas
canvas.create_text(
    97.0, 204.0, anchor="nw", text="WRITE A REVIEW :", fill="#000000", font=("Inter Light", 20)
)

# Center the window on the screen
center_window(window)
window.resizable(False, False)
window.mainloop()
