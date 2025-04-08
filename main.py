from flask import Flask, request, jsonify

# Create the Flask app
app = Flask(__name__)

# Route to display a welcome message
@app.route('/')
def home():
    return "Congratulations it's a web app! Welcome to flask Demo."
    


if __name__ == '__main__':
    app.run(debug=True)
