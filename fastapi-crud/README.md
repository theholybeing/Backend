# 🚀 FastAPI SQLite Full-Stack CRUD Application

A complete Full-Stack CRUD (Create, Read, Update, Delete) application built using:

- ⚡ FastAPI (Backend)
- 🗄️ SQLite (Database)
- 🧠 SQLAlchemy ORM
- 🌐 HTML + JavaScript (Frontend - Fetch API)

This project demonstrates how to build a REST API using FastAPI and connect it with a simple frontend using JavaScript.

---

## 📌 Features

✅ Create Student  
✅ Read All Students  
✅ Update Student  
✅ Delete Student  
✅ SQLite Database Integration  
✅ RESTful API  
✅ Swagger Auto Documentation  
✅ Frontend connected using Fetch API  
✅ Clean project structure  

---

## 🧠 System Architecture

Frontend (HTML + JavaScript)
        ⬇
FastAPI REST API
        ⬇
SQLAlchemy ORM
        ⬇
SQLite Database

---

## 📂 Project Structure
fastapi-crud/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── students.db
└── static/
  └── index.html


---

## 🛠️ Installation Guide

### 1️⃣ Clone the Repository

git clone https://github.com/theholybeing/Backend/fastapi-crud.git

cd fastapi-crud

---

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

---

### 3️⃣ Install Dependencies
pip install fastapi uvicorn sqlalchemy

OR if requirements.txt exists:
pip install -r requirements.txt

---

### 4️⃣ Run the Server
uvicorn main:app --reload

Server will start at:
http://127.0.0.1:8000

---

## 🌐 How to Use

### 🔹 API Documentation (Swagger)
http://127.0.0.1:8000/docs

Test all CRUD endpoints directly from browser.

---

### 🔹 Frontend Application
http://127.0.0.1:8000/static/index.html

You can:

- Add Student
- View Students
- Update Student
- Delete Student

---

## 📊 API Endpoints

| Method | Endpoint              | Description        |
|--------|----------------------|--------------------|
| POST   | /students/           | Create student     |
| GET    | /students/           | Get all students   |
| PUT    | /students/{id}       | Update student     |
| DELETE | /students/{id}       | Delete student     |

---

## 🗄️ Database

- SQLite database
- Automatically creates `students.db`
- Data persists locally
- No external database setup required

---

## 💻 Technologies Used

- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- HTML5
- JavaScript (Fetch API)
- Uvicorn

---

## 🎯 Learning Objectives Achieved

- Built REST APIs with FastAPI
- Used SQLAlchemy ORM for database operations
- Implemented SQLite database
- Structured backend in modular architecture
- Connected frontend with backend using Fetch API
- Implemented full CRUD operations

---

## 🚀 Future Enhancements

- JWT Authentication
- User Login & Registration
- Bootstrap UI Upgrade
- PostgreSQL Integration
- Docker Support
- Cloud Deployment (Render / Railway)

---

---

## 👨‍💻 Author

Muhammad Umer  
Backend & Full-Stack Developer  
