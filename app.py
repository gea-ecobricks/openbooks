from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to OpenBooks!</h1><p>Your sustainable accounting solution.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)