
######  Auto translated oomp file

def load(newPart,it):
    oType = "MODULE"
    oSize = "POWE"
    oColor = "KAP2112K"
    oDesc = "SO235"
    oIndex = "V33D"
    hexID = "MP2112"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['matchingBlock'].append('BLOCK-POW-STAN-STAN-01')
    newPart['oompParts'].append({'U1': {'OOMPID': 'VREG-SO235-X-KAP2112K-V33D'}, 'C1': {'OOMPID': 'CAPC-0603-X-NF100-V50'}, 'C2': {'OOMPID': 'CAPC-0603-X-NF100-V50'}})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

