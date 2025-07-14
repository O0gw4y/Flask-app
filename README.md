📄 README.md

# 🧩 Flask CRUD App with Authentication & Dashboard

This is a full-featured **Flask Web Application** that includes:

1. User **Sign Up** and **Login** system
2. A protected **Dashboard** using session-based authentication
3. Full **CRUD operations** (Create, Read, Update, Delete) for user records:
   - First Name
   - Last Name
   - Email
   - Phone
   - Address
4. SQLite integration with SQLAlchemy ORM
5. Clean and responsive UI using **Bootstrap 5**

---

## 📂 Project Structure

📁 Flask-app/  
├── `app.py`                – Main Flask application logic  
├── `firstapp.db`           – SQLite database (auto-generated)  
├── `requirements.txt`      – Python dependencies  
└── `templates/`            – HTML templates folder  
  ├── `index.html`          – Home with record listing & form  
  ├── `signup.html`         – Sign up form  
  ├── `login.html`          – Login form  
  ├── `dashboard.html`      – Dashboard after login  
  └── `update.html`         – Record update form  

---

## ⚙️ Requirements

**Python Version:** Python 3.8+ recommended

All dependencies are listed in `requirements.txt`:

```text
Flask==2.3.3
Flask_SQLAlchemy==3.1.1
```

---

## 🖥️ How to Run

### ✅ On **Windows** (PowerShell or CMD):

```powershell
# Step 1: Navigate to your project
cd "C:\path\to\Flask-app"

# Step 2: Create and activate virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the Flask app
python app.py
```

---

### 🐧 On **Kali Linux / Ubuntu / Debian**:

```bash
# Step 1: Navigate to your project
cd /path/to/Flask-app

# Step 2: Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Run the Flask app
python3 app.py
```

---

## 🚀 Using the App

After launching, open your browser and go to:

```
http://127.0.0.1:5000
```

### 📝 Steps:

1. Click **Sign Up** to create a new account
2. Log in to access the **Dashboard**
3. Add, edit, or delete user records directly from the home page
4. Use the navbar or buttons for navigation and logout

---

## 🔒 Features

- 🧾 Record creation and viewing on home page
- ✏️ Edit individual records
- 🗑️ Delete records by ID
- 🧑‍💻 Session management for secure dashboard access
- 🎨 Bootstrap 5 UI for mobile-responsive design

---

