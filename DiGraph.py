from src import GraphInterface
import Node

class DiGraph(GraphInterface):

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = {(e['src'], e['dest']): e['w'] for e in edges}
        self.mc = 0

    """This abstract class represents an interface of a graph."""
    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return len(self.edges)

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.inverse.keys():
            return self.inverse[id1]
        return {}

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.edges.keys():
            return self.edges[id1]
        return {}


    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 in self.nodes.keys() and id2 in self.nodes.keys():
            if self.getEdge(id1, id2):
                return False
            self.edges[id1][id2] = weight
            self.mc += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        else:
            self.nodes[node_id] = Node(node_id,pos)
            self.mc += 1
            return True


    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes:
            del self.nodes[node_id]
            for e in self.edges[node_id]:
                if(e[1])
            self.mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
       if node_id1 in self.nodes.keys() and node_id2 in self.nodes.keys():
           if self.edges[node_id1, node_id2]:
               del self.edges[node_id1, node_id2]
               self.mc += 1
               return True
       return False
