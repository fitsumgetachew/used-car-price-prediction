from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = [
            float(request.form['presentPrice']) / 1000,
        ]
        seller_type = request.form['sellerType']
        user_input.extend([1, 0] if seller_type == 'I' else [0, 1])
        user_input.extend([

            int(request.form['sellingYear']) - int(request.form['manufactureYear']),
            int(request.form['kmDriven']),
            1 if request.form['diesel'] == '1' else 0
        ])
        print(user_input)

        # Load the machine learning model
        model = pickle.load(open('model.pkl', 'rb'))
        selling_price = model.predict([np.array(user_input)])



        return render_template("result.html", predicted_price= int(1000 * selling_price))
        pass

    return render_template("input_field.html")


if __name__ == '__main__':
    app.run(debug=True)
