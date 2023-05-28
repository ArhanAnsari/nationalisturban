from flask import Flask

app = Flask('app',static_url_path="/static")


@app.route('/')
def index():
	page = ""
	f = open("website.html", "r")
	page = f.read()
	f.close()
	return page


app.run(host='0.0.0.0', port=8080)
