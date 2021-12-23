from GraphInterface import GraphInterface
from Node import Node

class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.mc = 0

    def __init__(self, nodes={}, edges={}) -> None:
        self.nodes = nodes
        self.edges = {(e['src'], e['dest']): e['w'] for e in edges}
        self.mc = 0

    def __repr__(self) -> str:
        return f"nodes: {self.nodes}\nedges: {self.edges}"


    """This abstract class represents an interface of a graph."""
    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        ans ={}
        i=0
        for e in self.edges.items():
            if e[1] == id1:
                ans[i].update(e[1])
                i=i+1
        return ans



    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.edges.keys():
            return self.edges[id1]
        return {}


    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes.keys() and id2 in self.nodes.keys():
            self.edges[self.e_size()]=[{'src':id1,'w': weight, 'dest':id2}]
            self.mc += 1
            return True
        return False



    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        else:
            self.nodes[self.v_size()] = {Node(node_id, pos)}
            self.mc += 1
            return True

    def remove_node(self, node_id: int) -> bool:
        # if node_id in self.nodes:
        #     del self.nodes[node_id]
        #     for e in self.edges.items():
        #         if e[0]==node_id or e[1]==node_id:
        #             #self.edges.get(node_id).pop(e)
        #     self.mc += 1
        #     return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
       if node_id1 in self.nodes and node_id2 in self.nodes:
            for e in self.edges.items():
               if e[0]==node_id1:
                   if e[1]==node_id2:
                       del e
                       self.mc += 1
                       return True
       return False



       def getEdge(self, id1, id2):
           return self.edges[id1][id2]
