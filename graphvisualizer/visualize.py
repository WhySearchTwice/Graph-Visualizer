import xmlrpclib
import json

from graphvisualizer import User, Device, PageView, Domain

print('starting')

# Create an object to represent our server.
server_url = 'http://127.0.0.1:20738/RPC2'
server = xmlrpclib.Server(server_url)
G = server.ubigraph

G.clear()

# Default vertex style
G.set_vertex_style_attribute(0, "shape", "sphere")
G.set_vertex_style_attribute(0, "shapedetail", "1")
G.set_vertex_style_attribute(0, "size", "0.5")

# Vertex style for users
userStyle = G.new_vertex_style(0)
G.set_vertex_style_attribute(userStyle, "color", "#FFFF00")

deviceStyle = G.new_vertex_style(0)
G.set_vertex_style_attribute(deviceStyle, "color", "#666600")

pageStyle = G.new_vertex_style(0)
G.set_vertex_style_attribute(pageStyle, "color", "#CCCC99")

domainStyle = G.new_vertex_style(0)
G.set_vertex_style_attribute(domainStyle, "color", "#0000CC")


users = {}
devices = {}
pageViews = {}
domains = {}

with open('largeSample.json') as file:
    data = json.load(file)

    for vertex in data['graph']['vertices']:
        if vertex['type'] == 'user':
            user = User(vertex)
            users[user.getId()] = user
        elif vertex['type'] == 'device':
            device = Device(vertex)
            devices[device.getId()] = device
        elif vertex['type'] == 'pageView':
            pageView = PageView(vertex)
            pageViews[pageView.getId()] = pageView
        elif vertex['type'] == 'domain':
            domain = Domain(vertex)
            domains[domain.getId()] = domain

    for edge in data['graph']['edges']:
        if edge['_label'] == 'owns':
            users[edge['_outV']].addChild(devices[edge['_inV']])
        if edge['_label'] == 'viewed':
            devices[edge['_outV']].addChild(pageViews[edge['_inV']])
        if edge['_label'] == 'under':
            pageViews[edge['_outV']].addChild(domains[edge['_inV']])



for userId in users:
    user = users[userId]

    G.new_vertex_w_id(user.getId())
    G.change_vertex_style(user.getId(), userStyle)

    for device in user.getAllChildren():
        G.new_vertex_w_id(device.getId())
        G.change_vertex_style(device.getId(), deviceStyle)
        G.new_edge(user.getId(), device.getId())

        for pageView in device.getAllChildren():
            G.new_vertex_w_id(pageView.getId())
            G.change_vertex_style(pageView.getId(), pageStyle)
            G.new_edge(device.getId(), pageView.getId())

            for domain in pageView.getAllChildren():
                G.new_vertex_w_id(domain.getId())
                G.change_vertex_style(domain.getId(), domainStyle)
                G.new_edge(pageView.getId(), domain.getId())



print(len(users))
print(len(devices))
print(len(pageViews))
print(len(domains))