# 📝 AI Blog Content Assistant (LangChain + Groq + Streamlit)

An AI-powered writing assistant that helps you create SEO-optimized blog content in seconds.  
This project uses LangChain and Groq’s blazing-fast LLMs to generate blog titles, full-length posts, subtitles, and hashtags with a downloadable PDF/TXT export — all through a beautiful Streamlit interface.

---

## 🚀 Features

- 🔤 Generate creative and engaging **blog titles**
- ✍️ Auto-write full **SEO-friendly blog posts** in markdown
- 🗒️ Suggest catchy **subtitles (meta descriptions)**
- 🏷️ Recommend **popular hashtags** for social reach
- 📄 **Download** blog content as PDF or TXT
- ⚡ Uses **Groq API + LangChain** with `Gemma2-9b-It`
- 🖥️ Simple and fast **Streamlit UI**

---

## 🧠 How It Works

1. **User inputs a topic or blog title**
2. The system uses **LangChain + Groq LLM** to:
   - Generate **10 unique blog titles**
   - Write a **full blog post** with intro, body, and conclusion
   - Suggest a **subtitle** (meta description)
   - Recommend **5 hashtags**
3. You can **preview the blog post** and **download** it as:
   - Plain `.txt` file
   - Stylized `.pdf` using FPDF

---

## 🗂️ Project Structure

```
.
├── app.py             # Streamlit frontend logic
├── chains.py          # Prompt templates + LLMChains
├── utils.py           # PDF generation helper (FPDF)
├── .env               # API keys (GROQ_API_KEY)
├── requirements.txt   # Project dependencies
```

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-blog-assistant.git
cd ai-blog-assistant
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Keys to `.env`

```env
GROQ_API_KEY="your_groq_api_key"

```

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`

---

## 🔐 Notes on Security

- Your API keys are **kept private** via `.env` and `python-dotenv`.
- Never commit `.env` to version control.
- Blog content is **not stored** anywhere — generation and downloads are local only.

---

## 📚 Tech Stack

- **LangChain** – Chain logic & prompt abstraction
- **Groq API** – Fast inference with `Gemma2-9b-It`
- **Streamlit** – Elegant UI for AI applications
- **FPDF** – PDF export for blog content
- **Python 3.9+**

