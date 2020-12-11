from bs4 import BeautifulSoup
from urllib.request import urlopen
def main():
    url = "http://www.sae.unal.edu.co/promedios/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    texto = soup.get_text()
    lineas = [linea for linea in texto.split('\n') if linea != '' ]
    #print(lineas)
    for linea in lineas:
        if linea[0]=="P" and linea[-1]==".":
            infoimport=linea
    print(infoimport)
    lineasguarda=html.encode()
    texto_limpio = '\n'.join(lineas)
    #print(texto_limpio)
    f = open("unalpromedios.html","wb") #w: write
    f.write(lineasguarda)
    f.close()
    z = open("aceptado","w") #w: write
    z.write(texto_limpio)
    z.close()

main()