import os
import urllib.request
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost, EditPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
from autowordpress import FailedPostException



class WpConnection():
    def __init__(self,url,user,password):
        self.url=url
        self.user=user
        self.password=password
        

    def connect(self):
        self.wp = Client(self.url, self.user, self.password)
    
    def publica_post(self,post):
        if int(self.wp.call(NewPost(post.get_post()))) <=0:
            raise FailedPostException()
    
    def publica_page(self,page):
        if int(self.wp.call(NewPost(page.get_page()))) <=0:
            raise FailedPostException()
        
    def get_connection(self):
        return self.wp

    def get_posts(self):
        return self.wp.call(posts.GetPosts({'number': 1000}))

    def edit_post(self,post):
        #self.wp.call(NewPost(post.get_post()))
        wp_article=WpPost(post.title+"2")
        self.wp.call(NewPost(wp_article))

        #self.wp.call(EditPost(post.id,post))
        