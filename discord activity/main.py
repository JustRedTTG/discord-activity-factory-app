import discord, tkinter, os, time, datetime
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
guild_subscription_options = discord.GuildSubscriptionOptions.off()
Client = discord.Client(guild_subscription_options=guild_subscription_options)

@Client.event
async def on_ready():
    print("Setting activity...")
    if data.type == 'playing':
        actv_type = discord.ActivityType.playing
    actv = discord.Activity(
        name=data.desc1,
        type=actv_type,
        #state='STATE',
        #details='DETAILS',
        large_image_url='https://cdn.discordapp.com/attachments/853191098285424652/961746816838279168/favicon.png?size=4096'
    )
    await Client.change_presence(activity=actv)


def save_token():
    print("""
# FISRT TIME SETUP #
To start the activity change on your account, 
please paste token below
# Note: Your token will be encrypted and saved ease of access #
# You can delete the token file at any time to force this setup again #
""")
    TOKEN = input("TOKEN = ")
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

Client.run(TOKEN)