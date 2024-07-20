import os
import streamlit as st
from openai import OpenAI

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set the OpenAI API key

# Settings for the OpenAI model
settings = {
    "model": "gpt-4",
    "temperature": 0,
    # ... more settings if needed
}


def get_openai_response(user_message):
    response = client.chat.completions.create(model=settings["model"],
    messages = [
        {
            "role": "system",
            "content": "You are a helpful bot, you always provide programming solutions in python in English",
        },
        {
            "role": "user",
            "content": user_message,
        },
    ],
    temperature=settings["temperature"])
    return response.choices[0].message.content


st.title("Chat with TechMalooBot")
user_message = st.text_input("Enter your message:")
if st.button("Send"):
    if user_message:
        with st.spinner("Generating response..."):
            try:
                response = get_openai_response(user_message)
                st.write(response)
            except Exception as e:
                st.write(f"Error: {e}")
    else:
        st.write("Please enter a message.")


