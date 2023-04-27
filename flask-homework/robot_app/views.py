from flask import request, render_template, abort, redirect, session
from . import app
import re
from .static.wraps import login_required
from .models import *


@app.route('/')
@login_required
def index():
    return render_template('index.html')


# USERS_ROUTS
@app.route('/users')
@login_required
def get_users():
    users = Users.query.all()
    return render_template('users.html', users=users)


@app.route('/users/<int:user_id>')
@login_required
def get_user(user_id):
    user = Users.query.get(user_id)
    if user:
        return render_template('user_id.html', user=user)
    else:
        return render_template('errors/404.html'), 404


# BOOKS_ROUTS
@app.get('/books')
@login_required
def get_books():
    books = Books.query.all()
    return render_template('books.html', books=books)


@app.route('/books/<int:book_id>')
@login_required
def get_book_by_id(book_id):
    if book_id:
        book = Books.query.get(book_id)
        if book:
            return render_template('book_id.html', book=book)
        else:
            return render_template('errors/404.html'), 404
    else:
        books = Books.query.all()
        return render_template('books.html', books=books)


# PURCHASES_ROUTS
@app.route('/purchases/')
@login_required
def get_purchases():
    purchases = Purchases.query.all()
    return render_template('purchases.html', purchases=purchases)


@app.route('/purchases/<int:purchase_id>')
def get_purchase_by_id(purchase_id):
    purchase = Purchases.query.get(purchase_id)
    if purchase:
        return render_template('purchase_id.html', purchase=purchase)
    else:
        return render_template('errors/404.html'), 404


# LOGIN-LOGOUT ROUTS
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login_form.html")
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            abort(400, 'Username and password are required')
        else:
            session['username'] = username
        if not re.match(r'^\w{5,}$', username):
            abort(400, 'Username must be at least 5 characters long')
        if not re.match(r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z_-]).{8,}$", password):
            abort(400,
                  'Password must be at least 8 characters long and contain at least 1 uppercase letter and 1 digit')
        return render_template('index.html', username=username)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')


# ERROR CUSTOMIZATION
@app.errorhandler(404)
def page_not_found():
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error():
    return render_template('errors/500.html'), 500
