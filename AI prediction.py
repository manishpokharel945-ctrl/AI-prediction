import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("student_data.csv")

# Understand dataset
print("First 5 rows of dataset:")
print(data.head())

print("\nDataset Information:")
print(data.info())

X = data[["StudyHours", "Attendance", "PreviousMarks", "AssignmentScore"]]
y = data["Result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


new_student = [[5, 80, 65, 70]]

prediction = model.predict(new_student)

print("\nPrediction for new student:", prediction[0])