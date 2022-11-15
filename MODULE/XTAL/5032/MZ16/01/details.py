
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "XTAL"
    oColor = "5032"
    oDesc = "MZ16"
    oIndex = "01"
    hexID = "MX53M16"

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

