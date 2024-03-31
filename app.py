# Store this code in 'app.py' file

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import pandas as pd


app = Flask(__name__)


app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Abc@123'
app.config['MYSQL_DB'] = 'sys'

mysql = MySQL(app)


@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			return render_template('home.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)

#------------------------------------------------------------------------
# Load the CSV data into a DataFrame
data = pd.read_csv('result_data.csv')  # Replace 'result_data.csv' with your CSV file name

@app.route('/resultAnalyser', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        # Get the SSC percentage entered by the user
        ssc_percentage = float(request.form['ssc_percentage'])

        # Filter colleges with cutoffs less than or equal to the entered percentage
        matching_colleges = data[data['SSCPercentage'] <= ssc_percentage]

        if matching_colleges.empty:
            message = "No colleges found with a cutoff percentage less than or equal to your SSC percentage."
            return render_template('resultAnalyser.html', message=message, result_data=None)
        else:
            # Display the list of colleges and branches that meet the student's criteria
            result_data = []
            for index, row in matching_colleges.iterrows():
                college_name = row['CollegeName']
                branches = row['Branches'].split(', ')  # Assuming branches are stored as comma-separated values in the CSV
                result_data.append({'CollegeName': college_name, 'Branches': branches})

            return render_template('resultAnalyser.html', result_data=result_data)
    else:
        # Handle GET requests (e.g., render a form)
        return render_template('resultAnalyser.html', result_data=None)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/collages')
def colleges():
    return render_template('collages.html')	
	

@app.route('/capround')
def admission_process():
    return render_template('capround.html')

@app.route('/scholarship')
def scholarship():
    return render_template('scholarship.html')

@app.route('/aboutus')
def about_us():
    return render_template('about us.html')


@app.route('/thakur')
def thakur():
    return render_template('thakur.html')

@app.route('/pillaiHoc')
def pillaihoc():
    return render_template('Pillai Hoc.html')

@app.route('/mhsaboosiddik')
def mhsaboosiddik():
    return render_template('M H Sabo siddik.html')

@app.route('/kjsomaya')
def kjsomaya():
    return render_template('kj somaya.html')

@app.route('/kalsekar')
def kalsekar():
    return render_template('kalsekar.html')

@app.route('/gpthane')
def gpthane():
    return render_template('GP Thane.html')

@app.route('/gpmumbai')
def gpmumbai():
    return render_template('GP Mumbay.html')

@app.route('/fatheragnel')
def fatheragnel():
    return render_template('father agnel.html')

@app.route('/bhartividhiyapeeth')
def bhartividhiyapeeth():
    return render_template('bharti vidhiyapeeth.html')

@app.route('/csp')
def csp():
    return render_template('csp.html')



if __name__ == '__main__':
    app.run(debug=False)