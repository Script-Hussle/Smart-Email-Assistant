import os
import re
import spacy
import pandas as pd
from transformers import pipeline
from email import policy
from email.parser import BytesParser

# Load NLP Models
nlp = spacy.load("en_core_web_sm")  # Load spaCy model for Named Entity Recognition (NER)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # Load BART model for summarization
classifier = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")  # Load DistilBERT for emotion classification

# Function to classify email category based on keywords
def classify_email(text):
    categories = {
        "work": ["meeting", "deadline", "project", "client"],
        "personal": ["family", "friend", "birthday", "weekend"],
        "promotion": ["sale", "discount", "offer", "limited time"],
        "spam": ["win", "lottery", "free money", "urgent"]
    }
    for category, keywords in categories.items():
        if any(word in text.lower() for word in keywords):
            return category
    return "general"  # Default category if no keyword matches

# Function to summarize email content
def summarize_email(text):
    summary = summarizer(text, max_length=50, min_length=20, do_sample=False)
    return summary[0]['summary_text']  # Return the summarized text

# Function to extract important entities (Names, Dates, Locations, etc.) from email
def extract_entities(text):
    doc = nlp(text)
    return {ent.text: ent.label_ for ent in doc.ents}  # Return extracted entities as a dictionary

# Function to generate an auto-reply based on the emotion detected in email
def generate_reply(text):
    emotion = classifier(text)[0]['label']  # Detect emotion from email text
    if emotion == "joy":
        return "Thank you! Looking forward to it."
    elif emotion == "anger":
        return "I understand your concern. Let's discuss further."
    else:
        return "Got it! I'll get back to you soon."

# Function to process an email file and extract relevant information
def process_email(file_path):
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)  # Parse email content
    text = msg.get_body(preferencelist=('plain')).get_content()  # Extract email body text
    category = classify_email(text)  # Classify email category
    summary = summarize_email(text)  # Summarize email content
    entities = extract_entities(text)  # Extract important entities
    auto_reply = generate_reply(text)  # Generate an appropriate reply
    return {
        "Category": category,
        "Summary": summary,
        "Entities": entities,
        "Auto Reply": auto_reply
    }

# Example Run: Process a sample email file
if __name__ == "__main__":
    email_data = process_email("sample_email.eml")  # Provide the path to the email file
    print(pd.DataFrame([email_data]))  # Print extracted email information as a DataFrame
