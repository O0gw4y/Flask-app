📘 Flask CRUD App
A simple yet powerful Flask-based web application with full CRUD capabilities and user authentication. Built using SQLite for storage and Bootstrap 5 for responsive UI.

🚀 Features
📝 User Registration & Login

🧾 Create, Read, Update, Delete (CRUD) user records

🗂️ SQLite database integration

🔒 Session-based user dashboard

🎨 Responsive Bootstrap 5 interface

📦 File Structure
bash
Copy
Edit
Flask-app/
│
├── app.py                  # Main application
├── requirements.txt        # Python dependencies
├── firstapp.db             # SQLite database (auto-created)
└── templates/              # HTML templates
    ├── index.html
    ├── login.html
    ├── signup.html
    ├── dashboard.html
    └── update.html
🛠️ Setup Instructions
💻 Windows
bash
Copy
Edit
# Clone the repository
git clone https://github.com/O0gw4y/Flask-app.git
cd Flask-app

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
🐧 Linux (Kali / Ubuntu / Debian)
bash
Copy
Edit
# Clone the repository
git clone https://github.com/O0gw4y/Flask-app.git
cd Flask-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python3 app.py
🔍 Usage
Open your browser and visit: http://127.0.0.1:5000

🧑‍💼 Sign up as a new user

🔐 Log in to access the dashboard

➕ Add user records

🛠️ Update or ❌ delete existing records

