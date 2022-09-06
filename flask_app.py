
from flask import Flask, redirect
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    url_list = [ "http://otree11.experiment.unsw.edu.au/join/savadoge",
        "http://otree11.experiment.unsw.edu.au/join/mogeliva",
        "http://otree11.experiment.unsw.edu.au/join/herebema",
        "http://otree11.experiment.unsw.edu.au/join/japagaza"]
    return redirect(url_list[random.randint(0, 5)], code=302)

if __name__ == '__main__':
    app.run()
