import hou

node = hou.node('PATH/TO/NODE/WITH/KEYFRAMES')
geo = hou.pwd().geometry()
parm = node.parm("TARGET_PARAM")

firstkey = int(parm.keyframes()[0].frame())
secondkey = int(parm.keyframes()[1].frame())
first = geo.addAttrib(hou.attribType.Point, "first", 0)
second = geo.addAttrib(hou.attribType.Point, "second", 0)

for pt in geo.points():
    pt.setAttribValue(first, firstkey)
    pt.setAttribValue(second, secondkey)