import xmlrpclib
import json

from graphvisualizer.user import User

print('starting')

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

# Set default edge style
G.set_edge_style_attribute(0, "oriented", "true")
G.set_edge_style_attribute(0, "color", "#C5892F")

# Default vertex style
G.set_vertex_style_attribute(0, "shape", "sphere")

# Vertex style for users
userStyle = G.new_vertex_style(0)
G.set_vertex_style_attribute(userStyle, "color", "#80219C")
G.set_vertex_style_attribute(userStyle, "shape", "sphere")
G.set_vertex_style_attribute(userStyle, "size", "3.0")





users = []
devices = []
pageViews = []
domains = []

with open('output.json') as file:
    data = json.load(file)

    for vertex in data['graph']['vertices']:
        if vertex['type'] == 'user':
            users.append(User(vertex))
        elif vertex['type'] == 'device':
            devices.append(vertex)
        elif vertex['type'] == 'pageView':
            pageViews.append(vertex)
        elif vertex['type'] == 'domain':
            domains.append(vertex)

print(len(users))
print(len(devices))
print(len(pageViews))
print(len(domains))