from graphvisualizer import Node

class Device(Node):
    style = None

    def __init__(self, graph, vertex=None):
        Node.__init__(self, graph, vertex)

        self.type = 'device'

        if Device.style is None:
            Device.style = graph.new_vertex_style(0)
            graph.set_vertex_style_attribute(Device.style, "color", "#666600")

    def getCaption(self):
        return 'Device: %s' % self.getId()