from saul.file_info_repository import *
from saul.codebasegraph import CodeBaseGraph
import networkx


def test_create_codebase_graph_based_on_file_info_repository():
    repository = FileInfoRepository()
    codebase = CodeBaseGraph(repository)

    assert isinstance(codebase.graph(), networkx.classes.graph.Graph)
