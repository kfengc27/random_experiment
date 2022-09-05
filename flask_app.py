
from flask import Flask, redirect
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    url_list = ['https://lab5-for-john.herokuapp.com/join/risaheke', "https://lab5-for-john.herokuapp.com/join/mepagagu", "https://lab5-for-john.herokuapp.com/join/gepuzujo","https://lab5-for-john.herokuapp.com/join/honozuti","https://lab5-for-john.herokuapp.com/join/dijakiha","https://lab5-for-john.herokuapp.com/join/nusefeva"]
    return redirect(url_list[random.randint(0, 5)], code=302)

if __name__ == '__main__':
    app.run()