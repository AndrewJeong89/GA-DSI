import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/greet/<name>')
def greet(name):
	return "Hello, %s!" %name
    
if __name__ == '__main__':
    app.run(debug=True)