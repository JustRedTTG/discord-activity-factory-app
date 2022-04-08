client_id = 961899767720468520
client_secret = 'SXO2GXFBXHfAmg_06BRsKijkMQn_NGke'
redirect_port = 2000
ip = '127.0.0.1'
redirect_complete = '/complete'
redirect_close = '/close'
redirect_url = f'http://{ip}:{redirect_port}{redirect_complete}'
redirect_url2 = f'http://{ip}:{redirect_port}{redirect_close}'
login_url = f"https://discord.com/api/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_url}&response_type=code&scope=identify rpc rpc.activities.write"
token_url = f"https://discord.com/api/oauth2/token"