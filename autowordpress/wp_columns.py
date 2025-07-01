from autowordpress import WpElement

class WpColumns(WpElement):
    def __init__(self,content):
        self.content='<!-- wp:columns -->\n<div class="wp-block-columns">'
        for contenido in content:
            self.content+=f'<!-- wp:column -->\n<div class="wp-block-column">{contenido}\n</div>\n<!-- /wp:column -->'
        self.content+='</div>\n<!-- /wp:columns -->'
       
   