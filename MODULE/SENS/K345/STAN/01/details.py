
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "SENS"
    oColor = "K345"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "MS345"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchingBlock'].append('BLOCK-SENS-ACCEL-I2C-01')
    newPart['oompParts'].append({'U1': {'OOMPID': 'SENS-LG14-X-K345-01'}})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

