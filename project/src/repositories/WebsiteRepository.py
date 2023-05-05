
from src.models import db, users, posts

class WebsiteRepository:
    
    def reset(self):
        for row in users.query:
            row.activeUser = False
        db.session.commit()

    def checkDuplicateUsername(self, username):
        for row in users.query:
            if row.username == username:
                return False
        return True
    
    def checkDuplicateEmail(self, email):
        for row in users.query:
            if row.email == email:
                return False
        return True
    
    def register(self, email, passw, username):
        newUser = users(email = email, passw = passw, username = username, activeUser = True)
        db.session.add(newUser)
        db.session.commit()
        return newUser
    
    def login(self, email, passw, username):
        foundUser = users.query.filter_by(email = email, passw = passw, username = username).first()
        if foundUser is not None:
            foundUser.activeUser = True
            db.session.commit()
            return foundUser
        else:
            return None

    def find_active_user(self):
        return users.query.filter_by(activeUser = True).first()

    def get_user_by_id(self, id):
        return users.query.filter_by(account_id = id).first()
    
    def get_post_by_id(self, id):
        return posts.query.filter_by(post_id = id).first()

    def get_all_posts(self):
        allPosts = posts.query.all()
        return allPosts
    
    def get_all_active_posts(self):
        activeUser = users.query.filter_by(activeUser = True).first().username
        activePosts = posts.query.filter(posts.author.like(activeUser)).all()
        return activePosts
    
    def create_post(self, title, body, author, tag):
        newPost = posts(title = title, body = body, author = author, tag = tag)
        db.session.add(newPost)
        db.session.commit()
        return newPost
    
    def update_post(self, target, title, body, tag):
        target.title = title
        target.body = body
        target.tag = tag
        db.session.commit()
        return

    def filter_by_tag(self, tag):
        return posts.query.filter_by(tag = tag)


website_repository_singleton = WebsiteRepository()
