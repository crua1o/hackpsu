import hashlib
from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


def hash_password(password):
    """
    Hashes a password using the SHA256 algorithm.

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def validate(email, password):
    # check if given email and hashed password exist in database
    connection = sql.connect('hackpsu.db')

    # hash the password
    password = hash_password(password)

    cursor = connection.execute('SELECT * FROM Users WHERE email=? AND password=?;', (email, password))
    user = cursor.fetchone()

    if user is None:
        return False

    return True


def insert(first_name, last_name, DOB, gender, email, password, phone):
    # check if given email and hashed password exist in database
    connection = sql.connect('hackpsu.db')

    # hash the password
    password = hash_password(password)

    # check if a pid of 1 is in the database (u_id = 1 means at least 1 user)
    value = 1

    # Execute a SELECT statement to check if an entry is in the column
    cursor = connection.execute("SELECT * FROM Users WHERE u_id=?", (value,))
    result = cursor.fetchone()

    # If result is not None, then the value is already in the column
    if result is not None:
        # see last pid entry and increment by 1

        # Execute the SQL query to get the most recently added value of a table column
        cursor.execute("SELECT u_id FROM Users ORDER BY u_id DESC LIMIT 1;")

        # Fetch the result
        result2 = cursor.fetchone()

        # increment pid
        u_id = result2[0] + 1

    else:
        # first entry into database
        u_id = 1

    # create Users table if it doesn't exist
    connection.execute('''CREATE TABLE IF NOT EXISTS Users(
                               u_id INTEGER PRIMARY KEY,
                               first_name TEXT,
                               last_name TEXT,
                               DOB TEXT,
                               phone TEXT,
                               email TEXT,
                               password TEXT,
                               gender TEXT
                             )''')

    # add parameters into Users table
    connection.execute("INSERT INTO Users (u_id, first_name, last_name, DOB, phone, email, password, gender) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (u_id, first_name, last_name, DOB, gender, email, password, phone))

    # execute command
    connection.commit()
    return cursor.fetchall()


def search(*tags):
    connection = sql.connect('hackpsu')

    # build the query dynamically based on the number of tags provided
    query = "SELECT * FROM restaurant WHERE "
    for i in range(len(tags)):
        query += f"tags LIKE '%{tags[i]}%'"
        if i < len(tags) - 1:
            query += " AND "

    result = connection.execute(query).fetchone()
    if result is None:
        return False

    return True


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template('signup.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    error = ''

    # check if email and password are valid
    if request.method == 'POST':
        result = validate(request.form['email'], request.form['password'])
        if result:
            return render_template('homepage.html', result=result)
        else:
            error = 'email or password not valid'
    return render_template('login.html', error=error)


@app.route('/register', methods=["GET", "POST"])
def register():
    error = ''
    if request.method == "GET":
        return render_template('signup2.html')

    elif request.method == "POST":
        # get params from form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        DOB = request.form['birthday']
        phone = request.form['phone_number']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        insert(first_name, last_name, DOB, gender, email, password, phone)

    return render_template("homepage.html")


if __name__ == "__main__":
    app.debug = True
    app.run()

