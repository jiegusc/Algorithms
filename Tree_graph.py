# class Vertex:
#     def __init__(self, key):
#         self.id = key
#         self.connectedTo = {}
#
#     def addNeighbor(self, nbr, weight=0):
#         self.connectedTo[nbr] = weight
#
#     def __str__(self):
#         return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
#
#     def getConnections(self):
#         return self.connectedTo.keys()
#
#     def getId(self):
#         return self.id
#
#     def getWeight(self, nbr):
#         return self.connectedTo[nbr]
#
#
# class Graph:
#     def __init__(self):
#         self.vertList = {}
#         self.numVertices = 0
#
#     def addVertex(self, key):
#         self.numVertices = self.numVertices + 1
#         newVertex = Vertex(key)
#         self.vertList[key] = newVertex
#         return newVertex
#
#     def getVertex(self, n):
#         if n in self.vertList:
#             return self.vertList[n]
#         else:
#             return None
#
#     def __contains__(self, n):
#         return n in self.vertList
#
#     def addEdge(self, f, t, cost=0):
#         if f not in self.vertList:
#             nv = self.addVertex(f)
#         if t not in self.vertList:
#             nv = self.addVertex(t)
#         self.vertList[f].addNeighbor(self.vertList[t], cost)
#
#     def getVertices(self):
#         return self.vertList.keys()
#
#     def __iter__(self):
#         return iter(self.vertList.values())
#
#
# g = Graph()
# for i in range(6):
#     g.addVertex(i)
# g.addEdge(0,1,5)
# g.addEdge(0,5,2)
# g.addEdge(1,2,4)
# g.addEdge(2,3,9)
# g.addEdge(3,4,7)
# g.addEdge(3,5,3)
# g.addEdge(4,0,1)
# g.addEdge(5,4,8)
# g.addEdge(5,2,1)
#
# for v in g:
#     for w in v.getConnections():
#         print("( %s , %s )" % (v.getId(), w.getId()))



# BFS

from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)

#DFS

class DFSGraph(Graph):
    def __init__(self):
        super(DFSGraph, self).__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1

print(36%24)