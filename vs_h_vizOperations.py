import hou

visualize_node = hou.node('/PATH/TO/VIZ_NODE')
node_category = hou.viewportVisualizerCategory.Node

visualizer_list = hou.viewportVisualizers.visualizers(category=node_category, node=visualize_node)

type_list = hou.viewportVisualizers.types()
marker_type = type_list[0]

visualizer = hou.viewportVisualizers.createVisualizer(marker_type, category=node_category, node=visualize_node)

value = 'TEST'

visualizer.setType(marker_type)
visualizer.setParm('parm_name', value)