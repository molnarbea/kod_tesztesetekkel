def egyedi_betuk(szoveg:str=""):
    lista=[]
    stat={}
    i=0
    while len(szoveg) > i:
        if  szoveg[i].isalpha():
            betu=szoveg[i].lower()
            stat[betu]=stat.get(betu, 0)+1
            if lista.count(szoveg[i]) == 0:
                lista.append(betu)
        i+=1
    stat = dict(sorted(stat.items()))
    return stat