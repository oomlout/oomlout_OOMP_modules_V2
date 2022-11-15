
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "MOSN"
    oColor = "K4184"
    oDesc = "T252"
    oIndex = "TL"
    hexID = "MMN4184252TL"

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

