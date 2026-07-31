# MotionForge AI ⚖️

> **AI-Powered Motion to Compel Document Drafting Engine**  
> Automatically generates formal legal pleading drafts following uploaded client format templates, incorporates case facts, performs transparent legal web searches, and visualizes multi-agent execution steps.

---

## 🌟 Overview

**MotionForge AI** is an advanced legal tech application designed to solve complex discovery dispute drafting. The application accepts a **Format/Template Document** (which defines court caption layout, section hierarchy, font guidelines, line numbering, and signature blocks) alongside a **Reference Case Document** (containing case facts, parties, and disputed interrogatories/RFPs).

Using a **4-Layer Agent Architecture**, the system parses both inputs, performs live web searches for relevant civil procedure rules and case law precedents, and synthesizes a high-fidelity **Motion to Compel** pleading draft that matches the exact template format.

---

## ✨ Key Features

- 📑 **Dual Document Uploader**
  - **Upload Format Template**: Parses client guidelines, court caption styles, section titles, typography, line numbering, and signature lines.
  - **Upload Case Reference Document**: Extracts Plaintiff/Defendant names, Court name, Case Number, Judge, and specific discovery items in dispute (Interrogatories & Requests for Production).
  - **Built-in Presets**: Instant load presets for *US District Court (FRCP Rule 37)* and *California Superior Court Discovery Motions*.

- 🤖 **4-Stage Multi-Agent Pipeline**
  1. **Layer 1: Client Guideline & Format Scraper Agent**: Learns structural guidelines and caption formatting rules.
  2. **Layer 2: Case Fact & Context Extractor Agent**: Parses factual background and disputed items.
  3. **Layer 3: Legal Web Search & Research Layer**: Queries web/legal databases for FRCP Rule 37, state codes, local court rules, and landmark case precedents (*Societe Internationale v. Rogers*).
  4. **Layer 4: Final Motion Draft Synthesizer Agent**: Combines format rules, case facts, and search citations into a publication-ready draft.

- 📊 **Real-Time Agent Stepper & Terminal Log UI**
  - Displays live progress for all 4 agent layers with status indicators.
  - Expandable agent thought log detailing internal reasoning and timestamps.

- 🌐 **Dedicated Web Search Sources UI Block**
  - Transparent UI block listing all web search sources used to make the draft.
  - Displays domain badges (`law.cornell.edu`, `supreme.justia.com`, `cand.uscourts.gov`), preview snippets, rule tags, and direct links.

- 📝 **Formatted Motion Draft Studio**
  - **Pleading Paper Viewer**: Formatted legal pleading paper with 28-line numbering, caption box, and formal sections.
  - **Format Adherence Score**: Live rating (e.g. 98.5%) measuring match accuracy against the input template.
  - **Export Tools**: Copy to Clipboard, Download as `.txt`, Raw Text view, and Print/Save as PDF.

---

## 🛠️ Technology Stack

### Backend
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.10+)
- **Server**: Uvicorn (ASGI)
- **Data Validation**: Pydantic v2
- **Web & Search Layer**: HTTPX & BeautifulSoup4

### Frontend
- **Framework**: React 18 + Vite
- **Styling**: Custom CSS Design Tokens (Glassmorphic dark mode, legal pleading layout, responsive grid)
- **Icons**: Lucide React

---

## 📁 Project Structure

```
DemandDraft/
├── backend/                        # FastAPI Backend Application
│   ├── main.py                     # FastAPI app entry point & CORS configuration
│   ├── schemas.py                  # Pydantic data schemas & request/response models
│   ├── requirements.txt            # Python dependencies list
│   ├── routers/
│   │   └── motion_router.py        # API endpoints (/api/generate-motion, /api/health)
│   └── services/
│       ├── format_scraper.py       # Layer 1: Format Scraper Agent
│       ├── fact_extractor.py       # Layer 2: Fact Extractor Agent
│       ├── web_search_layer.py     # Layer 3: Legal Web Search Layer
│       └── draft_synthesizer.py    # Layer 4: Final Draft Synthesizer Agent
│
├── src/                            # React Frontend Application
│   ├── App.jsx                     # Main application component & layout state
│   ├── main.jsx                    # React DOM entry point
│   ├── index.css                   # Custom CSS design system & glassmorphism
│   ├── data/
│   │   └── presets.js              # Sample format templates & reference files
│   ├── services/
│   │   └── api.js                  # Frontend API wrapper connecting to FastAPI
│   └── components/
│       ├── Header.jsx              # Application header & status indicator
│       ├── DocumentUploadSection.jsx # Dual document upload dropzones
│       ├── AgentStepper.jsx        # Live 4-layer step execution timeline & logs
│       ├── SearchSourcesBlock.jsx  # Dedicated web search sources UI block
│       └── DraftStudio.jsx         # Legal pleading preview & document exporter
│
├── index.html                      # HTML entry point with Google Fonts
├── package.json                    # Node.js dependencies
└── vite.config.js                  # Vite server & backend API proxy configuration
```

---

## 🚀 Quick Start Guide

### Prerequisites
- **Python**: 3.10 or higher
- **Node.js**: v18 or higher (npm v9+)

---

### Step 1: Set Up & Launch FastAPI Backend

1. Navigate to the project root directory:
   ```bash
   cd DemandDraft
   ```

2. Create and activate a Python Virtual Environment:
   ```powershell
   # Windows (PowerShell)
   python -m venv myvenv
   .\myvenv\Scripts\Activate.ps1

   # macOS / Linux
   python3 -m venv myvenv
   source myvenv/bin/activate
   ```

3. Install backend dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. Start the FastAPI server:
   ```bash
   python -m uvicorn backend.main:app --reload --port 8000
   ```
   - **FastAPI Server**: `http://127.0.0.1:8000`
   - **Interactive API Docs (Swagger UI)**: `http://127.0.0.1:8000/docs`

---

### Step 2: Launch React Frontend Application

Open a **new terminal window/tab** in `DemandDraft`:

1. Install frontend dependencies:
   ```bash
   npm install
   ```

2. Start the Vite development server:
   ```bash
   npm run dev
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:3000
   ```

---

## 📡 API Endpoint Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/health` | Health check endpoint returning backend server status |
| `GET` | `/api/presets` | Retrieves built-in template & reference presets |
| `POST` | `/api/upload-format` | Uploads and parses client format template document |
| `POST` | `/api/upload-reference` | Uploads and parses case reference facts document |
| `POST` | `/api/generate-motion` | Triggers full 4-stage agent pipeline and generates final draft |

---

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more details.
