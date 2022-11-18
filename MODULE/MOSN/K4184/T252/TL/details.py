
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

    newPart['matchingBlock'].append('BLOCK-MCUU-STAN-STAN-01')
    newPart['oompParts'].append({'Q1': {'OOMPID': 'MOSN-T252-X-K4184-01'}, 'Q2': {'OOMPID': 'TRNN-SO23-X-KSS8050-01'}})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

