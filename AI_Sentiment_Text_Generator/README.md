# AI Sentiment Text Generator 🧠

## Overview
This project is built for the Remote ML Internship Assessment.  
It detects the **sentiment** of a user's input and generates a **paragraph or essay aligned with that sentiment** using Google Gemini via LangChain.  
The system allows users to either automatically detect sentiment or manually select it, with adjustable output length.

---

## Features
- Automatic sentiment detection (positive / negative / neutral)  
- Manual sentiment override option  
- Adjustable paragraph length (short, medium, long)  
- Interactive Streamlit UI  
- Uses LangChain with Google Gemini generative AI model  

---

## Tech Stack
- Python  
- LangChain  
- Google Generative AI (Gemini)  
- TextBlob (for sentiment analysis)  
- Streamlit (frontend)  
- python-dotenv (API key management)  

---

## Setup Instructions
1. Clone the repository or extract the ZIP file.  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


"Add your Google API key in .env before running the app."