from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__) 

# app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'qwerty123'
app.config['MYSQL_DB'] = 'my_flask'

mysql = MySQL(app)

@app.route('/') 
def hello_world(): 
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("INSERT INTO blogs VALUES ('test', 'test heading', 'test content', 'test auth')")
    mysql.connection.commit()
    return "Hello World"

@app.route('/login', methods = ['POST', 'GET']) 
def login(): 
    if request.method == "POST":
        dict = {'phy':50,'che':60,'maths':70, 'english':60, 'French':90} 
        li = [100,200,300,400,500]
        first_name = request.form['u_name']
        last_name = request.form['u_last_name']
        user_mail = request.form['u_mail']
        my_file = request.files['u_file']
        my_file.save("my_downloads/" + my_file.filename)
        my_ppt = request.files['u_ppt']
        my_ppt.save("my_downloads/" + my_ppt.filename)
        return render_template('shell.html', heading = "My Heading", first_name = first_name, last_name = last_name, email = user_mail, my_list = li, my_dict = dict)
    elif request.method == "GET":
        return render_template('test.html')

if __name__ == "__main__": 
    app.run(debug = True)