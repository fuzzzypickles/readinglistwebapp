from flask import Flask, render_template
import requests

#variable used to acess information about the server
app = Flask(__name__)
app.config["DEBUG"] = True

#route() binds the url http://yourwebapp to this function.
@app.route("/")
def hello():
	return render_template("hello.html")

@app.route("/name")
def name():
	return "Bella Shim"

@app.route("/search")
def search():
	return render_template("search.html")
#0.0.0.0 lets all public IPs connect to the server. 
if __name__ == "__main__":
	app.run(host="0.0.0.0")

