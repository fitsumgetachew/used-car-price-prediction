from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        pass


    return render_template("")
