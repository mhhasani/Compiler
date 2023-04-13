import tkinter as tk
from PIL import Image, ImageTk
import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Create a tkinter window
window = tk.Tk()
window.title('Images from XML')

# Create a canvas widget
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Iterate through the XML elements
for child in root:
    # Get the image filename and label text
    filename = child.find('filename').text
    label_text = child.find('label').text

    # Open and resize the image
    image = Image.open(filename)
    image = image.resize((200, 200))

    # Create a Photoimage object from the image
    photo = ImageTk.PhotoImage(image)

    # Create a label widget and set its attributes
    label = tk.Label(canvas, image=photo, text=label_text, compound='top')
    label.photo = photo

    # Use the canvas widget's create_window method to place the label on the canvas
    canvas.create_window(100, 100, window=label)

# Start the tkinter event loop
window.mainloop()
