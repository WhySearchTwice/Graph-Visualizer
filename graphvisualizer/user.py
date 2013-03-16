from graphvisualizer import Node

class User(Node):
    style = None

    def __init__(self, graph, vertex=None):
        Node.__init__(self, graph, vertex)

        self.type = 'user'

        if User.style is None:
            User.style = graph.new_vertex_style(0)
            graph.set_vertex_style_attribute(User.style, "color", "#FFFF00")

    def getCaption(self):
        return 'User: %s' % self.getId()