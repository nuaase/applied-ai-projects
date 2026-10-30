import os
from datetime import date
import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load environment variables & initialize OpenAI client
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key and "OPENAI_API_KEY" in st.secrets:
    api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "eco_data.csv")

# Emission conversion factors (kg CO2 per unit)
EMISSION_FACTORS = {
    "Electricity (kWh)": ("Electricity", "kWh", 0.43),
    "Food Waste (kg)": ("Food Waste", "kg", 2.50),
    "Paper Used (kg)": ("Paper Used", "kg", 1.30),
    "Transport (km)": ("Transport", "km", 0.21),
}

st.set_page_config(page_title="Campus Eco-Footprint Tracker", page_icon="🌱")
st.title("🌱 Campus Eco-Footprint Tracker")

# 2. Load existing CSV data
df = pd.read_csv(CSV_FILE)

# 3. Input Form
with st.form("log_activity"):
    activity_date = st.date_input("Date", date.today())
    activity_choice = st.selectbox("Activity", list(EMISSION_FACTORS.keys()))
    value = st.number_input("Amount", min_value=0.0, step=1.0)
    submitted = st.form_submit_button("Log Activity")

    if submitted and value > 0:
        act_name, unit, factor = EMISSION_FACTORS[activity_choice]
        co2_est = round(value * factor, 2)

        new_row = pd.DataFrame([{
            "Date": str(activity_date),
            "Activity_Type": act_name,
            "Value": value,
            "Unit": unit,
            "CO2_Estimate_kg": co2_est,
        }])

        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)
        st.success(f"Logged {value} {unit} of {act_name} ({co2_est} kg CO2) on {activity_date}!")

# 4. Data Visualization
st.subheader("Your Footprint Trends")
fig = px.bar(
    df,
    x="Date",
    y="CO2_Estimate_kg",
    color="Activity_Type",
    title="Daily CO2 Emissions (kg)",
)
st.plotly_chart(fig, use_container_width=True)

# 5. AI Insights Engine
if st.button("Generate AI Sustainability Report"):
    with st.spinner("Analyzing emissions data..."):
        total_co2 = df["CO2_Estimate_kg"].sum()
        top_driver = df.groupby("Activity_Type")["CO2_Estimate_kg"].sum().idxmax()

        prompt = (
            f"Our school campus has emitted {total_co2:.2f} kg of CO2 recently. "
            f"The biggest driver is {top_driver}. "
            "Give 3 highly practical, low-cost tips to reduce this specific emission source."
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )

        st.info(response.choices[0].message.content)