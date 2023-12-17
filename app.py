import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

def generate_social_media_post(theme, platform):
    """
    Generates a social media post based on the given theme and platform.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Create a creative and engaging {platform} post about {theme}.",
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

def main():
    # Load the API key from environment variable
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # Input from the user
    theme = input("Enter the theme or keyword for your post: ")
    platform = input("Enter the social media platform (Twitter, Facebook, Instagram): ")

    # Generate and display the social media post
    post = generate_social_media_post(theme, platform)
    print("\nGenerated Post:")
    print(post)

if __name__ == "__main__":
    main()
