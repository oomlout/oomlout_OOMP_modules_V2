
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "CONN"
    oColor = "OOBB"
    oDesc = "BA"
    oIndex = "01"
    hexID = "MCOBA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchingBlock'].append('BLOCK-CONN-OOBB-BA-01')
    newPart['oompParts'].append({'J1': {'OOMPID': 'HEAD-I01-X-PI03-RA'}})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

