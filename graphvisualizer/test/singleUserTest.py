from graphvisualizer import Visualizer

v = Visualizer()

# File to be read from
v.setInputFile('largeSample.json')

# ID of the user to start from. This can optionally be ommitted to render the whole graph.
v.setUsers([92])

# Start the rendering process. This may take a while
v.runSimulation()

# Leave the server running to answer XML-RPC callbacks
