
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "POWE"
    oColor = "KLD1117"
    oDesc = "SO23"
    oIndex = "01"
    hexID = "MP1117"

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

