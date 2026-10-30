# ⚡ Multi-Source Live API Data Summarizer & Pipeline

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)

An automated data pipeline combining GitHub REST APIs, OpenAI Structured Outputs (Pydantic), and Google Apps Script Webhooks to extract, validate, and persist executive intelligence from unstructured developer commit feeds.

## Architecture
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

## Tech Stack
- **Language**: Python 3.12
- **Validation**: Pydantic v2
- **AI Engine**: OpenAI API (gpt-4o-mini)
- **Integration**: Google Apps Script Webhook receiver, Google Sheets
