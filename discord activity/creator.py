import tkinter, os
from tkinter import filedialog
from object import *

# Setup
root = tkinter.Tk()
root.withdraw()

temp = None
default_icon = Image.open('icon.png')
# Functions
def get_image():
    print("If you don't see the window, try looking in your task view")
    file = filedialog.askopenfilename(title="Select Icon", filetypes=[("PNG", "*.png"),("JPG", "*.jpg")], initialdir="icons")
    if os.path.exists(file):
        return Image.open(file)
def save_template():
    print("If you don't see the window, try looking in your task view")
    types = [("Discord Activity Factory Template","*.daft")]
    location = filedialog.asksaveasfile(title="Save Template", filetypes=types, defaultextension=types, initialdir="collection")
    location.close()
    save(location.name,temp)

# Make template
print("Please select the main icon for this activity")
icon = get_image() or default_icon
print("Please select the sub icon for this activity. You can skip this, click cancel!")
mini_icon = get_image()
print("Please the title for your activity")
desc1 = input('> ')

typeactv = 'playing'
# Make...
temp = template(icon, mini_icon, desc1, typeactv)

# Save template
save_template()
