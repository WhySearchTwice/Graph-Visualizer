class Node():
    def __init__(self, vertex=None):
        if vertex is not None:
            self.vertex = vertex

        self.children = {}

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