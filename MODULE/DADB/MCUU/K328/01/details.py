
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "DADB"
    oColor = "MCUU"
    oDesc = "K328"
    oIndex = "01"
    hexID = "MD328M"

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

