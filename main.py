from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"

@app.route('/')
def show_main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
