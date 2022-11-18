
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "CONN"
    oColor = "OOML"
    oDesc = "LED2X3"
    oIndex = "01"
    hexID = "MCOL23"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oompParts'].append({'J1': {'OOMPID': 'HEAD-I01-X-PI2X03-01'}})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

