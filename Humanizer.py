import streamlit as st
import re
import random

# Function to humanize text
def humanize_text(text):
    contractions = {
        "it is": "it's",
        "it can be": "it can",
        "it has": "it's",
        "you are": "you're",
        "we are": "we're",
        "they are": "they're",
        "do not": "don't",
        "does not": "doesn't",
        "did not": "didn't",
        "will not": "won't",
        "would not": "wouldn't",
        "cannot": "can't",
        "could not": "couldn't",
        "should not": "shouldn't",
        "might not": "mightn't",
        "must not": "mustn't",
        "let us": "let's",
    }

    personal_touches = [
        "you know",
        "I think",
        "honestly",
        "to be honest",
        "believe it or not",
        "if you ask me",
        "in my opinion",
    ]

    for k, v in contractions.items():
        text = re.sub(r'\b' + re.escape(k) + r'\b', v, text, flags=re.IGNORECASE)

    sentences = re.split(r'(?<=[.!?]) +', text)
    for i, sentence in enumerate(sentences):
        if random.random() < 0.3:
            personal_touch = random.choice(personal_touches)
            sentences[i] = f"{personal_touch}, {sentence.lower()}"
    
    text = ' '.join(sentences)
    return text

# Streamlit interface
st.title("AI Text Humanizer")

st.write("This app takes AI-generated text and makes it sound more human-like by using contractions and personal touches.")

ai_text = st.text_area("Enter AI-generated text:", height=200)
if st.button("Humanize Text"):
    if ai_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        humanized_text = humanize_text(ai_text)
        st.subheader("Humanized Text:")
        st.write(humanized_text)
