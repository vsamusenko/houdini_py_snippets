import hou

def forceObjects():
    for node in hou.selectedNodes():
        param = node.parm("PARAM_IN_QUESTION_OBJ")
        searchStr = param.evalAsString()

        matchStr = "IN_STRING"
        replaceStr = "REPL_STRING"

        if matchStr in searchStr:
            replStr = searchStr.replace(matchStr, replaceStr)
            param.set(replStr)


def forceLights():
    for node in hou.selectedNodes():
        param = node.parm("PARAM_IN_QUESTION_LIGHT")
        searchStr = param.evalAsString()

        matchStr = "IN_STRING"
        replaceStr = "REPL_STRING"

        if matchStr in searchStr:
            replStr = searchStr.replace(matchStr, replaceStr)
            param.set(replStr)


forceObjects()
forceLights()