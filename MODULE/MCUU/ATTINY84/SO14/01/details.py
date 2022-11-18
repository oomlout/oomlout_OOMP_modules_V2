
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "MCUU"
    oColor = "ATTINY84"
    oDesc = "SO14"
    oIndex = "01"
    hexID = "MMAT84S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchingBlock'].append('BLOCK-MCUU-STAN-STAN-01')
    newPart['oompParts'].append('U1,MCUU-SC14-84-ATTINY-01')
    newPart['oompParts'].append('C1,CAPC-0603-X-NF100-V50')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

