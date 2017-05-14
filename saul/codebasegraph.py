import networkx as nx


class CodeBaseGraph(object):

    def __init__(self, repository):
        self.repository = repository

    def graph(self):
        return nx.Graph()
