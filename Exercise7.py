import urllib.request

fp = urllib.request.urlopen("https://www.fhios.es")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()
print("La cantidad de veces que esta en la pagina https://www.fhios.es la palabra fhios es: {}".format(mystr.find("fhios")))
#print(myst
