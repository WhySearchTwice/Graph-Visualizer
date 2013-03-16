from time import sleep

class Node():
    def __init__(self, graph, vertex=None):
        if vertex is not None:
            self.vertex = vertex

        self.graphReference = graph
        self.children = {}
        self.labelVisible = False
        self.hasBeenDrawn = False

    def __repr__(self):
        return self.vertex.__repr__()

    def setVertex(self, vertex):
        self.vertex = vertex

    def getId(self):
        if self.vertex is not None:
            return self.vertex['_id']

    def addChild(self, child):
        self.children[child.getId()] = child

    def deletePageView(self, child):
        self.children.pop(child.getId())

    def getAllChildren(self):
        for child in self.children:
            yield self.children[child]

    def getCaption(self):
        return 'Default Node'

    def toggleLabel(self):
        if self.labelVisible:
            self.graphReference.set_vertex_attribute(self.getId(), 'label', '')
        else:
            self.graphReference.set_vertex_attribute(self.getId(), 'label', self.getCaption())

        self.labelVisible = not self.labelVisible

    def drawSelfRecursively(self):
        self.drawSelf()
        sleep(0.01)

        # Draw all the children and connect to them
        for child in self.getAllChildren():
            child.drawSelf()
            self.graphReference.new_edge(self.getId(), child.getId())

        # Recurse on each of the children
        for child in self.getAllChildren():
            child.drawSelfRecursively()

    def drawSelf(self):
        if not self.hasBeenDrawn:
            self.graphReference.new_vertex_w_id(self.getId())
            self.graphReference.change_vertex_style(self.getId(), self.style)
            self.hasBeenDrawn = True

