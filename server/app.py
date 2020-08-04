from flask import Flask

app = Flask(__name__, static_folder='../client/build/static')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=8080, debug=False)