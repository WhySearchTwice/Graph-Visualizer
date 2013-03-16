from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib
import json

from graphvisualizer import User, Device, PageView, Domain

class Visualizer():
    def __init__(self, server_url='http://127.0.0.1:20738/RPC2', serve_port=20739, serve_host='127.0.0.1'):
        self.serve_port = serve_port
        self.serve_host = serve_host

        # Create the graph
        server = xmlrpclib.Server(server_url)
        self.graph = server.ubigraph
        self.graph.clear()

        # Set the default style
        self.graph.set_vertex_style_attribute(0, "shape", "sphere")
        self.graph.set_vertex_style_attribute(0, "shapedetail", "7")
        self.graph.set_vertex_style_attribute(0, "size", "0.5")
        self.graph.set_vertex_style_attribute(0, "callback_left_doubleclick", "http://127.0.0.1:20739/vertex_callback")

    def setInputFile(self, filename):
        self.jsonFilename = filename

    def setUsers(self, userList):
        self.usersToDraw = userList

    def loadJson(self):
        self.users = {}
        self.devices = {}
        self.pageViews = {}
        self.domains = {}

        with open(self.jsonFilename) as file:
            data = json.load(file)

            for vertex in data['graph']['vertices']:
                if vertex['type'] == 'user':
                    user = User(self.graph, vertex)
                    self.users[user.getId()] = user
                elif vertex['type'] == 'device':
                    device = Device(self.graph, vertex)
                    self.devices[device.getId()] = device
                elif vertex['type'] == 'pageView':
                    pageView = PageView(self.graph, vertex)
                    self.pageViews[pageView.getId()] = pageView
                elif vertex['type'] == 'domain':
                    domain = Domain(self.graph, vertex)
                    self.domains[domain.getId()] = domain

            for edge in data['graph']['edges']:
                if edge['_label'] == 'owns':
                    self.users[edge['_outV']].addChild(self.devices[edge['_inV']])
                if edge['_label'] == 'viewed':
                    self.devices[edge['_outV']].addChild(self.pageViews[edge['_inV']])
                if edge['_label'] == 'under':
                    self.pageViews[edge['_outV']].addChild(self.domains[edge['_inV']])

    def drawUsers(self):
        for userId in self.usersToDraw:
            self.users[userId].drawSelfRecursively()

    def vertex_callback(self, v):
        try:
            if v in self.users:
                self.users[v].toggleLabel()
            elif v in self.devices:
                self.devices[v].toggleLabel()
            elif v in self.pageViews:
                self.pageViews[v].toggleLabel()
            elif v in self.domains:
                self.domains[v].toggleLabel()
            else:
                return -1
            return 0
        except:
            return -1

    def runSimulation(self):
        self.loadJson()
        self.drawUsers()

        callbackServer = SimpleXMLRPCServer((self.serve_host, self.serve_port))
        callbackServer.register_introspection_functions()
        callbackServer.register_function(self.vertex_callback)
        print("Listening for callbacks")
        callbackServer.serve_forever()