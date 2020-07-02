t=()
t=list(t)
for j in ["Tréboles","Corazones","Picas","Diamantes"]:
    for i in range(13):
        if (i+1)==11:
            t.insert(len(t),"J de " + j)
        elif (i+1)==12:
            t.insert(len(t),"Q de " + j)
        elif (i+1)==13:
            t.insert(len(t),"K de " + j)
        elif (i+1)==1:
            t.insert(len(t),"A de " + j)
        else:
            t.insert(len(t),"{} de {} ".format((i+1),j))
t=tuple(t)
print(t)
