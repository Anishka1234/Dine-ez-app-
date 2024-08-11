# Imports
from pathlib import Path
import sqlite3
from tkinter import Tk, Canvas, Button, PhotoImage


# Paths set for assets and outputs
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/anishkashahane/Desktop/display_reviews")


# Function to retrieve the path to an asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Function which centers the window on the screen on the user inter-face
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


# Function which gets user reviews from the main database
def get_reviews():
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_review FROM sideart_reviews LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    return [item[0] for item in data]


# Function which retrives the user's usernames from the database
def get_username():
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM sideart_reviews LIMIT 10")
    data = cursor.fetchall()
    conn.close()
    return [item[0] for item in data]


# Function which updates the canvas with user reviews and the username respectively
def update_canvas_with_data(canvas, text_ids, data):
    for text_id, text in zip(text_ids, data):
        canvas.itemconfig(text_id, text=text)


# Function to exit the review tab
def exit_review_tab():
    window.destroy()


# Initialize main window
window = Tk()
window.title("DINE-EZ")
window.geometry("800x446")
window.configure(bg="#FFFFFF")


# Canvas setup to hold widgets
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=446,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)


canvas.create_text(350.0, 72.0, anchor="nw", text="REVIEWS", fill="#000000", font=("Inter ExtraLightItalic", 20))


# Create text items for displaying reviews
text_id1 = canvas.create_text(104.0, 117.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id2 = canvas.create_text(104.0, 150.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id3 = canvas.create_text(104.0, 183.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id4 = canvas.create_text(104.0, 216.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id5 = canvas.create_text(104.0, 249.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id6 = canvas.create_text(104.0, 281.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id7 = canvas.create_text(104.0, 313.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id8 = canvas.create_text(104.0, 376.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id9 = canvas.create_text(104.0, 403.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id10 = canvas.create_text(104.0, 347.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))

# List of text item IDs for reviews
text_ids = [text_id1, text_id2, text_id3, text_id4, text_id5, text_id6, text_id7, text_id8, text_id9, text_id10]

# Retrieval of user reviews and to update the canvas with the data
user_reviews = get_reviews()
update_canvas_with_data(canvas, text_ids, user_reviews)


# Create text items for displaying usernames
text_id11 = canvas.create_text(
    35.0, 117.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))

text_id12 = canvas.create_text(
    35.0,
    150.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter", 15 * -1)

)

text_id13 = canvas.create_text(35.0, 183.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id14 = canvas.create_text(35.0, 216.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id15 = canvas.create_text(35.0, 249.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id16 = canvas.create_text(35.0, 281.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id17 = canvas.create_text(35.0, 313.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id18 = canvas.create_text(35.0, 376.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id19 = canvas.create_text(35.0, 404.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id20 = canvas.create_text(35.0, 347.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))


# List of text item IDs for usernames
text_ids = [text_id11, text_id12, text_id13, text_id14, text_id15, text_id16,
            text_id17, text_id18, text_id19, text_id20]

# Retrieval usernames and to update the canvas with the data
usernames = get_username()
update_canvas_with_data(canvas, text_ids, usernames)


image_image_1 = PhotoImage(
    file=relative_to_assets("logo.png"))
image_1 = canvas.create_image(400.0, 36.0, image=image_image_1)

# Exit button allows user to exit the displayed reviews
button_image_exit = PhotoImage(
    file=relative_to_assets("exit.png"))
button_exit = Button(image=button_image_exit, borderwidth=0, highlightthickness=0,
                     command=lambda: exit_review_tab(), relief="flat")
button_exit.place(x=750.0, y=398.0, width=51.0, height=37.0)

# Center the window and disable window resizing
center_window(window)

# Disable window resizing on user interface
window.resizable(False, False)
window.mainloop()
