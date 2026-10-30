# 🌱 Campus Eco-Footprint AI Tracker

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://applied-ai-projects-nstei7vudzvq2r2tc6phdv.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
# ⚡ Multi-Source Live API Data Summarizer & Pipeline

An automated data pipeline combining GitHub REST APIs, OpenAI Structured Outputs (Pydantic), and Google Apps Script Webhooks to extract, validate, and persist executive intelligence from unstructured developer commit feeds. 


## Architecture
1. **Extraction**: Ingests raw commit text from public GitHub repositories using requests.
2. **Schema Enforcement**: Leverages OpenAI beta.chat.completions.parse with strict Pydantic schemas to extract key_topic, sentiment, action_items, and urgency_level.
3. **Automated Loading**: Dispatches the validated JSON payload to an asynchronous Google Sheets webhook receiver deployed on Google Apps Script.

## Tech Stack
- **Language**: Python 3.12
- **Validation**: Pydantic v2
- **AI Engine**: OpenAI API (gpt-4o-mini)
- **Integration**: Google Apps Script Webhook receiver, Google Sheets

## Local Setup
1. Clone repository and navigate to the project:
   cd ai-summarizer
2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Set up .env:
   OPENAI_API_KEY=your_openai_api_key_here
5. Run the pipeline:
   python main.py
```mermaid
graph TD
    A[GitHub API] -->|Raw Commit Text| B(Python Data Pipeline)
    B -->|Schema Enforcement| C{OpenAI gpt-4o-mini}
    C -->|Structured JSON| B
    B -->|Webhook POST| D[(Google Sheets)]
    
    style A fill:#f9f9f9,stroke:#333,stroke-width:2px
    style C fill:#74aa9c,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#0f9d58,stroke:#333,stroke-width:2px,color:#fff
```
