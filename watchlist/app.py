#Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'DaniRodric,Welcome to My Watchlist!'

