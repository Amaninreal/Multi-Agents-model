# 📘 Multi-AI Test Agent System

This project uses CrewAI, LangChain, and OpenAI to create a multi-agent pipeline that automates the following:

1. **Requirement Summarization**  
2. **Test Case Generation**  
3. **Gap Analysis**

---

## 💪 Project Structure

```
multi-ai-test-agent-system/
├── agents/
│   ├── RequirementSummarizer.py
│   ├── TestCaseGenerator.py
│   └── GapAnalyzer.py
├── flows/
│   └── crewai_testflow.py
├── .env
├── README.md
└── requirements.txt
```

---

## 🚀 How It Works

- **Step 1:** `RequirementSummarizer` summarizes a given API requirement.
- **Step 2:** `TestCaseGenerator` uses that summary to generate functional and edge test cases.
- **Step 3:** `GapAnalyzer` reviews the generated test cases and identifies missing ones.

The entire process is orchestrated using `Crew` from `crewai`.

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Amaninreal/Multi-Agents-model.git
cd Multi-Agents-model
```

### 2. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If you see deprecation warnings for `ChatOpenAI`, install:
```bash
pip install -U langchain-openai
```

---

## 🔐 Environment Variables

Create a `.env` file in the root:

```env
OPENAI_API_KEY=sk-...
```

Make sure this file is **not committed** by adding `.env` to `.gitignore`.

---

## ▶️ Running the Flow

```bash
python flows/crewai_testflow.py
```

Output will display each agent's contribution and a final result.

---

## 📌 Requirements File Example

`requirements.txt`

```text
crewai==0.22.4
langchain-openai==0.1.1
python-dotenv==1.0.1
```