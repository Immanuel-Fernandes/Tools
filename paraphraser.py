import streamlit as st
from transformers import pipeline

# Streamlit interface
st.title("Text Paraphraser")

st.write("Enter a sentence to paraphrase:")

# Load the paraphrasing pipeline
paraphrase_pipeline = pipeline("text2text-generation", model="facebook/bart-large-cnn")

# Input text area
input_text = st.text_area("Input Text")

# Paraphrase button
if st.button("Paraphrase"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Generate paraphrased text
        paraphrased_text = paraphrase_pipeline(input_text, max_length=100, top_k=5)[0]['generated_text']

        # Display paraphrased text
        st.subheader("Paraphrased Text:")
        st.write(paraphrased_text)
