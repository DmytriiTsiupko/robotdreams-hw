from flask import request, render_template, abort, redirect
from . import app
import random
import re


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def get_users():
    users = ["John", "Mary", "Peter", "Alisa", "Bob", "Kate", "Ola", "Martin"]
    count = request.args.get('count')
    if count:
        try:
            count = int(count)
        except ValueError:
            return 'Invalid count value'
    else:
        count = random.randint(1, 10)
    random_users = []
    for _ in range(count):
        random_users.append(*random.sample(users, k=1))
    return ', '.join(random_users)


@app.get('/users/<int:user_id>')
def get_user_by_id(user_id):
    if user_id % 2 == 0:
        return f"User id is {user_id}"
    else:
        return "Not Found", 404


@app.get('/books')
def get_random_books():
    count = request.args.get('count')
    books = ["Think Python: How to Think Like a Computer Scientist",
             "To Kill a Mockingbird", "The Great Gatsby",
             "1984",
             "Pride and Prejudice",
             "The Catcher in the Rye"]
    if count:
        try:
            count = int(count)
        except ValueError:
            return 'Invalid count value'
    else:
        count = random.randint(1, 10)
    random_books = []
    book_list = "<ul>"
    for _ in range(count):
        random_books.append(*random.sample(books, k=1))
        book_list += f"<li>{random_books[-1]}</li>"
    book_list += "</ul>"
    return book_list


@app.get('/books/<title>')
def capitalize_title(title):
    return title.capitalize()


@app.route('/params')
def params():
    rows = []
    for key, value in request.args.items():
        rows.append(f"""<tr>
        <td>{key}</td>
        <td>{value}</td>
        </tr>""")
    return f'<table>{"".join(rows)}</table>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login_form.html")
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            abort(400, 'Username and password are required')
        if not re.match(r'^\w{5,}$', username):
            abort(400, 'Username must be at least 5 characters long')
        if not re.match(r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z_-]).{8,}$", password):
            abort(400,
                  'Password must be at least 8 characters long and contain at least 1 uppercase letter and 1 digit')
        return redirect('/users')


# ERROR CUSTOMIZATION

@app.errorhandler(404)
def page_not_found():
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error():
    return render_template('errors/500.html'), 500
