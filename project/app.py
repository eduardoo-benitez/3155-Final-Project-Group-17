from flask import Flask, abort, redirect, render_template, request

from src.repositories.WebsiteRepository import website_repository_singleton

from src.models import db

app = Flask(__name__)

# TODO: DB connection

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:password@localhost:3306/movies'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.get('/')
def login():
    return render_template('homepage.html')

@app.get('/login')
def register():
    return render_template('login.html')

@app.get('/all')
def all():
    #TODO: Implement view all posts by grabbing posts from database
    return render_template('allPosts.html')

@app.get('/profile')
def profile():
    #TODO: Implememt profile view by getting information from login/register and mathcing it with info in databse.
    return render_template('profile.html')

@app.post('/profile/post')
def post():
    #TODO: make post that updates database and displays in HTML. The following is mostly placeholder and doesnt do much.
    title = request.form.get('title', '')
    date = request.form.get('date', '')
    author = request.form.get('author', 0, type=int)
    body = date = request.form.get('date', '')

    created_post = website_repository_singleton.create_post(title, date, author, body)
    return redirect(f'/all/{created_post.post_id}')


@app.get('/all/<int:post_id>')
def view(post_id):
    #TODO: View specific post
    return render_template('post.html')

@app.get('/all/view/edit')
def edit():
    #TODO: Edit post being viewed, only if user is author.
    return render_template('editPost.html')

