# Jinja Statements

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/hello/<int:score>')
# def hello_name(score):
#     return render_template('marks.html', marks = score)

# if __name__ == '__main__':
#     app.run(debug = True)

# Example 2

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/result')
# def result():
#     dict = {'phy': 50, 'chem': 60, 'math': 70}
#     return render_template('result.html', result = dict)

# if __name__ == '__main__':
#     app.run(debug = True)

# File Uploads

from flask import Flask, render_template, request, url_for, redirect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'File uploaded successfully.'
    else:
        return redirect(url_for('upload_file'))

if __name__ == '__main__':
    app.run(debug = True)
