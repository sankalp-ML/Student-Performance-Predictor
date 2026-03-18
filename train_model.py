import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


data = pd.read_csv("student_data.csv")


X = data[["hours", "attendance", "previous_score"]]  
y = data["marks"]  


model = LinearRegression()
model.fit(X, y)


# x_input = [[10,60,80]]
# y_pred = model.predict(x_input)
# print(y_pred)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved as model.pkl")