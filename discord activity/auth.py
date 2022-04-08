import bottle, oauth, requests, webbrowser, threading, time
from bottle import request, response, redirect, ServerAdapter
class MyWSGIRefServer(ServerAdapter):
    server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()

    def stop(self):
        # self.server.server_close() <--- alternative but causes bad fd exception
        self.server.shutdown()

server = MyWSGIRefServer(host=oauth.ip, port = oauth.redirect_port)
app = bottle.Bottle()

def run():
    webbrowser.open(f'http://{oauth.ip}:{oauth.redirect_port}')
    try:
        app.run(server=server,quiet=True)
    except:
        return

@app.get('/')
def index():
    redirect(oauth.login_url)
@app.get(oauth.redirect_close)
def done():
    threading.Thread(daemon=True, target=server.stop).start()
    return """<html><body>
<h1>Auth Complete!</h1>
<h3>You can close this page now!</h3>
</body></html>"""
TOKEN = ''
@app.get(oauth.redirect_complete)
def auth():
    global TOKEN
    code = request.params.get('code')
    if not code:
        code = request.forms.get('code')
    if not code:
        return "ERROR WITH TOKEN"
    payload = {
        'client_id': oauth.client_id,
        'client_secret': oauth.client_secret,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': oauth.redirect_url
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(oauth.token_url,data=payload,headers=headers)
    try:
        r.raise_for_status()
    except:
        print("ERROR")
        return str(r.content)
    json = r.json()
    TOKEN = json.get('access_token')
    redirect(oauth.redirect_url2)

if __name__ == '__main__':
    run()