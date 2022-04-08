import hou

parent = hou.node("PATH/TO/ROPS")
for node in parent.children():
   node_type_name = node.type().name()
   if node_type_name == 'arnoldshadingnetwork':
      param = node.parm("example_param")
      param.set("example_value")