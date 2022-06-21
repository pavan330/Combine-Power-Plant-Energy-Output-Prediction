from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        AT = float(request.form['AT'])
        EV = float(request.form['EV'])
        AP = float(request.form['AP'])
        RH = float(request.form['RH'])
        

        values = np.array([[AT, EV, AP,RH]])
        prediction = model.predict(values)
        output = round(prediction[0], 2)
        return render_template('result.html', prediction_text='Net Hourly Electrical Energy Output (PE) = {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)