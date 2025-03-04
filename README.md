# Smart Email Assistant

## 📌 Overview
Smart Email Assistant is a Python-based AI tool that categorizes emails, summarizes content, extracts important entities, and generates auto-replies using NLP models from Hugging Face.

## ✨ Features
- 📧 **Email Categorization**: Detects email type (Work, Personal, Promotion, Spam).
- 📝 **Email Summarization**: Extracts key points from long emails.
- 🔍 **Entity Extraction**: Identifies important names, dates, and places.
- 🤖 **Auto-Reply Generator**: Suggests replies based on the email's sentiment.

## 🚀 Installation
### 1️⃣ **Clone the Repository**
```sh
https://github.com/Script-Hussle/smart-email-assistant.git
cd smart-email-assistant
```
### 2️⃣ **Create a Virtual Environment (Optional, Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## 🛠 Usage
### Process an Email File
```sh
python smartemailassistant.py sample_email.eml
```
The script will output the email's category, summary, extracted entities, and a suggested auto-reply.

## 📂 Project Structure
```
smart-email-assistant/
│── smartemailassistant.py   # Main script
│── requirements.txt         # Dependencies
│── sample_email.eml         # Sample email file
│── README.md                # Documentation
```

## 💡 Future Improvements
- 📩 Gmail API integration to fetch emails
- 🌍 Multilingual support for different languages
- 📊 Web-based UI with Streamlit

## 🏆 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License
This project is open-source under the MIT License.
