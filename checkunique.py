teststr = "abacd"

def checkunique(tmpstr):
    print("Function to check unique letter word")
    letterset = set()
    for l in tmpstr:
        if l in letterset:
            return False
        letterset.add(l)
    return True

def checkunique1(tmpstr):
    return len(set(tmpstr)) == len(tmpstr)

def listFunctions():
    emptyList = []

    emptyList.insert(0,1)
    emptyList.insert(0,2)
    emptyList.insert(0,3)

    print(emptyList)


#print(checkunique1(teststr))
listFunctions()
