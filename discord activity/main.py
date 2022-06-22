import threading, sys
import tkinter, os, time, oauth, auth, socket, json, pypresence, datetime
from object import *
from creator import *
from tkinter import filedialog

# Setup values
ABORT_EXIT_TIME = 3
TOKEN = '' # THIS IS SET AUTOMATICALLY! DO NOT EDIT! YOU'LL BE ASKED FOR TOKEN!

# Get template file
types = [("Discord Activity Factory Template","*.daft"), 
	 ("Discord Activity Factory Session","*.dafs")]
Idir = "collection"
if len(sys.argv)>1 and sys.argv[1]=="-daft":
	del types[0]
	Idir = "sessions"
if os.path.exists(Idir) and os.path.isdir(Idir):
	pass
else:
	os.makedirs(Idir)
file = filedialog.askopenfilename(filetypes=types, defaultextension=types, initialdir=Idir)
dafs = False

# Double check template file
if os.path.exists(file) and file.endswith('.daft'):
	print('File selected:',file)
elif os.path.exists(file) and file.endswith('.dafs'):
	print('File selected:',file)
	dafs = True
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
if dafs:
	start = data.start
else:
	start = time.time()+5
args = {
	'details':data.desc1,
	'large_image':data.img or 'logo',
	'small_image':data.icon or 'logo',
	'state':data.desc2,
	'start':start
}
saving = False
saving_temp = None
def writer():
	global data, saving, saving_temp
	print("Please feel free to write and edit any of the below data, during runtime.")
	while True:
		s = "WRITER\n======"
		for item in list(args):
			s += f"\n{item} = {args[item]}"
		print(s+"\n======")
		dataI = input('> ')
		try:
			item, info = dataI.split('=')
		except:
			if dataI == "save":
				saving_temp = template(args['large_image'], args['small_image'], args['details'], args['state'], data.type, args['start'])
				saving = True
				continue
			else:
				continue
		info = info.replace('time()',str(time.time()))
		item = item.replace(' ','')
		while info.startswith(' '):
			info = info[1:len(info)]
		if item == 'start':
			try:
				args[item] = float(info)
			except:
				args[item] = info
		else:
			args[item] = info
		os.system('cls' if os.name == 'nt' else 'clear')

threading.Thread(daemon=True, target=writer).start()
while True:
	try:
		p.update(
			details=args['details'],
			large_image=args['large_image'],
			small_image=args['small_image'],
			state=args['state'],
			start=args['start']
		)
	except:
		time.sleep(5)
	before = time.time()
	time.sleep(5)
	after = float(str(time.time()-before)[0:4])
	args['start'] = args['start'] + ( after - 5 )
	if saving:
		save_template(saving_temp)
		saving = False
