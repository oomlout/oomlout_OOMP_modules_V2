
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "MCUU"
    oColor = "ATTINY84"
    oDesc = "SO14"
    oIndex = "01"
    hexID = "SC"

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

