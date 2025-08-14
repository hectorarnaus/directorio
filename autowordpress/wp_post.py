#pip install python-wordpress-xmlrpc.

import os
import urllib.request
from funciones import sluguiza
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

class WpPost():
    def __init__(self,titulo,categoria=None):
        self.post = WordPressPost()
        self.post.title=titulo
        self.post.content=""
        if categoria==None:
          self.post.terms_names = {
            'post_tag': [],
            'category': []
          }
        else:
          self.post.terms_names = {
              'post_tag': [],
              'category': [sluguiza(categoria)]
            }

        self.post.post_status = 'publish'
        
    def get_post(self):
        return self.post
    
    def add_element(self,element):
      self.post.content+=str(element)
    
    def add_tag(self,tag):
      self.post.terms_names['post_tag'].append(tag)
    
    def add_category(self,category):
      self.post.terms_names['category'].append(category)
        
    def setContent(self,content):
       self.post.content=content

    def set_category(self,category):
      self.post.terms_names['category']=[]
      self.post.terms_names['category'].append(category)

    def set_slug(self,slug):
       self.post.slug=slug

