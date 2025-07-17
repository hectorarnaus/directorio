from autowordpress import WpElement
from autowordpress import Image

class WpImage(WpElement):

    def __init__(self,img):
        self.img=img
        print(f'<!-- wp:image {{"id":{self.img.get_id()},"sizeSlug":"large","align":"center","linkDestination":"none"}} --> <figure class="wp-block-image aligncenter size-full"><img src="{self.img.get_url()}" alt="{self.img.get_alt_text()}" class="wp-image-{self.img.get_id()}"/></figure><!-- /wp:image -->\n\n')
        self.content=f'<!-- wp:image {{"id":{self.img.get_id()},"sizeSlug":"large","align":"center","linkDestination":"none"}} --> <figure class="wp-block-image aligncenter size-full"><img src="{self.img.get_url()}" alt="{self.img.get_alt_text()}" class="wp-image-{self.img.get_id()}"/></figure><!-- /wp:image -->\n\n'
