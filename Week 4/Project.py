from flask import Flask, request, render_template, url_for, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__) 

# app.secret_key = 'your secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Marauders29?'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/') 
def landing_page(): 
    return redirect(url_for('user_login'))

@app.route('/login', methods = ['POST', 'GET'])
def user_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(("SELECT * FROM users WHERE userName ='{0}' AND passWord ='{1}'").format(username, password))
        user = cursor.fetchone()
        if user:
            return redirect(url_for('home_page'))
        else:
            return redirect(url_for('user_login'))
    elif request.method == "GET":
        return render_template('login.html')

@app.route('/registration', methods = ['POST', 'GET']) 
def user_reg(): 
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']
        birthday = request.form['birthday']
        email = request.form['email']
        phone = request.form['phone']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT INTO users VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(username, password, fname, lname, birthday, email, phone))
        mysql.connection.commit()
        return redirect(url_for('home_page'))
    elif request.method == "GET":
        return render_template('registration.html')

@app.route('/postpage', methods = ['POST', 'GET']) 
def user_post(): 
    if request.method == "POST":
        title = request.form['title']
        subtitle = request.form['subtitle']
        content = request.form['content']
        author = request.form['author']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO posts VALUES ("{0}", "{1}", "{2}", "{3}")'.format(title, subtitle, content, author))
        mysql.connection.commit()
        return redirect(url_for('home_page'))
    elif request.method == "GET":
        return render_template('postpage.html')

@app.route('/home', methods = ['POST', 'GET']) 
def home_page():
    if request.method == "GET":
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM posts")
        content = cursor.fetchall()
        return render_template('homepage.html', post = content)

if __name__ == "__main__": 
    app.run(debug = True)