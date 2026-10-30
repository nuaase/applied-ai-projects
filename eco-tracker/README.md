# 🌱 Campus Eco-Footprint AI Tracker

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://applied-ai-projects-nstei7vudzvq2r2tc6phdv.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

An interactive sustainability dashboard built with **Streamlit**, **Pandas**, and **OpenAI GPT-4o-mini** that logs resource consumption, tracks emission trends, and generates tailored operational carbon reduction reports.

## Features
- **Daily Activity Logging**: Form interface capturing Electricity, Food Waste, Paper, and Transport usage with dynamic CO2 calculation.
- **Trend Analytics**: Real-time time-series emissions visualization powered by Plotly.
- **AI Sustainability Insights**: Dynamically injects aggregate campus emission metrics and top impact drivers into OpenAI's reasoning model to return actionable reduction strategies.

## Tech Stack
- **Frontend / Dashboard**: Streamlit, Plotly Express
- **Data Layer**: Pandas, CSV storage
- **AI / LLM Integration**: OpenAI API (gpt-4o-mini) via context-grounded prompting
