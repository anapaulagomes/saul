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

    another_file = 'path/to/another_file.py'
    related_files = ['path/to/file.py', 'path/to/some_file.py']
    repository.add_or_update(another_file, related_files)

    codebase = CodeBaseGraph(repository)
    codebase.make_graph()

    assert codebase.nodes() == ['path/to/file.py', 'path/to/another_file.py']
