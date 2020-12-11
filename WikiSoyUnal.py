

from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():
    listagood=[]
    url = "https://tambinsoyunal.fandom.com/es/wiki/PAPA"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    texto = soup.get_text()
    lineas = [linea for linea in texto.split('\n') if linea != '' ]
    #print(lineas)
    for linea in lineas:
        linea.strip()
        if linea[0]==" " and linea[-1]==".":
            for posi in range(0, len(linea) - 4):
                if linea[posi:posi + 4] == "El P":
                    sale = linea[posi:]
                    listagood.append(sale)

                    break
            break
    for linea in range(0,len(lineas)):
        if lineas[linea]=="Cálculo del PAPA":
            newlist=[lineas[linea],lineas[linea+1],lineas[linea+2],lineas[linea+3], lineas[linea+4], lineas[linea+5], lineas[linea+6], lineas[linea+7]]
            listagood.append(newlist)

        elif lineas[linea]=="Relación entre PAPA y PA":
            newlist = [lineas[linea], lineas[linea + 1], lineas[linea + 2]]
            listagood.append(newlist)

        elif lineas[linea]=="Implicaciones a los estudiantes":
            newlist = lineas[linea:linea+15]
            listagood.append(newlist)

        elif lineas[linea]=="Se podría clasificar a un estudiante según los siguientes criterios:":
            newlist = lineas[linea+1:linea + 9]
            listagood.append(newlist)

        elif lineas[linea]==" PAPPI ":
            newlist = lineas[linea:linea + 6]
            listagood.append(newlist)

    lineasguarda=html.encode()
    texto_limpio = '\n'.join(lineas)
    #print(texto_limpio)
    f = open("soyunalpappa.html","wb") #w: write
    f.write(lineasguarda)
    f.close()
    z = open("aceptadosoyunal","w") #w: write
    z.write(texto_limpio)
    z.close()
    for caracter in listagood:
        if type(caracter)==list:
            for lista1 in caracter:
                print(lista1)
        else:
            print(caracter)

main()