# oauth PRAW template by /u/The1RGood #
#==================================================Config stuff====================================================
import time, praw
import webbrowser
from flask import Flask, request
from threading import Thread

access_information = ''
scope = 'identity' #SET THIS. SEE http://praw.readthedocs.org/en/latest/pages/oauth.html#oauth-scopes FOR DETAILS.
#==================================================End Config======================================================
#==================================================OAUTH APPROVAL==================================================
app = Flask(__name__)

CLIENT_ID = 'CLIENT_ID' #SET THIS TO THE ID UNDER PREFERENCES/APPS
CLIENT_SECRET = 'CLIENT_SECRET' #SET THIS TO THE SECRET UNDER PREFERENCES/APPS
REDIRECT_URI = 'http://127.0.0.1:65010/authorize_callback'

def kill():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()
	return "Shutting down..."

@app.route('/authorize_callback')
def authorized():
	global access_information
	state = request.args.get('state', '')
	code = request.args.get('code', '')
	access_information = r.get_access_information(code)
	user = r.get_me()
	text = 'Bot successfully started.'
	kill()
	return text
	
def refresh_access():
	while(True):
		time.sleep(1800)
		r.refresh_access_information(access_information['refresh_token'])
	
r = praw.Reddit('OAuth FLASK Template Script'
                'https://praw.readthedocs.org/en/latest/'
                'pages/oauth.html for more info.')
r.set_oauth_app_info(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)
webbrowser.open(r.get_authorize_url('DifferentUniqueKey',scope))
app.run(debug=False, port=65010)
amt = Thread(target=refresh_access,args=())
amt.daemon=True
amt.start()
#==================================================END OAUTH APPROVAL-=============================================
