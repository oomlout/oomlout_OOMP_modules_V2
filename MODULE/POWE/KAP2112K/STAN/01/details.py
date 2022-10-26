
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "POWE"
    oColor = "KAP2112K"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "MP2112"

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

