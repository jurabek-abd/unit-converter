from flask import Flask, render_template, request

# Create a Flask web app
app = Flask(__name__)

# Define route for the home page
@app.route('/')
def home():
    return "Welcome to the Unit Converter!"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)