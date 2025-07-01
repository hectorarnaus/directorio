from autowordpress import WpElement

class WpHTML(WpElement):

    def __init__(self,content):
        self.content=f'<!-- wp:html -->\n{content}\n<!-- /wp:html -->\n'
