# 🤖 LeadFlow Automation System

An intelligent, end-to-end **Lead Management Automation System** that receives incoming leads via webhook, classifies and scores them using NLP models, extracts client details, summarizes requirements, and automatically generates context-aware replies — complete with supporting resources and CRM integration.

---

## 🚀 Features

✅ **Webhook-based Ingestion** – Receive leads from email or platforms  
✅ **Text Cleaning & Normalization** – Parse, clean, and structure raw email text  
✅ **Lead Classification & Scoring** – Categorize intent, assign priority, and compute lead_score  
✅ **Entity Extraction** – Identify names, companies, and contact info  
✅ **AI Summarization** – Summarize client requirements concisely  
✅ **Context Retrieval (RAG)** – Enrich replies using FAQs, product docs, or prior leads  
✅ **Auto Reply Generation** – Generate personalized, helpful responses using templates or LLMs  
✅ **Human-in-the-loop Option** – Review or approve AI replies before sending  
✅ **Comprehensive Logging** – Store embeddings, summaries, and decisions for audit  

---


---

## 🔁 Pipeline Steps

### **Step A — Ingest**
- Webhook endpoint accepts:
  - Raw email text (subject + body)
  - Sender email
  - Timestamp
  - Source platform metadata
- Immediately creates a lightweight lead record in DB with status `received`.

---

### **Step B — Preprocess**
- Convert HTML → Text via **BeautifulSoup**  
- Strip signature blocks (heuristic: lines starting with `--`)  
- Normalize encodings and lowercase text (original preserved)  
- Extract:
  - `subject`
  - First N characters → headline or preview snippet  

---

### **Step C — Classify & Lead-Scoring**
- Use an NLP classifier (Hugging Face model) to produce:
  - Category (`pricing`, `demo`, `support`, etc.)
  - Priority (`low`, `medium`, `high`)
  - Intent probability
- Compute `lead_score` based on:
  - Category weight  
  - Keywords (e.g., "urgent", "RFP", "budget")  
  - Email domain (company vs generic)  
  - Job title patterns (CEO, Manager, Director)  
- If `lead_score >= threshold` and auto-reply allowed → move to reply pipeline.  
  Else → route to human queue.

---

### **Step D — Extract Entities**
- Use a **NER model** (e.g., `dslim/bert-base-NER`) to extract:
  - Person names
  - Organization names
  - Locations  
- Regex extraction for:
  - Email addresses
  - Phone numbers  
- Use parsed entities to fill CRM fields automatically.

---

### **Step E — Summarize Client Requirements**
- Summarization model (e.g., `facebook/bart-large-cnn`):
  - Generates 1–3 sentence summary
  - Produces bullet list of explicit asks  
- Store summary and keywords in database.

---

### **Step F — Enrich with Retrieval**
- Generate embeddings via `sentence-transformers/all-MiniLM-L6-v2`
- Query vector database (FAISS / Chroma / Pinecone) for:
  - Similar previous leads  
  - FAQ snippets  
  - Product documentation  
- Retrieve top 3–5 relevant passages for reply context.

---

### **Step G — Generate Reply (RAG + Template)**
- Build a structured prompt containing:
  - **System message:** “You are a helpful sales assistant…”  
  - **Context:** lead summary + retrieved knowledge  
  - **Few-shot examples:** sample replies for tone/style  
  - **Instructions:** include next steps, links, and contact info  
- Optionally use template placeholders:
  - `{name}`, `{company}`, `{demo_link}`  
- Store reply candidate for approval or auto-send.

---

### **Step H — Send & Log**
- Send email via **SMTP** or **platform API**  
- Log:
  - Classifier output  
  - Reply text  
  - Embeddings  
  - Status (auto or manual)  
- Dashboard allows:
  - Approve / Edit / Resend  
  - Track analytics per lead  

---

## 🧩 Example Stack

| Component | Tool / Library |
|------------|----------------|
| Web Framework | FastAPI |
| Text Parsing | BeautifulSoup, Regex |
| NLP Models | Hugging Face Transformers |
| Summarization | BART / T5 |
| Embeddings | SentenceTransformers |
| Vector DB | FAISS / Chroma / Pinecone |
| Database | PostgreSQL / MongoDB |
| Email API | SMTP, Gmail API |
| Logging | JSON + PostgreSQL |

---

## 🧠 Model Recommendations

| Task | Model |
|------|-------|
| Classification | `facebook/bart-large-mnli` |
| NER | `dslim/bert-base-NER` |
| Summarization | `facebook/bart-large-cnn` |
| Embedding | `sentence-transformers/all-MiniLM-L6-v2` |
| Reply Generation | `mistralai/Mixtral-8x7B-Instruct` or `gpt-3.5-turbo` |

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/leadflow-automation.git
cd leadflow-automation
