from flask import Flask, render_template
import os

# Get the directory path of the current script
base_dir = os.path.abspath(os.path.dirname(__file__))

# Create the Flask application instance
app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'))

@app.route("/")
def home():
    return render_template('Home.html')

if __name__ == '__main__':
    app.run(debug=True)
