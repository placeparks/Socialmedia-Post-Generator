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
            engine="gpt-3.5-turbo-instruct",
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

# Add custom CSS for footer
footer_style = """
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
padding: 10px;
background-color: rgba(255, 255, 255, 0.5);  /* Semi-transparent light background */
color: #000;                                  /* Dark text for visibility */
border-top: 1px solid #000;                   /* Border to distinguish the footer */
z-index: 1000;                                /* Ensures it stays on top of other elements */
"""

# Footer
st.markdown(
    '<div style="{}">Developed by Mirac.eth<br>Contact: mirac.eth@ethereum.email</div>'.format(footer_style),
    unsafe_allow_html=True
)
