from saul.file_info_repository import *
from saul.codebasegraph import CodeBaseGraph
import networkx


def test_create_codebase_graph_based_on_file_info_repository():
    repository = FileInfoRepository()
    codebase = CodeBaseGraph(repository)

    assert isinstance(codebase.make_graph(), networkx.classes.graph.Graph)


def test_create_codebase_graph_with_files_as_nodes():
    repository = FileInfoRepository()
    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    repository.add_or_update(a_file, related_files)

    codebase = CodeBaseGraph(repository)
    codebase.make_graph()

    assert set(codebase.nodes()) == set(['path/to/file.py', 'path/to/another_file.py', 'path/to/some_file.py'])


def test_create_codebase_graph_with_related_files_as_edges():
    repository = FileInfoRepository()
    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    repository.add_or_update(a_file, related_files)

    another_file = 'path/to/another_file.py'
    related_files = ['path/to/file.py', 'path/to/some_file.py']
    repository.add_or_update(another_file, related_files)

    some_file = 'path/to/some_file.py'
    related_files = ['path/to/another_file.py', 'path/to/file.py']
    repository.add_or_update(some_file, related_files)

    codebase = CodeBaseGraph(repository)
    codebase.make_graph()
    all_edges = codebase.edges()
    
    assert find_edge(all_edges, ('path/to/file.py', 'path/to/another_file.py'))
    assert find_edge(all_edges, ('path/to/file.py', 'path/to/some_file.py'))
    assert find_edge(all_edges, ('path/to/another_file.py', 'path/to/some_file.py'))


def find_edge(all_edges, wanted_edge):
    for edge in all_edges:
        if edge[0] == wanted_edge[0] or edge[0] == wanted_edge[1] and edge[1] == wanted_edge[0] or edge[1] == wanted_edge[1]:
            return True
    return False
