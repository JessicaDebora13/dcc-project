from flask import Flask

app = Flask(__name__)

# Define the /hello route
@app.route('/hello')
def hello():
    return "Hello, World!"

# Define the /goodbye route
@app.route('/goodbye')
def goodbye():
    return "Goodbye, World!"

if __name__ == '__main__':
    # Start the Flask web server on port 5000
    app.run(debug=True, port=5000)
