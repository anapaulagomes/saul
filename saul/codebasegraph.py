import networkx as nx


class CodeBaseGraph(object):

    def __init__(self, repository):
        self.repository = repository

    def make_graph(self):
        self.graph = nx.Graph()
        self.__add_nodes()
        self.__add_edges()

        return self.graph

    def files(self, data=False):
        return self.graph.nodes(data=True if data else False)

    def related_files(self):
        return self.graph.edges()

    def export(self):
        return nx.write_gml(self.graph, 'codebasegraph.gml')

    def __add_nodes(self):
        for a_file, a_file_info in self.repository.files.items():
            self.graph.add_node(a_file, changes=a_file_info.changes)

    def __add_edges(self):
        for a_file, a_file_info in self.repository.files.items():
            for related_files in a_file_info.related_files.keys():
                self.graph.add_edge(a_file, related_files)
