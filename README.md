# 🧴 Cosmetic Ingredient Analyzer

A Streamlit-based web application that analyzes skincare product ingredients 
using OCR, LLM normalization, and a curated ingredient safety database — 
delivering personalized safety scores based on your skin type.

---

## 🚀 Features

- 📸 **OCR Extraction** — Upload a product label image; Tesseract OCR extracts the ingredient text automatically
- 🧠 **LLM Normalization** — OpenAI GPT normalizes raw OCR output into clean, standardized INCI ingredient names
- 🗄️ **Ingredient Database** — Custom JSON database cross-referenced with Open Beauty Facts, covering safety risk levels, comedogenic scores, categories, and benefits
- 📊 **Personalized Safety Scoring** — Calculates a safety score and average comedogenic rating tailored to your skin type (Oily, Dry, Sensitive, Normal, Combination)
- ⚠️ **Flagged Ingredient Detection** — Highlights medium and high-risk ingredients with reasoning
- 💬 **AI Skincare Chatbot** — Context-aware OpenAI assistant answers questions about the analyzed product
- 💾 **MySQL Persistence** — Saves user profiles and analysis history via SQLAlchemy

---

## 🏗️ Architecture
```
├── app.py                  # Streamlit frontend & session management
├── backend/
│   └── analyzer.py         # Ingredient scoring & safety logic
├── services/
│   ├── ocr.py              # Tesseract OCR image processing
│   ├── llm_normalizer.py   # OpenAI-based ingredient normalization
│   ├── ai_insights.py      # GPT-generated product insights
│   └── chatbot.py          # Context-aware skincare assistant
├── db/
│   └── repo.py             # MySQL user & search history repository
├── ingredients.json        # Curated ingredient safety database
└── requirements.txt
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-beauty-analyzer.git
cd ai-beauty-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR
- **Windows:** Download from [UB-Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)
- **Mac:** `brew install tesseract`
- **Linux:** `sudo apt install tesseract-ocr`

### 4. Configure environment variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key
MYSQL_USER=your_db_user
MYSQL_PASSWORD=your_db_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=beauty_ai
```
> ⚠️ **Never commit your `.env` file.** Add it to `.gitignore`.

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🧪 Service Testing

Before running the full application, individual services can be validated 
independently to confirm OCR, database connectivity, and LLM normalization 
are functioning correctly.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| OCR | Tesseract / Pytesseract |
| LLM | OpenAI GPT (normalization + chatbot) |
| Database | MySQL + SQLAlchemy |
| Ingredient Data | Custom DB + Open Beauty Facts |
| Language | Python 3.10+ |

---

## 📌 Important Notes

- Add `.env` to your `.gitignore` before pushing to GitHub
- The `ingredients.json` database is continuously expandable with new INCI entries
- Safety scoring logic is customized per skin type — oily skin applies comedogenic 
  penalties, sensitive skin penalizes risk-rated ingredients more heavily

---

## 🔮 Roadmap

- [ ] Expand ingredient database via Open Beauty Facts API integration
- [ ] Add allergen detection layer
- [ ] Support multi-language OCR
- [ ] REST API wrapper for third-party integration
- [ ] Ingredient comparison across multiple products

---

## 👩‍💻 Author

Built by Hashini Krishnamoorthy — MS Graduate | AI/ML Engineer  
Email: hashinikrishnamoorthy246@gmail.com
