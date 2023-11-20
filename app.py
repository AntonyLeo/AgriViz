from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
import pymysql
from datetime import datetime
import csv
from flask import make_response

app = Flask(__name__)

app.secret_key = 'your secret key'

# database connection details 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'stavros1332'
app.config['MYSQL_DB'] = 'pythonlogin'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        # Retrieve the hashed password
        hash = password + app.secret_key
        hash = hashlib.sha1(hash.encode())
        password = hash.hexdigest()
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return the result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg='')
 
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))
 
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Hashing the password
            hash = password + app.secret_key
            hash = hashlib.sha1(hash.encode())
            password = hash.hexdigest()
            # Account doesn't exist, and the form data is valid, so inserting the new account into the accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        msg = 'Please fill out the form!' # Form is empty
    return render_template('register.html', msg=msg)
 
@app.route('/home')
def home():
    # If the user logged in
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    # If the user logged in
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not logged in redirect to login page
    return redirect(url_for('login'))

@app.route('/display_data', methods=['POST'])
def display_data():
    if request.method == 'POST':
        field = request.form['field']
        year = request.form['year']
        from_date = request.form.get('from_date')
        to_date = request.form.get('to_date')

        # Defining field_id based on the field value
        field_id_map = {
            'Salinas': 101,
            'Santa Maria': 102,
            # Add more mappings if needed
        }
        field_id = field_id_map.get(field)

        connection = pymysql.connect(
            host='yielddatabase.coz72rpcgefb.us-east-1.rds.amazonaws.com',
            user='admin',
            password='stavros1332',
            db='harvest',
            cursorclass=pymysql.cursors.DictCursor
        )

        cursor = connection.cursor()

        # Constructing the query
        query = 'SELECT * FROM raw_data WHERE field_id = %s AND DATE_FORMAT(Date, "%%Y") = %s'
        query_params = [field_id, year]

        # Adding date range to the query if provided
        if from_date and to_date:
            query += ' AND Date BETWEEN %s AND %s'
            query_params.extend([from_date, to_date])

        query += ' LIMIT 10'
        cursor.execute(query, tuple(query_params))

        data = cursor.fetchall()
        connection.close()

        if data:
            return render_template('home.html', data=data, field=field, year=year, from_date=from_date, to_date=to_date)
        else:
            no_data_message = "SORRY! NO DATA AVAILABLE. PLEASE TRY AGAIN LATER!"
            return render_template('home.html', no_data_message=no_data_message, field=field, year=year, from_date=from_date, to_date=to_date)
        

@app.route('/download_data', methods=['POST'])
def download_data():
    if request.method == 'POST':
        field = request.form['field']
        year = request.form['year']
        from_date = request.form.get('from_date')
        to_date = request.form.get('to_date')

        # Defining field_id based on the field value
        field_id_map = {
            'Salinas': 101,
            'Santa Maria': 102,
            # Add more mappings if needed
        }
        field_id = field_id_map.get(field)
    # Connecting to the RDS database and fetch all data from the table
    connection = pymysql.connect(
        host='yielddatabase.coz72rpcgefb.us-east-1.rds.amazonaws.com',
        user='admin',
        password='stavros1332',
        db='harvest',
        cursorclass=pymysql.cursors.DictCursor
    )

    cursor = connection.cursor()
    
    # Constructing the query
    query = 'SELECT * FROM raw_data WHERE field_id = %s AND DATE_FORMAT(Date, "%%Y") = %s'
    query_params = [field_id, year]

    # Adding date range to the query if provided
    if from_date and to_date:
        query += ' AND Date BETWEEN %s AND %s'
        query_params.extend([from_date, to_date])

    cursor.execute(query, tuple(query_params))
    data = cursor.fetchall()
    connection.close()

     # Converting data to CSV
    if data:
        output = make_response('\n'.join([','.join(data[0].keys())] + [','.join(map(str, item.values())) for item in data]))
        output.headers["Content-Disposition"] = f"attachment; filename={field}_{year}_data.csv"
        output.headers["Content-type"] = "text/csv"
        return output
    else:
        return "No data available for download"

@app.route('/visualize_data', methods=['POST'])
def visualize_data():
    # Redirecting to the QuickSight link
    return redirect("https://us-east-1.quicksight.aws.amazon.com/sn/data-sets/new", code=302)

if __name__ == '__main__':
    app.run(debug=True)
