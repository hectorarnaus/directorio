import os
import urllib.request
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts

class Image():
    def __init__(self,path,alt_text):
        self.path=path
        self.alt_text=alt_text
        self.id=0

    def get_alt_text(self):
        return self.alt_text
    
    def get_url(self):
        return self.link
    def get_id(self):
        return self.id
    
    def get_correct_path(self):
        path_limpio=self.path.split("/")
        pos=len(path_limpio)
        return path_limpio[pos-1]
    
    def upload(self,wp):        
        data = {'name': self.get_correct_path(),'type': 'image/jpg',}
        with open(self.path,'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())
        response=wp.get_connection().call(media.UploadFile(data))
        self.id=response['id']
        self.link=response['link']
        wppimage = wp.get_connection().call(posts.GetPost(response['id']))
        wppimage.custom_fields = [{'key':'_wp_attachment_image_alt','value':self.get_alt_text()}]
        wppimage.title=self.get_alt_text()
        wppimage.content = self.get_alt_text()
        success = wp.get_connection().call(posts.EditPost(response['id'],wppimage))
        
        if not success: print('Editing alt text for image [{}] failed'.format(self.get_alt_text()))
       
        
#https://python-wordpress-xmlrpc.readthedocs.io/en/latest/examples/media.html
