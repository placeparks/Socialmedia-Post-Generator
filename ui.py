import streamlit as st
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# OpenAI API setup
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_social_media_post(theme, platform):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Create a creative and engaging {platform} post about {theme}.",
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Streamlit UI
st.title('Social Media Post Generator')

theme = st.text_input('Enter the theme or keyword for your post:')
platform = st.selectbox('Select the social media platform:', ['Twitter', 'Facebook', 'Instagram'])

if st.button('Generate Post'):
    post = generate_social_media_post(theme, platform)
    st.text_area('Generated Post:', post, height=150)