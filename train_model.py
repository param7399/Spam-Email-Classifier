import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("=" * 50)
print("      SPAM EMAIL CLASSIFIER TRAINING")
print("=" * 50)

# Load Dataset
data = pd.read_csv("dataset/spam.csv", encoding="latin-1")

# Keep only required columns
data = data[['v1', 'v2']]

# Rename columns
data.columns = ['label', 'message']

print("\nDataset Loaded Successfully!")
print("Total Messages :", len(data))

# Features and Labels
X = data["message"]
y = data["label"]

# Convert Text into Numerical Features
vectorizer = TfidfVectorizer(stop_words="english")

X = vectorizer.fit_transform(X)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = MultinomialNB()

model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("\nModel Accuracy :", round(accuracy * 100, 2), "%")

print("\nClassification Report\n")
print(classification_report(y_test, prediction))

print("\nConfusion Matrix\n")
print(confusion_matrix(y_test, prediction))

# Save Model
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/spam_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("\nModel Saved Successfully!")
print("Location : model/spam_model.pkl")
print("Location : model/vectorizer.pkl")