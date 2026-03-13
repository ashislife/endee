# app.py
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from textblob import TextBlob
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# ---------------------- Streamlit Page Config ----------------------
st.set_page_config(page_title="AI Sentiment Text Generator", page_icon="🧠", layout="wide")
st.title("🧠 AI Sentiment-Based Text Generator")
st.markdown("Generate intelligent, **sentiment-aligned** text using Google Gemini + LangChain.")

# ---------------------- Sidebar Controls ----------------------
st.sidebar.header("⚙️ Settings")

model_choice = st.sidebar.radio(
    "Choose Model",
    ["models/gemini-2.0-flash-001 (fast)", "gemini-2.5-pro (accurate)"]
)
model = ChatGoogleGenerativeAI(
    model="models/gemini-2.0-flash-001" if "flash" in model_choice else "models/gemini-2.5-pro"
)

length_choice = st.sidebar.select_slider(
    "Select output length:",
    options=["short", "medium", "long"],
    value="medium"
)

manual_sentiment = st.sidebar.toggle("🔧 Manually select sentiment", value=False)
if manual_sentiment:
    sentiment = st.sidebar.radio("Choose sentiment:", ["positive", "neutral", "negative"])
else:
    sentiment = None

st.sidebar.markdown("---")
st.sidebar.info("💡 Tip: You can either let AI detect sentiment automatically, or manually choose it.")

# ---------------------- Main Input Area ----------------------
prompt = st.text_area("💬 Enter your text prompt:", placeholder="e.g. I lost my job today but I’m staying hopeful.")

if st.button("🚀 Generate Text"):
    if not prompt.strip():
        st.warning("Please enter a prompt first.")
    else:
        # Detect sentiment automatically (if not manual)
        if not manual_sentiment:
            sentiment_score = TextBlob(prompt).sentiment.polarity
            if sentiment_score > 0:
                sentiment = "positive"
            elif sentiment_score < 0:
                sentiment = "negative"
            else:
                sentiment = "neutral"

        st.info(f"**Detected Sentiment:** `{sentiment}`")

        # Build generation instruction
        instructions = {
            "short": "Write a short paragraph (2–3 sentences)",
            "medium": "Write a medium-length paragraph (4–6 sentences)",
            "long": "Write a detailed essay (8–10 sentences)"
        }

        # Generate text using model
        with st.spinner("🧠 Generating AI text..."):
            response = model.invoke(
                f"{instructions[length_choice]} in a {sentiment} tone based on the following prompt:\n\n{prompt}"
            )

        # ---------------------- Output Section ----------------------
        st.subheader("✨ Generated Text")
        st.write(response.content)

        # ---------------------- Feedback Section ----------------------
        st.markdown("---")
        st.markdown("#### 📝 Feedback (optional)")
        feedback = st.text_input("Was the generated text accurate or relevant?")
        if st.button("Submit Feedback"):
            st.success("✅ Thanks for your feedback!")



