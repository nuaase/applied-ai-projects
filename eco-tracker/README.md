# 🌱 Campus Eco-Footprint AI Tracker

An interactive sustainability dashboard built with Streamlit, Pandas, and OpenAI GPT-4o-mini that logs resource consumption, tracks emission trends, and generates tailored operational carbon reduction reports.

## Features
- **Daily Activity Logging**: Form interface capturing Electricity, Food Waste, Paper, and Transport usage with dynamic CO2 calculation.
- **Trend Analytics**: Real-time time-series emissions visualization powered by Plotly.
- **AI Sustainability Insights**: Dynamically injects aggregate campus emission metrics and top impact drivers into OpenAI's reasoning model to return actionable reduction strategies.

## Tech Stack
- **Frontend / Dashboard**: Streamlit, Plotly Express
- **Data Layer**: Pandas, CSV storage
- **AI / LLM Integration**: OpenAI API (gpt-4o-mini) via context-grounded prompting

## Local Setup
1. Clone repository and navigate to the project:
   cd eco-tracker
2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate
3. Install dependencies:
   pip install -r requirements.txt
4. Configure .env in the root directory:
   OPENAI_API_KEY=your_openai_api_key_here
5. Launch the application:
   streamlit run app.py
