#Importing necessary libraries
from flask import Flask

#Initializing Flask Application
app = Flask(__name__)

# Index Route
# Route for showing Hello World on the browser.
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
