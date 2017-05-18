import networkx as nx


class CodeBaseGraph(object):

    def __init__(self, repository):
        self.repository = repository

    def make_graph(self):
        self.graph = nx.Graph()
        self.__add_nodes()
        self.__add_edges()

        return self.graph

    def files(self):
        return self.graph.nodes()

    def related_files(self):
        return self.graph.edges()

    def __add_nodes(self):
        for a_file, a_file_info in self.repository.files.items():
            self.graph.add_node(a_file, fileinfo=a_file_info)

    def __add_edges(self):
        for a_file, a_file_info in self.repository.files.items():
            for related_files in a_file_info.related_files.keys():
                self.graph.add_edge(a_file, related_files)
