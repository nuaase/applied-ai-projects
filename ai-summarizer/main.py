import os
import requests
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1. Define the exact JSON structure we want back from the AI
class ExecutiveSummary(BaseModel):
    key_topic: str
    sentiment: str
    action_items: list[str]
    urgency_level: str

# 2. Fetch live unstructured text (top 5 recent commits from Streamlit's GitHub repo)
def fetch_raw_data() -> str:
    url = "https://api.github.com/repos/streamlit/streamlit/commits"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    commits = response.json()[:5]
    return "\n---\n".join([c["commit"]["message"] for c in commits])

# 3. Pass the raw text to OpenAI and enforce the Pydantic schema
def generate_summary(raw_text: str) -> ExecutiveSummary:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a data summarization bot. Extract the main themes from this raw feed.",
            },
            {"role": "user", "content": raw_text},
        ],
        response_format=ExecutiveSummary,
    )
    return completion.choices[0].message.parsed

# 4. Run the pipeline and forward to Google Sheets
if __name__ == "__main__":
    print("1. Fetching live data from GitHub...")
    raw_data = fetch_raw_data()

    print("2. Generating structured summary with OpenAI...")
    structured_summary = generate_summary(raw_data)
    payload = structured_summary.model_dump()
    
    print("\n✅ Structured JSON Output from AI:")
    print(payload)

webhook_url = "https://script.google.com/macros/s/AKfycbyxFDF4IybnCxpGrtDExNKYp7n4FiFwb7d3_IEHtSOEpoyJ5iWOKvk16a2EJRT80A/exec"
print("\n3. Sending data to Google Sheets...")
res = requests.post(webhook_url, json=payload, timeout=15)
print(f"🎉 Google Sheets Response ({res.status_code}): {res.text}")