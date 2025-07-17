import os
from extraer_datos_excel import *
from pixabay_python import PixabayClient, Category, download,ImageOrientation
from google_images_search import GoogleImagesSearch

def obten_nombre_fichero(url):
    datos=url.split("/")
    return datos[-1]


#https://pypi.org/project/Google-Images-Search/
def obten_imagen_google(nombre,carpeta,num,provincia=True):
    gis = GoogleImagesSearch("AIzaSyD8Gxqlbw9uVepbvc6tx4j7L-TvfqHQAXw","429c521e05e754bd1")
    _search_params = {
        'q': nombre+" españa",
        'num': 5,
        'fileType': 'jpg',
        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
        'imgSize': 'xlarge',
        'imgDominantColor': 'imgDominantColorUndefined',
        'imgColorType': 'color'
    }

    try:
        gis.search(search_params=_search_params)
        ficheros=[]
        for image in gis.results():
            image.url 
            image.referrer_url        
            image.download(carpeta) 
            ficheros.append(image.path)
        i=0
        if len(ficheros)==0:
            return False
        while i<len(ficheros):
            print(ficheros[i])
            if provincia==True:
                os.rename(ficheros[i],carpeta+"/"+nombre+str(num+i)+".jpg")
            else:
                os.rename(ficheros[i],carpeta+"/"+nombre+"_"+provincia+str(num+i)+".jpg")
            i+=1
        return True
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return False
  



def obten_imagen_pixabay(nombre,carpeta,num,provincia=True):
    client = PixabayClient(apiKey="50941131-9e334548d8a355bbadf6f5388")
    searchResult = client.searchImage(q=nombre,category=Category.PLACES)
    hitsList = list(searchResult.hits)
    if len(hitsList)>0:
        i=num
        while i<len(hitsList) and i<5:
            print(f"i={i}\n")
            download(url=hitsList[i].largeImageURL, outputDir=carpeta)
            fichero=obten_nombre_fichero(hitsList[i].largeImageURL)
            if provincia==True:
                os.rename(carpeta+"/"+fichero,carpeta+"/"+nombre+str(i)+".jpg")
            else:
                os.rename(carpeta+"/"+fichero,carpeta+"/"+nombre+"_"+provincia+str(i)+".jpg")
            i+=1
        return True
    return False


'''municipios=obten_lista_municipios("castilla_leon_1.xlsx")
for municipio in municipios:
    print(municipio[0])
    res=obten_imagen_pixabay(municipio[0],"municipio",0,municipio[1])
    if res==False:
        obten_imagen_google(municipio[0],"municipio",5,municipio[1])
'''
provincias=obten_lista_provincias("castilla_leon_1.xlsx")
for provincia in provincias:
    print(provincia)
    res=obten_imagen_pixabay(provincia,"provincia",0)
    if res==False:
        obten_imagen_google(provincia,"provincia",5)
   