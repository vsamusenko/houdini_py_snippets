import hou

def setIterations(kwargs):
    node = kwargs['node']

    idx = hou.parm(node.path() + '/noiseType').eval()
    iterations = hou.parm(node.path() + '/Parms/numTypeVariations').eval()[str(idx)]

    iteParm = hou.parm(node.path() + '/iterations')
    iteParm.set(iterations)

    labels = ["Perlin", "Original Perlin", "Sparse Convolution", "Alligator", "Simplex", "Analytic Perlin",
              "Analytic Simplex"]
    items = []
    itm = 0
    for l in labels:
        items.append(str(itm))
        itm += 1

    varParm = hou.parm(node.path() + '/noiseVaiations')
    varParmTmp = None
    if varParm == None:
        varParmTmp = hou.IntParmTemplate('noiseVaiations', 'Variations', 1)
        varParmTmp.setMenuType(hou.menuType.Normal)
        varParmTmp.setScriptCallback('hou.phm().printSelection(kwargs)')
        varParmTmp.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    else:
        varParmTmp = varParm.parmTemplate()

    varParmTmp.setMenuItems(items)
    varParmTmp.setMenuLabels(labels)

    parmGrp = node.parmTemplateGroup()
    if parmGrp.find('noiseVaiations') == None:
        parmGrp.insertAfter('noiseType', varParmTmp)
    else:
        parmGrp.replace('noiseVaiations', varParmTmp)

    node.setParmTemplateGroup(parmGrp)