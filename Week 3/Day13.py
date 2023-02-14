# from flask import Flask

# app = Flask(__name__)

# @app.route('/') 
# def hello_world(): 
#     return "Hello World"

# @app.route('/contact') 
# def contact_world(): 
#     return "Contact us"

# @app.route('/hello') 
# def no_world(): 
#     return "I am saying hello through flask"

# if __name__ == "__main__": 
#     app.run(debug = True)

# Routing

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def main_page():
#     return 'Welcome to the main page.'

# @app.route('/hello')
# def hello_world():
#     return 'hello world'

# if __name__ == "__main__": 
#     app.run(debug = True)

# Add URL Rule

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def main_page():
#     return 'Welcome to the main page.'

# def hello_world():
#     return 'hello world'

#     # Works the same as @app.route('/hello')

# app.add_url_rule('/hello', 'hello', hello_world)

# if __name__ == "__main__": 
#     app.run(debug = True)

# Variable Rules

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def main_page():
#     return 'Welcome to the main page.'

# @app.route('/hello')
# def hello_world():
#     return 'hello world'

# @app.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello %s!' %name

# if __name__ == "__main__": 
#     app.run(debug = True)

# Other URL Rules

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def main_page():
#     return 'Welcome to the main page.'

# @app.route('/hello')
# def hello_world():
#     return 'hello world'

# @app.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello %s!' %name

# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#     return 'Blog Number %d' %postID

# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#     return 'Revision Number: %f' %revNo

# if __name__ == "__main__": 
#     app.run(debug = True)

# URL Building

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Welcome Admin.'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))

if __name__ == "__main__": 
    app.run(debug = True)