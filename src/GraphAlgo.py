from asyncio import PriorityQueue
from typing import List
import json
import os
from src import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    """This abstract class represents an interface of a graph."""

    def __init__(self, graph):
        self.nodes = graph.get_all_v
        self.edges = {(e['src'], e['dest']): e['w'] for e in graph.edges}


    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as f:
                dict = json.load(f)
                graph = DiGraph()
            for n in dict["nodes"].values():
                self.add_node(n["id"], (n['pos']['x'], n['pos']['y']))
            edges = dict["Edges"]
            for e in edges:
                graph.add_edge(e["src"], e["dest"], e["w"])
            self.graph = graph
            return True
        except Exception:
            return False



    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as f:
                json.dump(self, indent=2, fp=f, default=lambda a: a.__dict__)
                return True
        except Exception:
            return False

    def dijkstra(self, src) -> (list, list):
        D = {v: float('inf') for v in range(self.graph.nodes)}
        D[src] = 0

        pq = PriorityQueue()
        pq.put((0, src))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.graph.visited.append(current_vertex)

            for neighbor in range(self.graph.nodes):
                if self.graph.edges[current_vertex][neighbor] != -1:
                    distance = self.graph.edges[current_vertex][neighbor]
                    if neighbor not in self.graph.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

    def shortest_path(self, id1: int, id2: int) -> (float, list):


    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        raise NotImplementedError