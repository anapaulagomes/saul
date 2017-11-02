import mock
from saul.file_info_repository import FileInfoRepository
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

    expected_files = [
        'path/to/file.py', 'path/to/another_file.py', 'path/to/some_file.py'
    ]
    assert set(codebase.files()) == set(expected_files)


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
    assert find_edge(all_edges,
                     ('path/to/another_file.py', 'path/to/some_file.py'))


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


# added to keep compatibility with py2 and py3 (since the dict order are different in different versions)
def find_edge(all_edges, wanted_edge):
    for edge in all_edges:
        found_node_one = edge[0] == wanted_edge[0] or edge[0] == wanted_edge[1]
        found_node_two = edge[1] == wanted_edge[0] or edge[1] == wanted_edge[1]
        if found_node_one and found_node_two:
            return True
    return False


def find_node(all_nodes, wanted_node):
    for node, data in all_nodes:
        if node == wanted_node:
            return (node, data)
    return None
