import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer

# Initialize Porter Stemmer
ps = PorterStemmer()

# Function to preprocess text
def transform_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Tokenize text
    text = nltk.word_tokenize(text)

    y = []
    # Remove non-alphanumeric characters
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    # Remove stopwords and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    # Stemming
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# Load the TF-IDF vectorizer
tfidf = pickle.load(open('vectorizer.pkl','rb'))
# Load the pre-trained model
model = pickle.load(open('model.pkl','rb'))

# Set up Streamlit UI
st.title("Email/SMS Spam Classifier")
input_sms = st.text_area("Enter the message")

# Prediction button
if st.button('Predict'):
    # Preprocess input text
    transformed_sms = transform_text(input_sms)
    # Vectorize preprocessed text
    vector_input = tfidf.transform([transformed_sms])
    # Make prediction
    result = model.predict(vector_input)[0]
    # Display prediction
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
