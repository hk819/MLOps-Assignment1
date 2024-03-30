import os
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Ensure the model directory exists
model_directory = './model'
if not os.path.exists(model_directory):
    os.makedirs(model_directory)

# Load dataset
X, y = load_iris(return_X_y=True)

# Split dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predict and calculate accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy}")

# Save the trained model
model_path = os.path.join(model_directory, 'iris_model.pkl')
joblib.dump(model, model_path)
