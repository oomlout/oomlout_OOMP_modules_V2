
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "CONN"
    oColor = "ISP"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "MCISP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchingBlock'].append('BLOCK-CONN-PROG-STAN-01')
    newPart['oompParts'].append('J1,HEAD-I01-X-PI2X03-01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

