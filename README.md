# Chatbot Project

## 📌 Project Overview
This is an **End-to-End Chatbot System** built as part of the *Machine Learning Beginner to Advanced Course Final Project*. It integrates a simple ML-powered backend with a user-friendly frontend interface.

- **Frontend:** HTML, CSS, JavaScript (located in `frontend/`)
- **Backend:** Flask API serving chatbot logic (located in `backend/`)
- **Dataset:** Knowledge base stored in `knowledge_base.json`

The system allows users to type queries into the frontend interface, which are processed by the backend chatbot model and return responses in real-time.

---

## 🚀 Features
- End-to-End chatbot pipeline (Frontend ↔ Backend ↔ ML Model)
- Flask backend with REST API endpoints
- CORS enabled → can open `index.html` directly
- Simple, clean UI for chatbot interaction
- Knowledge-base driven response generation

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/chatbot-project.git
cd chatbot-project
```

### 2️⃣ Install Dependencies
Make sure you have Python 3.8+ installed.
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Backend
```bash
cd backend
python app.py
```
By default, the Flask server will run at:
```
http://127.0.0.1:5000
```

### 4️⃣ Open the Frontend
Simply open `frontend/index.html` in your browser.

---

## 📂 Project Structure
```
chatbot-project/
├── README.md              <- Project setup & instructions
├── report.md              <- Project documentation (for reference)
├── requirements.txt       <- Python dependencies
├── frontend/              <- User interface
│   ├── index.html
│   ├── style.css
│   └── script.js
└── backend/               <- Backend logic (Flask API)
    ├── app.py
    ├── chatbot_model.py
    └── knowledge_base.json
```
---

## 📑 Deliverables
- **Codebase:** Frontend + Backend
- **Report (PDF):** Contains problem definition, solution overview, challenges, and references

---

## 🙌 References
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [NumPy](https://numpy.org/)

