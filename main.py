from flask import Flask
from flask.helpers import url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello there'


@app.route('/home')
def home():
    return 'This is the home page.'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revison Number %f' % revNo

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else :
        return redirect(url_for('hello_guest', guest= name))



 
if __name__ == '__main__':
    app.run(debug=True)
