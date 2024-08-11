# Imports
from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage


# Paths set for assets and outputs
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/anishkashahane/Desktop/loading")


# Function to retrieve the path to an asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Create a new Tkinter window
window = Tk()
window.title("DINE-EZ")
window.geometry("1450x900")
window.configure(bg="#FFFFFF")


# Canvas setup to hold widgets
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=900,
    width=1450,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# Canvas positioned on top-left corner of the window
canvas.place(x=0, y=0)

# image loaded from the assets folder using the relative_to_assets function
image_loading_image = PhotoImage(
    file=relative_to_assets("loading.png"))
image_loading = canvas.create_image(
    725.0,
    436.0,
    image=image_loading_image
)

# Start the Tkinter main loop
window.mainloop()
