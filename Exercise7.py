import queue
import urllib.request
import re
from urllib.parse import urljoin

cont = 0

def descargar(pagina,cont):
    if pagina != "https://www.fhios.es/blog/" :
        try:
            peticion = urllib.request.Request(pagina)
            html = urllib.request.urlopen(peticion).read()
            print("[*] Descarga OK >>", pagina)
            html1 = html.decode("utf8")
            print(html1.count("fhios"))
            cont = cont + html1.count("fhios")
        except:
            return None, cont
    else:
        return None, cont

    return html, cont


def rastrearEnlaces(pagina,cont):
    visitados = [pagina]
    buscaEnlaces = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    print("Buscando enlaces en",pagina)
    html = descargar(pagina,cont)
    enlaces = buscaEnlaces.findall(str(html[0]))
    for enlace in enlaces:
        if enlace not in visitados :
            html = descargar(enlace,html[1])
            visitados.append(enlace)
    return html[1]


cont = 0
print("Numero total", rastrearEnlaces("https://www.fhios.es",cont))
