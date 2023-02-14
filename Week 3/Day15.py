# from flask import Flask, redirect, url_for, request

# app = Flask(__name__)

# @app.route('/success/<name>')
# def success(name):
#     return 'Welcome %s' %name

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['nm']
#         return redirect(url_for('success', name = user))
#     else:
#         user = request.args.get('nm')
#         return redirect(url_for('success', name = user))

# if __name__ == '__main__':
#     app.run(debug = True)

# Internal HTML Templates

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<html><body><h1>Hello World</h1></body></html>'

# if __name__ == "__main__":
#     app.run(debug = True)

# External HTML Templates

# from flask import Flask, request, render_template

# app = Flask(__name__) 

# @app.route('/') 
# def hello_world(): 
#     return "Hello World"

# @app.route('/login', methods = ['POST', 'GET']) 
# def login(): 
#     if request.method == 'POST':
#         print("i am in here")
#         user_name = request.form["u_name"]
#         user_last_name = request.form["u_last_name"]
#         my_str = "Your name provided is " + user_name + " and the last name " + user_last_name
#         return "<html><body><h1>" + my_str + "</h1></body></html>"
#     elif request.method == 'GET':
#         return render_template('home.html')

# if __name__ == "__main__": 
#     app.run(debug = True)