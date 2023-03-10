from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<string:name>")
def say(name):
    return (f"Hi {name}")

@app.route("/repeat/<int:number>/<string:word>")
def repeat(number, word):
    temp_str = ""
    temp_str += (word+" ")*number
    return (temp_str)


if __name__ == "__main__":
    app.run(debug = True, port=5001)
