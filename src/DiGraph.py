from src import GraphInterface
import Node

class DiGraph(GraphInterface):

    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = {(e['src'], e['dest']): e['w'] for e in edges}
        self.mc=0

    """This abstract class represents an interface of a graph."""
    def v_size(self) -> int:
        return len(self.nodes)
        #return size(self.nodes['id'])

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
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        raise NotImplementedError

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        raise NotImplementedError
