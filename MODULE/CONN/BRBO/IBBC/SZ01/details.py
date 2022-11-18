
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "CONN"
    oColor = "BRBO"
    oDesc = "IBBC"
    oIndex = "SZ01"
    hexID = "MCBI1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchingBlock'].append('BLOCK-CONN-I2C-EXTRA-01')
    newPart['oompParts'].append('J1,HEAD-I01-X-PI06-01')
    newPart['oompParts'].append('J2,HEAD-I01-X-PI06-01')
    newPart['componentModules'].append('M1,MODULE-CONN-I2C-QWIIC-01')
    newPart['componentModules'].append('M2,MODULE-CONN-I2C-QWIIC-01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

