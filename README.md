# Applied AI & Machine Learning Engineering Portfolio

A collection of production-oriented AI, Computer Vision, and Data Engineering pipelines built in Python. This repository houses modular applications leveraging **Agentic LLM Workflows**, **Structured Schema Validation**, and **Interactive Analytics**.

---

## 📂 Repository Index

| Project Directory / Repo | Core Focus | Tech Stack |
| :--- | :--- | :--- |
| **[`./eco-tracker`](./eco-tracker)** | **Campus Eco-Footprint AI Tracker** — Interactive CO₂ analytics dashboard with an embedded LLM sustainability agent (`gpt-4o-mini`) for dynamic emission driver analysis. | `Python` `Streamlit` `OpenAI API` `Plotly` `Pandas` |
| **[`./ai-summarizer`](./ai-summarizer)** | **Automated API Data Summarizer Pipeline** — Event-driven ETL pipeline ingesting live GitHub REST API commit feeds, enforcing strict Pydantic schema validation via OpenAI Structured Outputs, and dispatching payloads via webhooks. | `Python` `Pydantic` `OpenAI API` `REST APIs` `Webhooks` |
| **[`autonomous-vision-pipeline`](https://github.com/nuaase/autonomous-vision-pipeline)** | **Autonomous Vehicle Perception & Spatial Alert Pipeline** — Real-time monocular camera perception node using PyTorch (YOLOv8) and OpenCV for pinhole depth estimation, ego-lane spatial filtering, and forward collision telemetry logging. | `PyTorch` `YOLOv8` `OpenCV` `Pandas` `NumPy` |

---

## 🏗️ Architecture Highlights

### 1. Campus Eco-Footprint AI Tracker (`./eco-tracker`)
* **Real-Time Telemetry & Visualization:** Tracks resource consumption metrics and visualizes carbon emission trends using `Plotly` and `Streamlit`.
* **Context-Grounded LLM Agent:** Dynamically injects aggregated dataframe statistics into `gpt-4o-mini` prompts to generate targeted, quantitative carbon reduction strategies.

### 2. Automated API Data Summarizer (`./ai-summarizer`)
* **Deterministic LLM Outputs:** Uses `Pydantic` models with OpenAI Structured Outputs to guarantee 100% schema-compliant JSON extractions from raw developer commit logs.
* **Automated Downstream Delivery:** Pushes validated telemetry payloads asynchronously to Google Sheets via a custom Apps Script webhook.

---

## 🚀 Quick Start

Clone the repository and navigate to either project directory to install its dependencies:

```bash
git clone [https://github.com/nuaase/applied-ai-projects.git](https://github.com/nuaase/applied-ai-projects.git)
cd applied-ai-projects/eco-tracker  # or cd ai-summarizer
pip install -r requirements.txt
