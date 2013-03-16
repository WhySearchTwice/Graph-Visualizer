from graphvisualizer import Node

class PageView(Node):
    style = None

    def __init__(self, graph, vertex=None):
        Node.__init__(self, graph, vertex)

        self.type = 'pageView'

        if PageView.style is None:
            PageView.style = graph.new_vertex_style(0)
            graph.set_vertex_style_attribute(PageView.style, "color", "#CCCC99")

    def getCaption(self):
        return self.vertex['pageUrl']