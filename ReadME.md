# AI Content Generator 🚀

An AI-powered Content Generator built using **FastAPI**, **Streamlit**, and **Groq LLM API**.

This project helps users generate:

* Blogs
* LinkedIn Posts
* Instagram Captions
* Emails
* Twitter Posts
* YouTube Descriptions

based on selected topic, technology, and tone.

---

# 📌 Technologies Used

## Frontend

* Streamlit

## Backend

* FastAPI
* Uvicorn

## AI Model

* Groq API
* Llama 3.1 8B Instant Model

---

# 📂 Project Structure

```bash
AI_Content_Generator/
│
├── Backend/
│   └── main.py
│
├── Frontend/
│   └── app.py
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone <your-github-repo-link>
```

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

---

## Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup Groq API Key

Create environment variable:

## Windows CMD

```bash
set GROQ_API_KEY=your_api_key
```

## PowerShell

```bash
$env:GROQ_API_KEY="your_api_key"
```

---

# ▶️ Run Backend

Move to Backend folder:

```bash
cd Backend
```

Run FastAPI server:

```bash
uvicorn main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend

Open new terminal.

Move to Frontend folder:

```bash
cd Frontend
```

Run Streamlit app:

```bash
streamlit run app.py
```

Frontend runs on:

```bash
http://localhost:8501
```

---

# 🧠 How Project Works

1. User enters:

   * Topic
   * Technology
   * Content Type
   * Tone

2. Streamlit sends request to FastAPI backend.

3. Backend creates prompt.

4. Groq AI model generates content.

5. Generated content is displayed in frontend.

---

# 📜 Backend Code Explanation

## FastAPI

Used to create API endpoints.

```python
app = FastAPI()
```

---

## POST API

```python
@app.post("/generate")
```

Used to receive data from frontend.

---

## Groq Client

```python
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
```

Connects project with Groq AI model.

---

# 📜 Frontend Code Explanation

## Streamlit Form

Used to collect user inputs.

```python
with st.form():
```

---

## Requests Library

Sends API request to backend.

```python
requests.post()
```

---

## Display Output

```python
st.write(data["response"])
```

Displays generated AI content.

---

# 📦 requirements.txt

```txt
fastapi
uvicorn
streamlit
requests
groq
```

---

# 🌐 Deployment

## Backend Deployment

* Render Backend Link = [https://ai-content-generator-bh01.onrender.com](https://ai-content-generator-bh01.onrender.com)
## Frontend Deployment

* Streamlit Cloud 

Live Link = [[https://ai-content-generator-bh01.onrender.com]](https://aicontentgeneratornew.streamlit.app/)
---

# 🛠️ Common Errors

## 1. API Key Error

Error:

```bash
GroqError: api_key must be set
```

Solution:
Set `GROQ_API_KEY`.

---

## 2. Backend Not Connecting

Check:

* Backend URL
* Backend is running
* Render deployment successful

---

## 3. Content Not Displaying

Check:

```python
st.write(data["response"])
```

---

# ✨ Future Improvements

* Add Chat History
* Add Download Option
* Add Multiple AI Models
* Add User Authentication
* Add Dark Theme

---

# 👨‍💻 Author

Jeegari Thirumal

