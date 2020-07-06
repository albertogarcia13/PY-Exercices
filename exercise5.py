def telegrama(data):
    data = data.replace(".", " STOP")
    data1 = data.split()
    frase = ""
    for i in data1:
        if len(i)>5:
            frase = frase + i[:5] + "@ "
        else:
            frase = frase + i + " "
    frase = frase + "STOPSTOP"
    return(frase.strip())

print(telegrama("holaaa queee. talasdfasdf"))
