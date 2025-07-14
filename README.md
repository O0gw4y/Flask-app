📘 Flask CRUD App
This is a simple full-featured Flask CRUD application with:

User login/signup system

Dashboard with session control

Add, update, and delete user records (first name, last name, email, phone, address)

SQLite database integration

Bootstrap 5 UI for a responsive layout

📁 Features
📝 User Registration & Login

🧾 CRUD for user records (name, email, phone, etc.)

🗂️ SQLite Database

🔒 Session-based Dashboard

🎨 Styled with Bootstrap 5

🛠️ Setup Instructions
🔧 1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/O0gw4y/Flask-app.git
cd Flask-app
💻 2. Setup on Windows (PowerShell or CMD)
📌 Step-by-step:
bash
Copy
Edit
# Create and activate a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
🐧 3. Setup on Kali Linux / Ubuntu / Debian
📌 Step-by-step:
bash
Copy
Edit
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python3 app.py
📦 Requirements
All required packages are listed in requirements.txt. Example:

ini
Copy
Edit
Flask==2.3.3
Flask_SQLAlchemy==3.1.1
You can generate this yourself with:

bash
Copy
Edit
pip freeze > requirements.txt
🧪 Usage
After launching:

Visit http://127.0.0.1:5000 in your browser.

Use the Sign Up page to register a new user.

Login to access the dashboard.

Add records and manage them using the UI.

📂 File Structure
pgsql
Copy
Edit
Flask-app/
│
├── app.py                  # Main application script
├── firstapp.db             # SQLite DB (auto-created)
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── update.html
