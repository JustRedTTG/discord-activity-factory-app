import tkinter, os, time, datetime, oauth, auth
from object import *
from tkinter import filedialog

# Setup tkinter
root = tkinter.Tk()
root.withdraw()

# Setup values
ABORT_EXIT_TIME = 3
TOKEN = '' # THIS IS SET AUTOMATICALLY! DO NOT EDIT! YOU'LL BE ASKED FOR TOKEN!

# Get template file
types = [("Discord Activity Factory Template","*.daft")]
file = filedialog.askopenfilename(filetypes=types, defaultextension=types, initialdir="collection")

# Double check template file
if os.path.exists(file) and file.endswith('.daft'):
    print('File selected:',file)
else:
    print('Invalid or no file. Abort')
    time.sleep(ABORT_EXIT_TIME)
    exit()

# Try to load template file
try:
    data = load(file)[0]
except:
    print('Invalid or corrupt file. Abort')
    time.sleep(ABORT_EXIT_TIME)
    exit()

def save_token():
    print("""
# FISRT TIME SETUP #
To start the activity change on your account, 
please go to http:127.0.0.1:2000 and login
# Note: Your token will be encrypted and saved ease of access #
# You can delete the token file at any time to force this setup again #
""")
    auth.run()
    TOKEN = auth.TOKEN
    TOKEN_enc = list(TOKEN)
    TOKEN_enc.reverse()
    save('token', TOKEN_enc)
    return TOKEN_enc

# Get user token
if os.path.exists('token'):
    try:
        TOKEN_enc = load('token')[0]
    except:
        print("error occured loading token")
        TOKEN_enc = save_token()
else:
    TOKEN_enc = save_token()

# Decrypt user token
TOKEN_enc.reverse()
TOKEN = ''
for item in TOKEN_enc:
    TOKEN += item

print(TOKEN)