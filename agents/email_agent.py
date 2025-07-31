import streamlit as st
import google.generativeai as genai

# Configure Gemini API key securely via Streamlit secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Function to generate response
def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="Email Responder with Gemini")
st.title("📧 AI Email Responder")

email_text = st.text_area("Paste the email content:")
tone = st.selectbox("Select the tone of your reply:", ["Formal", "Friendly", "Professional", "Apologetic", "Enthusiastic"])

if st.button("Generate Reply"):
    if email_text:
        reply = generate_email_response(email_text, tone)
        st.success("✅ Generated Reply:")
        st.write(reply)
    else:
        st.warning("Please enter the email text.")
