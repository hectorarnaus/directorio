
from wordpress_xmlrpc import Client, WordPressTerm
from wordpress_xmlrpc.methods import taxonomies

class WPCategory:
    def __init__(self,nombre,slug, padre=None):
        
        self.nombre=nombre
        self.slug=slug
        self.padre=padre
        self.id=0

    def creaCategoria(self,wp):        

        nueva_categoria = WordPressTerm()
        nueva_categoria.taxonomy = 'category'
        nueva_categoria.name = self.nombre
        nueva_categoria.slug = self.slug

        if self.padre:
            nueva_categoria.parent = int(self.padre)  # ID de la categoría padre

        cat_id = wp.get_connection().call(taxonomies.NewTerm(nueva_categoria))
        print(f'✅ Categoría creada: {self.nombre} (ID: {cat_id})')
        self.id=id
        return cat_id
    
    def getId(self):
        return self.id