
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "CONN"
    oColor = "I2C"
    oDesc = "QWIIC"
    oIndex = "I01"
    hexID = "MCQI01"

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

