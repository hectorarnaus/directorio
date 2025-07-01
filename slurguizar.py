def slurguiza(texto):
    texto=texto.strip()
    texto=texto.lower()
    texto=texto.replace("ñ","n")
    texto=texto.replace("á","a")
    texto=texto.replace("é","e")
    texto=texto.replace("í","i")
    texto=texto.replace("ó","o")
    texto=texto.replace("ú","u")
    texto=texto.replace("ü","u")
    texto=texto.replace("de","")
    texto=texto.replace("el","")
    texto=texto.replace("la","")
    texto=texto.replace("los","")
    texto=texto.replace("las","")
    texto=texto.replace(" ","-")
    while texto.find("--")!=-1:
        texto=texto.replace("--","-")
    
    return texto
