markdown
Copy
Edit
# 📘 Flask CRUD App

A simple yet complete **Flask CRUD application** that includes:

- User signup and login system
- Dashboard with session-based authentication
- Add, update, and delete user records (first name, last name, email, phone, address)
- SQLite database integration
- Responsive layout with Bootstrap 5

---

## 📁 Features

- 📝 User Registration & Login
- 🧾 Full CRUD for user records
- 🗂️ SQLite Database
- 🔒 Session-based access control
- 🎨 Bootstrap 5 UI

---

## 🛠️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/O0gw4y/Flask-app.git
cd Flask-app
💻 2. Setup on Windows (PowerShell or CMD)
bash
Copy
Edit
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
🐧 3. Setup on Kali Linux / Ubuntu / Debian
bash
Copy
Edit
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python3 app.py
📦 Requirements
All required packages are listed in requirements.txt. Example:

txt
Copy
Edit
Flask==2.3.3
Flask_SQLAlchemy==3.1.1
To regenerate the requirements file manually:

bash
Copy
Edit
pip freeze > requirements.txt
🧪 Usage
Once the app is running:

Open your browser and go to http://127.0.0.1:5000

Use the Sign Up page to register a new user

Log in to access the Dashboard

Add, update, and delete records through the web UI

📂 File Structure
bash
Copy
Edit
Flask-app/
│
├── app.py                 # Main Flask app
├── firstapp.db            # SQLite DB (auto-generated)
├── requirements.txt       # Dependency list
├── templates/             # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── update.html
