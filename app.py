from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Config SQLite DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))

    def __repr__(self):
        return f'{self.sno} - {self.firstname}'

class AuthUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        new_user = User(firstname=firstname, lastname=lastname, email=email, phone=phone, address=address)
        db.session.add(new_user)
        db.session.commit()
    all_users = User.query.all()
    return render_template('index.html', users=all_users)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if username exists
        if AuthUser.query.filter_by(username=username).first():
            return "User already exists!"
        new_user = AuthUser(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = AuthUser.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = user.username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials!"
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/home')
def home():
    return redirect(url_for('index'))


@app.route('/delete/<int:sno>')
def delete(sno):
    user = User.query.get_or_404(sno)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    user = User.query.get_or_404(sno)
    if request.method == 'POST':
        user.firstname = request.form['firstname']
        user.lastname = request.form['lastname']
        user.email = request.form['email']
        user.phone = request.form['phone']
        user.address = request.form['address']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', user=user)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
