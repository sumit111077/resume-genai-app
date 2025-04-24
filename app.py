import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Title of the App
st.title("🎯 AI Resume Bullet Generator")
st.write("Generate resume bullet points by entering your role and responsibilities.")

# User Inputs
role = st.text_input("Enter your job title", placeholder="e.g., Frontend Developer")
tasks = st.text_area("Enter your responsibilities", placeholder="e.g., Built UI components, Collaborated with backend team...")

def generate_bullets(role, tasks):
    prompt = f"""You are a professional resume writer. Convert the following responsibilities for a {role} into 3 compelling resume bullet points:

Responsibilities:
{tasks}

Resume Bullet Points:"""

    # Updated API call for v1
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=200
    )

    return response.choices[0].message['content']

# Button to trigger generation
if st.button("Generate Resume Bullet Points"):
    if role and tasks:
        with st.spinner("Generating bullet points..."):
            result = generate_bullets(role, tasks)
            st.subheader("✨ Generated Bullet Points:")
            st.markdown(result)
    else:
        st.warning("Please fill in both the job title and responsibilities.")
