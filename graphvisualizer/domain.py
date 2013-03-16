from graphvisualizer import Node

class Domain(Node):
    style = None

    def __init__(self, graph, vertex=None):
        Node.__init__(self, graph, vertex)

        self.type = 'domain'

        if Domain.style is None:
            Domain.style = graph.new_vertex_style(0)
            graph.set_vertex_style_attribute(Domain.style, "color", "#0000CC")

    def getCaption(self):
        return self.vertex['domain']