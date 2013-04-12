Graph-Visualizer
================

With having a large amount of data comes the need to look at and read the large amount of data. Using [UbiGraph](http://ubietylab.net/ubigraph/) in conjunction with this Python program, our graph of web history can be easily visualized and interpreted.

Running this program
--------------------

1. Obtain a copy of the graph, or preferably just a small portion of the graph. It must contain a user as a starting location.
2. Convert the graph using the [Graph Export Tool](https://github.com/WhySearchTwice/Data-and-Rest-Services/tree/master/graph-export). This will transform the JSON exported from Faunus into a JSON file readable by this application and a GraphML file. For this application you will only need the new JSON file.
3. Start UbiGraph server.
4. Using the [example](https://github.com/WhySearchTwice/Graph-Visualizer/blob/master/graphvisualizer/test/singleUserTest.py) run the application, informing it what file to read from and what user to start from.
