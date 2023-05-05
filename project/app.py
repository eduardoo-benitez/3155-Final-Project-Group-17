from flask import Flask, redirect, render_template, request

from src.repositories.WebsiteRepository import website_repository_singleton

from src.models import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:password@localhost:3306/FinalProjectDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def reset_active():
    website_repository_singleton.reset()

@app.get('/')
def register_form():
    reset_active()
    return render_template('homepage.html')

@app.post('/')
def register():
    email = request.form.get('email')
    passw = request.form.get('passw')
    username = request.form.get('username')
    
    if (website_repository_singleton.login(email, passw, username)) is None:
        if website_repository_singleton.checkDuplicateUsername(username) and website_repository_singleton.checkDuplicateEmail(email):
            created_user = website_repository_singleton.register(email, passw, username)
            return redirect(f'/profile/{created_user.account_id}')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.get('/login')
def login_form():
    reset_active()
    return render_template('login.html')

@app.post('/login')
def login():
    email = request.form.get('email')
    passw = request.form.get('passw')
    username = request.form.get('username')

    if (website_repository_singleton.login(email, passw, username)) is None:
        return redirect('/login')
    else:
        found_user = website_repository_singleton.login(email, passw, username)
        return redirect(f'/profile/{found_user.account_id}')

@app.get('/profile')
def profile_redirect():
    active_user = website_repository_singleton.find_active_user()
    return redirect(f'/profile/{active_user.account_id}')

@app.get('/profile/<int:user_id>')
def profile(user_id):
    single_user = website_repository_singleton.get_user_by_id(user_id)
    user_posts = website_repository_singleton.get_all_active_posts()
    return render_template('profile.html', user = single_user, posts = user_posts)

@app.get('/profile/create')
def create_post_form():
    return render_template('createPost.html')

@app.post('/profile/create')
def create_post():
    title = request.form.get('title')
    body = request.form.get('body')
    author = website_repository_singleton.find_active_user()
    tag = request.form.get('year')

    created_post = website_repository_singleton.create_post(title, body, author.username, tag)
    return redirect(f'/post/{created_post.post_id}')

@app.get('/post/<int:post_id>')
def view(post_id):
    single_post = website_repository_singleton.get_post_by_id(post_id)
    active_user = website_repository_singleton.find_active_user()

    return render_template('post.html', post = single_post, active = active_user)

@app.get('/all')
def list_all_posts():
    all_posts = website_repository_singleton.get_all_posts()
    return render_template('allPosts.html', posts = all_posts)

@app.get('/post/<int:post_id>/edit')
def edit_form(post_id):
    single_post = website_repository_singleton.get_post_by_id(post_id)
    return render_template('editPost.html', post = single_post)

@app.post('/post/<int:post_id>/edit')
def edit(post_id):
    title = request.form.get('title')
    body = request.form.get('text')
    tag = request.form.get('year')
    target_post = website_repository_singleton.get_post_by_id(post_id)

    website_repository_singleton.update_post(target_post, title, body, tag)
    return redirect(f'/post/{post_id}')

@app.post('/all/filter')
def filter():
    filter = request.form.get('filter')
    filtered_posts = website_repository_singleton.filter_by_tag(filter)
    return render_template('allPosts.html', posts = filtered_posts)

