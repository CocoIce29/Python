from flask import Flask, request, render_template
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
def hello_world(): 
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("INSERT INTO blogs VALUES ('test', 'test heading', 'test content', 'test auth')")
    mysql.connection.commit()
    return "Hello World"

@app.route('/blog_form', methods = ['POST', 'GET']) 
def blog_form(): 
    if request.method == "POST":
        blog_name = request.form['blog_name']
        blog_heading = request.form['blog_heading']
        blog_body = request.form['blog_body']
        blog_author = request.form['blog_author']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("INSERT INTO blogs VALUES ('{0}', '{1}', '{2}', '{3}')".format(blog_name, blog_heading, blog_body, blog_author))
        mysql.connection.commit()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT b_name FROM blogs")
        blog_name = cursor.fetchall()
        return render_template('shell.html', blog_heading = blog_heading, blog_body = blog_body, blog_author = blog_author, links = blog_name)
    elif request.method == "GET":
        return render_template('test.html')

@app.route('/blog/<blog_name>', methods = ['POST', 'GET']) 
def blog(blog_name):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(("SELECT * FROM blogs WHERE b_name = '{0}'").format(blog_name))
    blog = cursor.fetchone()
    print('{0}')
    print(blog)
    blog_heading = blog['b_heading']
    blog_body = blog['b_body']
    blog_author = blog['b_author']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT b_name FROM blogs")
    blog_name = cursor.fetchall()
    print(blog_name)
    return render_template('shell.html', blog_heading = blog_heading, blog_body = blog_body, blog_author = blog_author, links = blog_name)

if __name__ == "__main__": 
    app.run(debug = True)