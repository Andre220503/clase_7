import requests
from bs4 import BeautifulSoup
import urllib.request

for i in range(1, 11):
    respuesta = requests.get("https://xkcd.com/1/")
    html = respuesta.content
    contenido = BeatifulSoup(html,"html.parser")
    contenedor_imagen = contenido.find(id="comic")
    url_imagen = contenido.find("img")["src"]
    nombre_imagen = url_imagen.split("/")[-1]
    print(f"Descargando la imagen {nombre_imagen}")
    urllib.request.urlretrieve(f"https:{url_imagen}", nombre_imagen)