Student Performance Predictor

Project Overview

The **Student Performance Predictor** is a Machine Learning web application that predicts a student's performance based on various input features such as study hours, attendance, and other academic factors.

This project demonstrates the end-to-end ML workflow:

* Data collection
* Model training
* Model deployment using Flask

Live Demo

https://student-performance-predictor-3thk.onrender.com

Features

* Predict student performance instantly
* User-friendly web interface
* Fast and real-time predictions
* Input validation for better accuracy

Tech Stack

* **Frontend:** HTML, CSS
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn
* **Deployment:** Render / Railway / etc.

 
 Project Structure

Student-Performance-Predictor/
│
├── app.py              
├── model1.pkl          
├── templates/          
│   └── index.html
├── static/             
├── dataset.csv         
└── README.md


How It Works

1. User enters input values (like study hours, attendance, etc.)
2. Data is sent to the Flask backend
3. The trained ML model processes the input
4. Prediction is generated and displayed on the web page



Run Locally

1. Clone the repository

bash
git clone https://github.com/sankalp-ML/Student-Performance-Predictor.git
cd Student-Performance-Predictor


2. Install dependencies

bash
pip install -r requirements.txt


3. Run the app

bash
python app.py


4. Open in browser


http://127.0.0.1:5000/


Future Improvements

* Add data visualization (graphs & charts)
* Improve model accuracy
* Deploy with custom domain
* Store user inputs in database


Author

Sankalp H V

Contribute

Feel free to fork this repository and contribute!


