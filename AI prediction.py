# AI Student Result Prediction Project
# Created by Manish Pokharel

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("student_data.csv")

# Separate input features and output result
X = data[["Study_Hours", "Attendance"]]
y = data["Result"]

# Split data into training and testing parts
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create and train AI model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("===================================")
print("   AI Student Result Prediction")
print("===================================")
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Take user input
study_hours = float(input("\nEnter study hours per day: "))
attendance = float(input("Enter attendance percentage: "))

# Make prediction
prediction = model.predict([[study_hours, attendance]])

print("\nPrediction Result:")
print(f"The student is likely to: {prediction[0]}")