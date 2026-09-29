import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score ,accuracy_score


data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 3, 4, 5, 6, 7, 8, 9, 10, 11],

    "attendance": [55, 60, 65, 70, 72, 75, 78, 82, 88, 92,
                   58, 63, 69, 74, 77, 80, 85, 89, 94, 96],

    "assignments_completed": [2, 3, 4, 5, 5, 6, 7, 7, 8, 9,
                              3, 4, 5, 5, 6, 7, 7, 8, 9, 10],

    "sleep_hours": [5, 5, 6, 6, 7, 7, 7, 8, 8, 8,
                    5, 6, 6, 7, 7, 7, 8, 8, 8, 9],

    "final_score": [35, 42, 48, 55, 60, 65, 70, 76, 84, 90,
                    40, 46, 53, 58, 64, 69, 75, 82, 88, 94]
}


df = pd.DataFrame(data)

print("Dataset:")
print(df)

print("\nShape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

X = df[[
    "study_hours",
    "attendance",
    "assignments_completed",
    "sleep_hours"
]]

y = df["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=0
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)

mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)
accuracy = r2_score(y_test, y_pred)
print("Model Accuracy (R²):", accuracy)
print("Model Accuracy (%):", accuracy * 100)
print("\nMean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R-squared:", r2)

new_student = [[7, 85, 7, 7]]

prediction = model.predict(new_student)

print("\nNew Student:")
print("Study Hours: 7")
print("Attendance: 85%")
print("Assignments: 7")
print("Sleep Hours: 7")

print("\nPredicted Final Score:", prediction[0])

print("\nLinear Regression Model Implemented Successfully!")