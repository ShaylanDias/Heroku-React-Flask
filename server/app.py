from flask import Flask 
import os

app = Flask(__name__, static_folder='../client/build/', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(port=(os.getenv('PORT') if os.getenv('PORT') else 8000), debug=False)