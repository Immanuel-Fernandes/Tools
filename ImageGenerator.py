import base64
import requests
import streamlit as st
from PIL import Image
from io import BytesIO

# Function to generate image
def generate_image(prompt, api_key):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    
    body = {
        "steps": 40,
        "width": 1024,
        "height": 1024,
        "seed": 0,
        "cfg_scale": 5,
        "samples": 1,
        "text_prompts": [
            {
                "text": prompt,
                "weight": 1
            },
            {
                "text": "blurry, bad",
                "weight": -1
            }
        ],
    }
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    
    response = requests.post(url, headers=headers, json=body)
    
    if response.status_code != 200:
        st.error(f"API Error: {response.text}")
        return None
    
    data = response.json()
    image_data = base64.b64decode(data["artifacts"][0]["base64"])
    image = Image.open(BytesIO(image_data))
    return image

# Streamlit UI
st.title("Environment Image Generator")

prompt = st.text_input("Enter your environment-related prompt:")
#api_key = st.text_input("Enter your Stability AI API Key:", type="password")
api_key = 'sk-z6Kj18xNpMMFVOo4O93z8cCrxcYgXzTSSnvw3jlmtJu0p35z'

if st.button("Generate Image"):
    if not prompt or not api_key:
        st.warning("Please provide both prompt and API key.")
    else:
        with st.spinner('Generating image...'):
            image = generate_image(prompt, api_key)
            if image:
                st.image(image, caption='Generated Image', use_column_width=True)
                
                # Save the image for download
                img_buffer = BytesIO()
                image.save(img_buffer, format='PNG')
                img_buffer.seek(0)
                b64_img = base64.b64encode(img_buffer.read()).decode()

                href = f'<a href="data:file/png;base64,{b64_img}" download="generated_image.png">Download Image</a>'
                st.markdown(href, unsafe_allow_html=True)
