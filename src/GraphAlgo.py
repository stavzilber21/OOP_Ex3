from typing import List
import json
import numpy as np
from numpy import double
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import random
import matplotlib.pyplot as plt
import numpy as np
import Node


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""

    # def __init__(self, graph:DiGraph)-> None:
    #     self.nodes = graph.nodes
    #     self.edges = {(e['src'], e['dest']): e['w'] for e in graph.edges}
    #     self.graph = DiGraph(self.nodes,self.edges)

    def __init__(self)-> None:
        self.nodes = {}
        self.edges = {}
        self.graph = DiGraph()

    def __repr__(self):
        return f"Nodes: {self.nodes}\nEdges: {self.edges}"

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            graph = DiGraph()
            with open(file_name, "r") as f:
                dict = json.load(f)
            for n in range(len(dict["Nodes"])):
                id = dict["Nodes"][n]["id"]
                if(len(dict["Nodes"][n])==1):
                    tuple = [np.random.uniform(35, 36), np.random.uniform(32, 33)]
                    graph.add_node(id, tuple)
                else:
                    pos = dict["Nodes"][n]["pos"]
                    tuple = pos.split(',')
                    graph.add_node(id, tuple)
            for e in range(len(dict["Edges"])):
                src = dict["Edges"][e]["src"]
                dest = dict["Edges"][e]["dest"]
                w = dict["Edges"][e]["w"]
                graph.add_edge(src,dest,w)
            self.edges=graph.edges
            self.nodes=graph.nodes
            self.graph=graph

            return True
        except Exception:
            return False


    def save_to_json(self, file_name: str) -> bool:
        try:
            dict_e = {"Edges": self.edges}
            with open(file_name, 'w') as f:
                dict_n = {"Nodes": self.nodes}
                json.dump(dict_e, indent=2, fp=f, default=lambda a: a.__dict__)
                return True
        except Exception:
            return False

    def dijkstra(self, src: int) -> (list, list):
        unvisited = list(self.nodes.keys())

        shortest_from_src = {i: float('inf') for i in unvisited}  # dist between src and other nodes
        shortest_from_src[src] = 0  # dist from src to itself is 0

        previous_nodes = {}

        while unvisited:
            current = None
            # let's find the node with the lowest weight value
            for node in unvisited:
                if current == None:
                    current = node
                elif shortest_from_src[node] < shortest_from_src[current]:
                    current = node

            neighbors = self.graph.all_out_edges_of_node(current)

            for i in range(len(neighbors)):
                m = list(neighbors[i])
                value = shortest_from_src[current] + neighbors[i].get(m[0])
                if value < shortest_from_src[m[0]]:
                    shortest_from_src[m[0]] = value
                    previous_nodes[m[0]] = current

            unvisited.remove(current)

        return previous_nodes, shortest_from_src

    def is_connected(self):
        return float('inf') not in self.dijkstra(0)[1]

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        list = self.dijkstra(id1)

        # if there is no path, return
        if list[1].get(id2) == float('inf'):
            return float('inf'), []

        answer = []
        node = id2

        while node != id1:
            answer.append(node)
            node = list[0].get(node)

        answer.append(id1)
        result = answer[::-1]

        return list[1][id2], result

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if not self.is_connected():
            return [],0.0

        copy_cities = [j for j in node_lst]# copy node list
        result = []
        answer = 0

        temp = node_lst[0]
        result.append(copy_cities[0])
        copy_cities.remove(copy_cities[0])

        while len(copy_cities)>=1:
            min = double('inf')
            same = -1
            place = -1
            for i in range(len(copy_cities)):
                open = copy_cities[i]
                dist = self.shortest_path(temp, open)[0]
                if dist < min:
                    min = dist
                    same = open
                    place = i
            list = self.shortest_path(temp,same)[1]
            while len(list)>=1:
                if list[0] not in result:
                    result.append(list[0])
                list.remove(list[0])
            q = copy_cities[place]
            temp=q
            copy_cities.remove(copy_cities[place])
            if len(copy_cities)==1 and same+1 not in result:
                result.append(same+1)

        return result, answer

        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):

        if not self.is_connected():
            return None, float('inf')

        list = []

        for i in range(len(self.nodes)):
            dist = self.dijkstra(i)[1]  # list of distances
            # find maximum
            max = 0
            for j in range(len(dist)):
                if dist[j] > max:
                    max = dist[j]
            list.insert(i, max)

        min = float('inf')

        for i in range(len(list)):
            if min > list[i]:
                min = list[i]
                node = i

        return node, min

        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        for v in self.graph.nodes.values():
            x,y,z = v.getPos()
            plt.plot(float(x), float(y), markersize=6, marker="o", color="yellow")
            plt.text(float(x), float(y), str(v.id), color="red", fontsize=6)
            for u in self.graph.edges.values():
                src=self.graph.nodes.get(u["src"])
                dest = self.graph.nodes.get(u["dest"])
                srcX=src.getPos()[0]
                srcY=src.getPos()[1]
                destX = dest.getPos()[0]
                destY = dest.getPos()[1]
            #plt.Arrow(float(srcX),float(srcY),float(destX),float(destY),1.0)
                plt.annotate("", xy=float(srcX,srcY), xytext=float(destX,destY), arrowprops=dict(arrowstyle="->"))
            #   plt.annotate("", xy=(x, y), xytext=(x_, y_), arrowprops=dict(arrowstyle="<-"))
            #plt.plot(srcX, srcY, destX, destY)
            #plt.annotate("", xy=(u,u+1), xytext=(u+10,u+11),
                         #arrowprops=dict(arrowstyle="<-", edgecolor="yellow", lw=1.5))

        plt.show()







