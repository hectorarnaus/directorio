def slurguiza(texto):
    texto=texto.strip()
    
    texto=texto.replace("de","")
    texto=texto.replace("el","")
    texto=texto.replace("la","")
    texto=texto.replace("los","")
    texto=texto.replace("las","")
    texto=texto.replace(" ","-")
    while texto.find("--")!=-1:
        texto=texto.replace("--","-")
    texto=texto.lower()
    return texto

print(slurguiza("Santa Cruz de los Tenerifes"))
