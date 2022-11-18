
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "CONN"
    oColor = "RASP"
    oDesc = "PICO"
    oIndex = "2040"
    hexID = "MCRP2040"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchingBlock'].append('BLOCK-CONN-RASP-PICO-2040')
    newPart['oompParts'].append('J1,HEAD-I01-X-PI20-01')
    newPart['oompParts'].append('J2,HEAD-I01-X-PI20-01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

