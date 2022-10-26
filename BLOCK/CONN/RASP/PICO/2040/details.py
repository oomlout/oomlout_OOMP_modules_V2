
######  Auto translated oomp file

def load(newPart,it):
    oType = "BLOCK"
    oSize = "CONN"
    oColor = "RASP"
    oDesc = "PICO"
    oIndex = "2040"
    hexID = "BCRP2040"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)



    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

