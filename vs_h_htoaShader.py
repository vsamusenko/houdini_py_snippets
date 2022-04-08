import hou

shop_name = 'shaders'
shader_name = 'example_shader'
shader_type = 'standard_surface'

root = hou.node('/obj/')
shopnet = root.createNode('shopnet')
shopnet.setName(shop_name)
shopnet.moveToGoodPosition()

shop_path = '/obj/' + shop_name + '/'
root = hou.node(shop_path)
vopnet = root.createNode('arnold_vopnet')
vopnet.setName(shader_name)
vopnet.moveToGoodPosition()

vop_path = shop_path + shader_name + '/'
root = hou.node(vop_path)
shader = root.createNode(shader_type)

out = hou.node(vop_path + 'OUT_material')
out.setInput(0, shader)

root.layoutChildren()



