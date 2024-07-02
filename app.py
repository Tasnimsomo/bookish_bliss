from flask import Flask, render_template, redirect, flash, url_for, session, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from forms import RegisterForm, LoginForm
from flask_bcrypt import Bcrypt
import os
from database import session as db_session
from models import User, Book

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure SQLAlchemy database URI using environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return db_session.query(User).get(int(user_id))

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_customer = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db_session.add(new_customer)
        db_session.commit()
        flash('Registration successful. Please login.')
        return redirect(url_for('login'))
    return render_template('sign-up.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db_session.query(User).filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password. Please try again.', 'error')
    return render_template('log-in.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

def create_admin_user():
    admin_user = db_session.query(User).get(1)
    if not admin_user:
        hashed_password = bcrypt.generate_password_hash('admin_password').decode('utf-8')
        admin_user = User(id=1, username='admin', email='admin@example.com', password=hashed_password)
        db_session.add(admin_user)
        db_session.commit()
        print("Admin user created successfully")
    else:
        print("Admin user already exists")

def reset_users():
    db_session.query(User).delete()
    db_session.commit()
    print("All users deleted")


@app.route('/admin')
@login_required
def admin():
    id = current_user.id
    if id == 1:
        return render_template("admin.html")
    else:
        flash("Sorry must be an admin to access this page")
        return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/add_book', methods=['GET', 'POST'])
@login_required
def add_book():
    if current_user.id != 1:
        flash("Sorry, you must be an admin to access this page")
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        price = float(request.form['price'])
        quantity = int(request.form['quantity'])
        
        new_book = Book(title=title, author=author, price=price, quantity=quantity)
        db_session.add(new_book)
        db_session.commit()
        
        flash('Book added successfully!', 'success')
        return redirect(url_for('admin'))
    
    return render_template('add_book.html')

@app.route('/view_books')
@login_required
def view_books():
    if current_user.id != 1:
        flash("Sorry, you must be an admin to access this page")
        return redirect(url_for('home'))
    
    books = db_session.query(Book).all()
    return render_template('view_books.html', books=books)

@app.route('/remove_book', methods=['GET', 'POST'])
@login_required
def remove_book():
    if current_user.id != 1:
        flash("Sorry, you must be an admin to access this page")
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        book_id = request.form['book_id']
        book = db_session.query(Book).get(book_id)
        if book:
            db_session.delete(book)
            db_session.commit()
            flash('Book removed successfully!', 'success')
        else:
            flash('Book not found!', 'error')
        return redirect(url_for('admin'))
    
    books = db_session.query(Book).all()
    return render_template('remove_book.html', books=books)

@app.route('/increase_book_amount', methods=['GET', 'POST'])
@login_required
def increase_book_amount():
    if current_user.id != 1:
        flash("Sorry, you must be an admin to access this page")
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        book_id = request.form['book_id']
        amount = int(request.form['amount'])
        
        book = db_session.query(Book).get(book_id)
        if book:
            book.quantity += amount
            db_session.commit()
            flash('Book amount increased successfully!', 'success')
        else:
            flash('Book not found!', 'error')
        return redirect(url_for('admin'))
    
    books = db_session.query(Book).all()
    return render_template('increase_book_amount.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)