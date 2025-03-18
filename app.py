from flask import Flask

app = Flask(__name__)

# Route untuk hello dengan nama pengguna di URL
@app.route('/hello/<username>')
def hello(username):
    return f"Hello, {username}!"

# Route untuk goodbye dengan nama pengguna di URL
@app.route('/goodbye/<username>')
def goodbye(username):
    return f"Goodbye, {username}!"

if __name__ == '__main__':
    # Start the Flask web server on port 8080
    app.run(debug=True, port=5050)
