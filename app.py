import streamlit as st
import re
import random
from transformers import pipeline
import language_tool_python

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

# Function to paraphrase text
def paraphrase_text(text):
    paraphrase_pipeline = pipeline("text2text-generation", model="facebook/bart-large-cnn")
    paraphrased_text = paraphrase_pipeline(text, max_length=100, top_k=5)[0]['generated_text']
    return paraphrased_text

# Function to improve and correct sentences
def improve_sentences(text):
    tool = language_tool_python.LanguageTool('en-US')  # Use 'en' for British English
    matches = tool.check(text)
    corrected_text = tool.correct(text)
    return corrected_text

# Streamlit interface
st.title("Text Enhancement Tool")

# Feature selection
selected_feature = st.selectbox("Select a feature:", ("AI Text Humanizer", "Text Paraphraser", "Sentence Improver"))

if selected_feature == "AI Text Humanizer":
    st.write("This feature makes AI-generated text sound more human-like.")
    ai_text = st.text_area("Enter AI-generated text:", height=200)
    if st.button("Humanize Text"):
        if ai_text.strip() == "":
            st.warning("Please enter some text.")
        else:
            humanized_text = humanize_text(ai_text)
            st.subheader("Humanized Text:")
            st.write(humanized_text)

elif selected_feature == "Text Paraphraser":
    st.write("This feature paraphrases input text.")
    input_text = st.text_area("Enter a sentence to paraphrase:", height=200)
    if st.button("Paraphrase"):
        if input_text.strip() == "":
            st.warning("Please enter some text.")
        else:
            paraphrased_text = paraphrase_text(input_text)
            st.subheader("Paraphrased Text:")
            st.write(paraphrased_text)

elif selected_feature == "Sentence Improver":
    st.write("This feature improves and corrects sentences.")
    input_text = st.text_area("Enter your text:", height=200)
    if st.button("Improve Text"):
        if input_text.strip() == "":
            st.warning("Please enter some text.")
        else:
            improved_text = improve_sentences(input_text)
            st.subheader("Improved Text:")
            st.write(improved_text)
