import streamlit as st
import joblib

# Load Model
model = joblib.load("model/spam_model.pkl")

# Load Vectorizer
vectorizer = joblib.load("model/vectorizer.pkl")

st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Spam Email Classifier")

st.write(
    "This Machine Learning application predicts whether an Email or SMS is Spam or Not Spam."
)

message = st.text_area("Enter Email or SMS")

if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:

        message_vector = vectorizer.transform([message])

        prediction = model.predict(message_vector)

        if prediction[0] == "spam":
            st.error("🚫 SPAM MESSAGE")
        else:
            st.success("✅ NOT SPAM (HAM)")

st.markdown("---")
st.write("Developed by Param Chavada")