from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcome():
    return "WELCOME TO MY WEBSITE"

@app.route('/contact')
def contact():
    return "Contact page"

@app.route('/gallery')
def gallery():
    return " gallery "

@app.route('/home')
def home():
    return "Home page"

if __name__=="__main__":
    app.run()
