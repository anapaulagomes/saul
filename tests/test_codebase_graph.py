import mock
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

    assert set(codebase.files()) == set(['path/to/file.py', 'path/to/another_file.py', 'path/to/some_file.py'])


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
    all_edges = codebase.related_files()

    assert find_edge(all_edges, ('path/to/file.py', 'path/to/another_file.py'))
    assert find_edge(all_edges, ('path/to/file.py', 'path/to/some_file.py'))
    assert find_edge(all_edges, ('path/to/another_file.py', 'path/to/some_file.py'))


def test_node_should_know_how_many_times_the_file_was_modified():
    repository = FileInfoRepository()
    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    repository.add_or_update(a_file, related_files)

    more_related_files = ['path/to/yet_another_file']
    repository.add_or_update(a_file, more_related_files)

    codebase = CodeBaseGraph(repository)
    codebase.make_graph()

    all_nodes = codebase.files(data=True)
    node = find_node(all_nodes, a_file)

    assert node[1]['changes'] == 2


def test_edge_should_know_how_many_times_the_files_were_modified_together():
    repository = FileInfoRepository()

    repository.add_or_update('path/to/file.py', ['path/to/another_file.py', 'path/to/some_file.py'])
    repository.add_or_update('path/to/another_file.py', ['path/to/file.py', 'path/to/some_file.py'])

    codebase = CodeBaseGraph(repository)
    codebase.make_graph()
    all_edges = codebase.related_files(data=True)

    edge_file_another_file = find_edge(all_edges, ('path/to/file.py', 'path/to/another_file.py'))
    edge_file_some_file = find_edge(all_edges, ('path/to/file.py', 'path/to/some_file.py'))
    edge_another_file_some_file = find_edge(all_edges, ('path/to/another_file.py', 'path/to/some_file.py'))
    import pdb; pdb.set_trace()
    
    assert edge_file_another_file[2]['changes'] == 2
    assert edge_file_some_file[2]['changes'] == 1


@mock.patch('saul.codebasegraph.nx.write_gml')
def test_should_generate_gml_file_to_codebase_graph(mock_write_gml):
    repository = FileInfoRepository()
    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    repository.add_or_update(a_file, related_files)

    more_related_files = ['path/to/yet_another_file']
    repository.add_or_update(a_file, more_related_files)

    codebase = CodeBaseGraph(repository)
    codebase.make_graph()
    codebase.export()

    assert mock_write_gml.called


#added to keep compatibility with py2 and py3 (since the dict order are different in different versions)
def find_edge(all_edges, wanted_edge):
    for edge in all_edges:
        if edge[0] == wanted_edge[0] or edge[0] == wanted_edge[1] and edge[1] == wanted_edge[0] or edge[1] == wanted_edge[1]:
            return edge
    return None

def find_node(all_nodes, wanted_node):
    for node, data in all_nodes:
        if node == wanted_node:
            return (node, data)
    return None
