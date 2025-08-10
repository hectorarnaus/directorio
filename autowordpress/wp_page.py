#pip install python-wordpress-xmlrpc.

import os
import urllib.request
from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc import Client, WordPressPage
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

class WpPage():
    def __init__(self,titulo):
        self.page = WordPressPage()
        self.page.title=titulo
        self.page.content=""
        self.page.terms_names = {
          'page_tag': []
        }
    def get_page(self):
        return self.page
    
    def add_element(self,element):
      self.page.content+=str(element)
    
    def add_tag(self,tag):
      self.page.terms_names['page_tag'].append(tag)
    '''
    def add_category(self,category):
      self.page.terms_names['category'].append(category)
       ''' 
    def setContent(self,content):
       self.page.content=content

    def set_slug(self,slug):
       self.page.slug=slug
