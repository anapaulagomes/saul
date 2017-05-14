import networkx as nx


class CodeBaseGraph(object):

    def __init__(self, repository):
        self.repository = repository

    def make_graph(self):
        self.graph = nx.Graph()

        for a_file in self.repository.files:
            self.graph.add_node(a_file)

        return self.graph

    def nodes(self):
        return self.graph.nodes()
