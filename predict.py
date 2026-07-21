import joblib

# Load Model
model = joblib.load("model/spam_model.pkl")

# Load Vectorizer
vectorizer = joblib.load("model/vectorizer.pkl")

print("=" * 50)
print("      SPAM EMAIL CLASSIFIER")
print("=" * 50)

while True:

    message = input("\nEnter Email/SMS (Type exit to quit): ")

    if message.lower() == "exit":
        print("\nThank You!")
        break

    message_vector = vectorizer.transform([message])

    prediction = model.predict(message_vector)

    if prediction[0] == "spam":
        print("\nPrediction : SPAM")
    else:
        print("\nPrediction : NOT SPAM (HAM)")