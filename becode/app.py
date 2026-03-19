from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


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


    if prediction >= 90:
        grade = "A "
    elif prediction >= 75:
        grade = "B "
    elif prediction >= 50:
        grade = "C "
    else:
        grade = "D "

    return render_template('index.html',
                           prediction_text=f"{prediction:.2f}",
                           grade=grade)

if __name__ == "__main__":
    app.run(debug=True)