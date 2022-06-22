import tkinter, os
from tkinter import filedialog
from object import *

# Setup
root = tkinter.Tk()
root.withdraw()

temp = None
# Functions
def save_template(temp):
    print("If you don't see the window, try looking in your task view")
    if temp.start:
        types = [("Discord Activity Factory Session","*.dafs")]
        dafs = True
        Idir = "sessions"
    else:
        types = [("Discord Activity Factory Template","*.daft")]
        Idir = "collection"
    if os.path.exists(Idir) and os.path.isdir(Idir):
        pass
    else:
        os.makedirs(Idir)
    if dafs:
        location = filedialog.asksaveasfile(title="Save Session", filetypes=types, defaultextension=types, initialdir="sessions")
    else:
        location = filedialog.asksaveasfile(title="Save Template", filetypes=types, defaultextension=types, initialdir="collection")
    location.close()
    save(location.name,temp)

# Make template
if __name__ == "__main__":
    print("Please select the main icon for this activity")
    icon = input('icon > ')
    print("Please select the sub icon for this activity. You can skip this, click cancel!")
    mini_icon = input('mini_icon > ')
    print("Please the description for your activity")
    desc1 = input('description > ')
    print("Please the default status for your activity")
    status = input('status > ')

    typeactv = 'playing'
    # Make...
    temp = template(icon, mini_icon, desc1, status, typeactv)

    # Save template
    save_template(temp)
