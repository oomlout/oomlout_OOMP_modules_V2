
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "CONN"
    oColor = "DCJP"
    oDesc = "21D"
    oIndex = "01"
    hexID = "MCD2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchingBlock'].append('BLOCK-CONN-POWE-STAN-01')
    newPart['oompParts'].append({'J1': {'OOMPID': 'DCJP-21D-X-STAN-01'}})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

