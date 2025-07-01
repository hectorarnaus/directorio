from autowordpress import WpElement

class WpList(WpElement):

    def __init__(self,items,ordered):
        if ordered:
            self.content='<!-- wp:list {"ordered":true} --><ol>'
            for item in items:
                self.content+=f'<!-- wp:list-item --><li>{item}</li><!-- /wp:list-item -->\n'
            self.content+='</ol><!-- /wp:list -->\n\n'
        else:
            self.content='<!-- wp:list --><ul>'
            for item in items:
                self.content+=f'<!-- wp:list-item --><li>{item}</li><!-- /wp:list-item -->\n'
            self.content+='</ul><!-- /wp:list -->\n\n' 
