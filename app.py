from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)


with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    hours = float(request.form['hours'])
    attendance = float(request.form['attendance'])
    previous_marks = float(request.form['previous_marks'])

    features = np.array([[hours, attendance, previous_marks]])

    prediction = model.predict(features)[0]

    
    prediction = max(0, min(100, prediction))

    return render_template('index.html',
                           prediction_text=f"Predicted Score: {prediction:.2f} ")

if __name__ == "__main__":
    app.run(debug=True)