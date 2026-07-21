# 📧 Spam Email Classifier

A Machine Learning project that classifies an Email or SMS message as **Spam** or **Not Spam (Ham)** using **Natural Language Processing (NLP)** and the **Multinomial Naive Bayes** algorithm.

---

## 📖 Project Overview

Spam messages often contain advertisements, phishing links, scams, or other unwanted content. This project uses Machine Learning to automatically identify whether a message is spam or legitimate.

The model is trained on the **SMS Spam Collection Dataset** using **TF-IDF Vectorization** and **Multinomial Naive Bayes**, then deployed with a simple and interactive **Streamlit** web application.

---

## 🎯 Objectives

- Detect spam and legitimate (ham) messages.
- Learn the fundamentals of Machine Learning and NLP.
- Build a real-world text classification project.
- Create a user-friendly web application.
- Understand the complete ML workflow from training to deployment.

---

## ✨ Features

- 📧 Spam Message Detection
- ✅ Ham (Not Spam) Detection
- 📝 TF-IDF Text Vectorization
- 🤖 Multinomial Naive Bayes Classifier
- 🌐 Interactive Streamlit Web Interface
- 💻 Command Line Prediction Support
- ⚡ Fast and Accurate Predictions

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Joblib
- Streamlit
- Matplotlib

---

## 📂 Dataset

**Dataset:** SMS Spam Collection Dataset

The dataset contains two columns:

| Column | Description |
|---------|-------------|
| **v1** | Label (spam / ham) |
| **v2** | Email or SMS message |

---

## 📁 Project Structure

```
Spam-Email-Classifier
│
├── dataset/
│   └── spam.csv
├── model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
├── app.py
├── train_model.py
├── predict.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/Spam-Email-Classifier.git
```

### 2. Open the Project Folder

```bash
cd Spam-Email-Classifier
```

### 3. Install Required Libraries

```bash
py -m pip install -r requirements.txt
```

---

## 🚀 Train the Model

Run:

```bash
py train_model.py
```

This will:

- Load the dataset
- Clean the data
- Convert text into numerical features using TF-IDF
- Train the Machine Learning model
- Save the trained model and vectorizer

Saved files:

```
model/spam_model.pkl
model/vectorizer.pkl
```

---

## 💻 Command Line Prediction

Run:

```bash
py predict.py
```

Example:

```
Enter Email/SMS:

Congratulations!
You have won ₹50,000.
Click here to claim your prize.

Prediction:
SPAM
```

---

## 🌐 Run the Streamlit Application

```bash
py -m streamlit run app.py
```

The application will open automatically in your browser.

If it doesn't, open:

```
http://localhost:8501
```

---

## 🔄 Project Workflow

```
SMS Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Train/Test Split
      │
      ▼
Multinomial Naive Bayes
      │
      ▼
Model Evaluation
      │
      ▼
Save Model (.pkl)
      │
      ▼
Spam Prediction
```

---

## 📊 Machine Learning Algorithm

### Multinomial Naive Bayes

Multinomial Naive Bayes is a supervised Machine Learning algorithm widely used for text classification tasks such as:

- Spam Detection
- Sentiment Analysis
- News Classification
- Document Categorization

It is fast, efficient, and performs exceptionally well on text data.

---

## 📈 Expected Accuracy

**97% – 99%**

*(Accuracy may vary depending on the dataset and preprocessing.)*

---

## 📷 Sample Predictions

### Example 1

**Input**

```
Congratulations!
You have won ₹50,000.
Click here to claim your prize.
```

**Output**

```
🚫 SPAM
```

---

### Example 2

**Input**

```
Hi Param,
Let's meet tomorrow at 5 PM.
```

**Output**

```
✅ NOT SPAM (HAM)
```

---

## 🚀 Future Improvements

- Gmail API Integration
- Multi-language Support
- Deep Learning Models (LSTM/BERT)
- Mobile Application
- Cloud Deployment
- Real-time Email Filtering

---

## 👨‍💻 Author

**Param Chavada**

B.Tech – Artificial Intelligence & Data Science

JECRC Foundation, Jaipur

GitHub: https://github.com/param7399

LinkedIn: https://linkedin.com/in/paramchavada

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgements

- SMS Spam Collection Dataset
- Scikit-learn Documentation
- Streamlit
- Python Community

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Thank you for visiting this repository!
