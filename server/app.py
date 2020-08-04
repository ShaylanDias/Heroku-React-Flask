from flask import Flask, send_file
import os

app = Flask(__name__, static_folder='../client/build/static')

@app.route('/')
def index():
    print('index endpoint')
    return send_file('../client/build/index.html')

if __name__ == '__main__':
    app.run(port=(os.getenv('PORT') if os.getenv('PORT') else 8000), debug=False)