import language_tool_python
import streamlit as st

# Function to improve and correct sentences
def improve_sentences(text):
    tool = language_tool_python.LanguageTool('en-US')  # Use 'en' for British English
    matches = tool.check(text)
    
    # Apply corrections to the text
    corrected_text = tool.correct(text)
    
    return corrected_text

# Streamlit interface
st.title("Sentence Improver and Grammar Checker")

st.write("This tool improves sentences and corrects grammatical errors.")

input_text = st.text_area("Enter your text:", height=200)
if st.button("Improve Text"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        improved_text = improve_sentences(input_text)
        st.subheader("Improved Text:")
        st.write(improved_text)
