# cosmetic-ingredient-analyzer
AI-powered beauty product analyzer using OCR, hybrid ingredient standardization, and LLM-based explainability to generate safety scores and personalized skincare insights from cosmetic products.


## 🚀 Overview
The **AI Beauty Product Ingredient Analyzer** is an intelligent web application that analyzes cosmetic product ingredients and evaluates their safety for different skin types.

It combines **OCR (image-to-text)**, **Large Language Models (LLMs)**, and a **rule-based analysis engine** to deliver accurate, explainable, and user-friendly skincare insights.

This project demonstrates real-world integration of:
- AI (LLMs & NLP)
- Computer Vision (OCR)
- Backend data processing
- Database integration
- Interactive UI development

> ⚠️ This is an academic prototype. Production-level deployment would require validated datasets, regulatory compliance, and external API integrations.

---

## 🎯 Key Features

- 📷 Extract ingredients directly from product images using OCR  
- 🤖 Normalize ingredient names using LLMs  
- 📊 Calculate safety score based on skin type  
- 🧪 Compute comedogenic (pore-clogging) score  
- ⚠️ Detect and flag high-risk ingredients  
- 📋 Display detailed ingredient insights  
- 🧠 Generate AI-powered explanations  
- 💬 Provide chatbot-based interaction  
- 🗄️ Store user data and results in MySQL  

---

## 🧠 System Architecture

```
User Upload (Image / Product)
        ↓
Streamlit Web Application
        ↓
OCR (Tesseract)
        ↓
LLM Processing (Ingredient Normalization)
        ↓
Ingredient Analysis Engine
        ↓
AI Insights Generation
        ↓
Results Display + Chatbot
        ↓
MySQL Database Storage
```

---

## 🛠️ Technology Stack

### Core
- Python 3.10+
- Streamlit
- pandas, NumPy

### AI & Processing
- Tesseract OCR (Image → Text)
- OpenAI / LLM APIs (Normalization, Insights, Chatbot)

### Backend & Data
- JSON (Ingredient dataset)
- MySQL (Data storage)
- SQLAlchemy / PyMySQL

### MLOps (Extended)
- Databricks (ML experimentation)
- MLflow (Model tracking)

---

## 📂 Project Structure

```
beauty-product-analyzer/
│
├── app.py
├── backend/
│   └── analyzer.py
│
├── services/
│   ├── ocr.py
│   ├── llm_normalizer.py
│   ├── ai_insights.py
│   └── chatbot.py
│
├── db/
│   ├── mysql.py
│   └── repo.py
│
├── pipelines/
│   └── inference_pipeline.py
│
├── ml/
│   ├── prepare_dataset.py
│   └── train_model.py
│
├── ingredients.json
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/yourusername/beauty-product-analyzer.git
cd beauty-product-analyzer
```

```bash
python -m venv venv
venv\\Scripts\\activate
```

```bash
pip install -r requirements.txt
```

```bash
python -m streamlit run app.py
```

---

## 📊 Output

The application provides:

- **Safety Score (%)** – Overall product safety  
- **Average Comedogenic Score** – Acne risk indicator  
- **Flagged Ingredients** – Medium/High risk components  
- **Ingredient Table** – Category, benefits, risk, comedogenic score  
- **AI Insights** – Natural language explanation  
- **Chatbot Interaction** – Follow-up Q&A  

---

## 🧪 Example

**Input:**
\`\`\`
Water, Cetyl Alcohol, Propylene Glycol, Sodium Lauryl Sulfate
\`\`\`

**Output:**
- Safety Score: 82%  
- Avg Comedogenic: 1.5  
- Flagged: Sodium Lauryl Sulfate (Medium Risk)  

---

## ⚠️ Limitations

- Uses a locally created JSON dataset  
- OCR accuracy depends on image quality  
- LLM responses may vary slightly  
- No external cosmetic APIs integrated  

---

## 🔮 Future Enhancements

- Barcode (UPC/EAN) product lookup  
- External APIs (INCI / Open Beauty Facts)  
- ML-based personalized recommendations  
- Cloud deployment  
- Full MLOps pipeline  

---

## 👩‍💻 Author

**Hashini Krishnamoorthy**

---

## ⭐ Project Summary

This project evolved from a **rule-based analyzer (v1.0)** to an **AI-powered system (v2.0)** integrating:

- OCR-based extraction  
- LLM-based processing  
- AI insights and chatbot  
- Database integration  
- MLOps-ready architecture  

It demonstrates strong capabilities in **AI application development, backend engineering, and system design**.

EOF
