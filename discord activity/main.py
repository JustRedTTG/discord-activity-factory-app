import tkinter, os, time, oauth, auth, socket, json, pypresence, datetime
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
# SETUP #
To start the activity change on your account, 
please go to http:127.0.0.1:2000 and login
# Note: Your token will be encrypted and saved for ease of access #
# You can delete the token file at any time to force this setup again #
""")
    auth.run()
    TOKEN = auth.TOKEN
    TOKEN_enc = list(TOKEN)
    TOKEN_enc.reverse()
    save('token', TOKEN_enc)
    return TOKEN_enc
def send_ws(ws, payload):
    ws.send(json.dumps(payload))
def receive_ws(ws):
    r = ws.recv()
    if r:
        return json.loads(r)
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

# Get discord client port
DISCORD_PORT = 0
for port in range(6463, 6473):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    if result == 0:
        DISCORD_PORT = port
        sock.close()
        break
    sock.close()
print(f"Found discord on: localhost:{DISCORD_PORT}")

# Autherize to discord

p = pypresence.Presence(oauth.client_id)
p.connect()
args = {
    'details':data.desc1,
    'large_image':data.img,
    'small_image':data.icon,
    'state':data.desc2,
    'start':time.time()
}
while True:
    p.update(
        details=args['details'],
        large_image=args['large_image'],
        small_image=args['small_image'],
        state=args['state'],
        start=args['start']
    )
    time.sleep(5)