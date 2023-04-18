
from src.models import db, movie

class WebsiteRepository:
    
    def get_all_posts(self):
        # TODO get all posts from the DB
        return 

# Singleton to be used in other modules
website_repository_singleton = WebsiteRepository()