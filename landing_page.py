from pathlib import Path
import webbrowser
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess
import random
from tkinter import Menu

# Paths set for assets and outputs
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/anishkashahane/Desktop/landing")


# Function to retrieve the path to an asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# random number generator for randomising restaurants
random_number = random.randint(0, 4)
random_dispaly_number = random_number


# Retrieval restaurant data from the database
def retrieve_restaurant_data():
    global random_dispaly_number
    db_path = 'restaurants.db'
    if not os.path.exists(db_path):
        messagebox.showerror("Error", "Database file not found.")
        return []

    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        query = "SELECT image_path, website FROM featured_restaurants LIMIT 3 OFFSET ?"
        c.execute(query, (random_dispaly_number,))
        data = c.fetchall()
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve restaurant data: {str(e)}")
        return []
    finally:
        if conn:
            conn.close()


# Function to load image and for image resizing
def load_image(image_path, size=(346, 453)):
    if not os.path.exists(image_path):
        messagebox.showerror("Error", f"Image file not found: {image_path}")
        return None

    try:
        img = Image.open(image_path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image: {str(e)}")
        return None


# Function that opens the URL in the web browser for any restaurant in the main database
def open_url(url):
    webbrowser.open(url)


# Retrieval of restaurant names from the main database
def get_restaurant_names():
    global random_dispaly_number
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM featured_restaurants LIMIT 3 OFFSET {random_dispaly_number }")
    data = cursor.fetchall()
    conn.close()
    return [item[0] for item in data]


# Retrieval of restaurant locations from the main database
def get_restaurant_locations():
    global random_dispaly_number
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT location FROM featured_restaurants LIMIT 3 OFFSET {random_dispaly_number }")
    data = cursor.fetchall()
    conn.close()
    return [item[0] for item in data]


# Canvas is updated with the retrieved restaurant data
def update_canvas_with_data(canvas, text_ids, data):
    for text_id, text in zip(text_ids, data):
        canvas.itemconfig(text_id, text=text)


# Functions that open different pages dependent on user choice,
# by destroying the current window and opening the relevant window by starting a new subprocess
def open_landing():
    window.destroy()
    subprocess.Popen(['python', 'landing_page.py'])


# Functions that opens the vegetarian window
def open_vegetarian_page_1():
    window.destroy()
    subprocess.Popen(['python', 'vegetarian_mainpage.py'])


# Function that opens the gluten-free window
def open_gluten_free_page_1():
    window.destroy()
    subprocess.Popen(['python', 'glutenfree_mainpage.py'])


# Function that opens the vegan window
def open_vegan_page_1():
    window.destroy()
    subprocess.Popen(['python', 'vegan_mainpage.py'])


# Function that opens the keto window
def open_keto_page_1():
    window.destroy()
    subprocess.Popen(['python', 'keto_mainpage.py'])


# Function that opens the healthy window
def open_healthy_page_1():
    window.destroy()
    subprocess.Popen(['python', 'healthy_mainpage.py'])


# Function that opens the accounts window
def open_account_page():
    window.destroy()
    subprocess.Popen(['python', 'account_page.py'])

# Initialize main window
window = Tk()
window.title("DINE-EZ")
window.geometry("1450x900")
window.configure(bg="#FFFFFF")

# Canvas setup to hold widgets
canvas = Canvas(window, bg="#FFFFFF", height=900, width=1450, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)


def main():
    global window
    restaurant_data = retrieve_restaurant_data()

    # Load images from database paths
    images_and_urls = [(load_image(data[0]), data[1]) for data in restaurant_data]

    if not all(img for img, url in images_and_urls):
        return

    restaurant_1 = Button(image=images_and_urls[0][0], borderwidth=0, highlightthickness=0,
                      command=lambda: open_url(images_and_urls[0][1]), relief="flat")
    restaurant_1.place(x=81.0,y=320.0,width=342.0,height=379.0)
    restaurant_1.image = images_and_urls[0][0]

    restaurant_2 = Button(image=images_and_urls[1][0], borderwidth=0, highlightthickness=0,
                      command=lambda: open_url(images_and_urls[1][1]), relief="flat")
    restaurant_2.place(x=556.0, y=320.0, width=342.0, height=379.0)
    restaurant_2.image = images_and_urls[1][0]

    restaurant_3 = Button(image=images_and_urls[2][0], borderwidth=0, highlightthickness=0,
                      command=lambda: open_url(images_and_urls[2][1]), relief="flat")
    restaurant_3.place(x=1017.0, y=320.0, width=342.0, height=379.0)
    restaurant_3.image = images_and_urls[2][0]

    # Decorative line image on the canvas
    image_image_1 = PhotoImage(file=relative_to_assets("line.png"))
    canvas.create_image(721.0, 203.0, image=image_image_1)

    # Decorative line image on the canvas
    image_image_2 = PhotoImage(file=relative_to_assets("line.png"))
    canvas.create_image(727.0, 860.0, image=image_image_2)

    # Decorative image on the canvas
    image_image_3 = PhotoImage(
        file=relative_to_assets("featured.png"))
    canvas.create_image(712.0, 244.0, image=image_image_3)

# Images for graphical user interface, aesthetics
    image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
    canvas.create_image(252.0, 557.0, image=image_image_4)

    image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
    canvas.create_image(725.0, 557.0, image=image_image_5)

    image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
    canvas.create_image(1180.0, 557.0, image=image_image_6)

    image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
    canvas.create_image(338.0, 244.0, image=image_image_7)

    image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
    canvas.create_image(1105.0, 241.0, image=image_image_8)

    # 'Vegan' button that navigates to the first page of vegan options
    button_image_vegan = PhotoImage(file=relative_to_assets("vegan.png"))
    button_vegan = Button(image=button_image_vegan, borderwidth=0, highlightthickness=0,
                          command=lambda: open_vegan_page_1(), relief="flat")
    button_vegan.place(x=681.0, y=129.0, width=205.0, height=68.0)

    # 'Gluten-Free' button that navigates to the first page of gluten-free options
    button_image_gluten_free = PhotoImage(file=relative_to_assets("gluten_free.png"))
    button_gluten_free = Button(image=button_image_gluten_free, borderwidth=0, highlightthickness=0,
                                command=lambda: open_gluten_free_page_1(), relief="flat")
    button_gluten_free.place(x=331.0, y=141.0, width=281.0, height=43.0)

    # 'Keto' button that navigates to the first page of keto options
    button_image_keto = PhotoImage(
        file=relative_to_assets("keto.png"))
    button_keto = Button(image=button_image_keto, borderwidth=0, highlightthickness=0,
                         command=lambda: open_keto_page_1(), relief="flat")
    button_keto.place(x=951.0, y=126.0, width=197.0, height=66.0)

    # 'Vegetarian' button that navigates to the first page of vegetarian options
    button_image_vegetarian = PhotoImage(
        file=relative_to_assets("vegetarian.png"))
    button_vegetarian = Button(image=button_image_vegetarian, borderwidth=0, highlightthickness=0,
                               command=lambda: open_vegetarian_page_1(), relief="flat")
    button_vegetarian.place(x=37.0, y=128.0, width=249.0, height=67.0)

    # 'Healthy' button that navigates to the first page of healthy food options
    button_image_healthy = PhotoImage(file=relative_to_assets("healthy.png"))
    button_healthy = Button(image=button_image_healthy, borderwidth=0, highlightthickness=0,
                            command=lambda: open_healthy_page_1(), relief="flat")
    button_healthy.place(x=1218.0, y=129.0, width=194.0, height=60.0)

    # 'Landing' button that navigates back to the landing page (home)
    button_image_landing = PhotoImage(
        file=relative_to_assets("logo.png"))
    button_landing = Button(image=button_image_landing, borderwidth=0, highlightthickness=0,
                            command=lambda: open_landing(), relief="flat")
    button_landing.place(x=49.0, y=40.0, width=277.0, height=71.0)

    # 'Account' button that navigates to the user's account page
    account_button_image = PhotoImage(file=relative_to_assets("account.png"))
    account_button = Button(image=account_button_image, borderwidth=0, highlightthickness=0,
                            command=lambda: open_account_page(), relief="flat")
    account_button.place(x=1275.0, y=44.0, width=62.0, height=62.0)

    # Dynamic text items for restaurant names on the canvas
    # These placeholders will be updated with the real restaurant names from the database
    restaurant_name_text_1 = canvas.create_text(161.0, 713.0, anchor="nw", text="NAME OF RESTAURANT",
                                                fill="#000000", font=("Inter Light", 25))
    restaurant_name_text_2 = canvas.create_text(645.0, 713.0, anchor="nw", text="NAME OF RESTAURANT",
                                                fill="#000000", font=("Inter Light", 25))
    restaurant_name_text_3 = canvas.create_text(1130.0, 713.0, anchor="nw", text="NAME OF RESTAURANT",
                                                fill="#000000", font=("Inter Light", 25))

    # Store text IDs in a list for easy updating
    restaurant_name_texts = [restaurant_name_text_1, restaurant_name_text_2, restaurant_name_text_3]

    # Retrieval and update of restaurant names on the canvas on user-interface
    restaurant_names = get_restaurant_names()
    update_canvas_with_data(canvas, restaurant_name_texts, restaurant_names)

    # Dynamic text items for restaurant locations on the canvas
    # These placeholders will be updated with real restaurant locations from the database
    restaurant_location_text_1 = canvas.create_text(115.0, 757.0, anchor="nw", text="location",
                                                    fill="#000000", font=("Inter Light", 17))
    restaurant_location_text_2 = canvas.create_text(600.0, 757.0, anchor="nw", text="location",
                                                    fill="#000000", font=("Inter Light", 17))
    restaurant_location_text_3 = canvas.create_text(1059.0, 757.0, anchor="nw", text="location",
                                                    fill="#000000", font=("Inter Light", 17))

    # Store the text IDs in a list for easy updating
    restaurant_location_texts = [restaurant_location_text_1, restaurant_location_text_2, restaurant_location_text_3]

    # Retrieve the actual restaurant locations from the database and update the canvas text placeholders
    restaurant_locations = get_restaurant_locations()
    update_canvas_with_data(canvas, restaurant_location_texts, restaurant_locations)

    # Disable window resizing on user interface
    window.resizable(False, False)

    # Main loop to run the application
    window.mainloop()



if __name__ == "__main__":
    main()
