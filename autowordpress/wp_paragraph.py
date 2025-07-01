from autowordpress import WpElement

class WpParagraph(WpElement):

    def __init__(self,content):
        self.content=f'<!-- wp:paragraph -->\n<p>{content}</p>\n<!-- /wp:paragraph -->\n\n'
    def get_element(self):
        return self.content
