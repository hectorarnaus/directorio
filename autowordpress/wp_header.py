from autowordpress import WpElement

class WpHeader(WpElement):

    def __init__(self,content,level):
        self.level=level
        if self.level==2:
            self.content= f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{content}</h2>\n<!-- /wp:heading -->\n\n'
        elif 2<self.level<7:
            self.content= f'<!-- wp:heading {{"level":{self.level}}} -->\n<h{self.level} class="wp-block-heading">{self.content}</h{self.level}>\n<!-- /wp:heading -->\n\n'
    