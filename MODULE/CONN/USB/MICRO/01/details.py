
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "CONN"
    oColor = "USB"
    oDesc = "MICRO"
    oIndex = "01"
    hexID = "MCUMC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['oompParts'].append({'J1': {'OOMPID': ' USBS-TC-X-K31-01'}})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

