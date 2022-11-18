
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "CONN"
    oColor = "I2C"
    oDesc = "QWIIC"
    oIndex = "01"
    hexID = "MCQI01"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchingBlock'].append('BLOCK-CONN-I2C-STAN-01')
    newPart['oompParts'].append({'J1': {'OOMPID': 'HEAD-JSTSH-X-PI04-RS'}})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

