from saul import parser
from tests import log_fixtures

def test_parse_single_commit_log_into_list_of_changed_files():
    log_parser = parser.LogParser()

    changed_files = log_parser.commit(log_fixtures.COMMIT_LOG)

    assert 4 == len(changed_files)
    assert 'path/to/another/file/client.py' == changed_files[0]
    assert 'path/to/file/order.py' == changed_files[1]
    assert 'path/to/tests/test_client.py' == changed_files[2]
    assert 'path/to/tests/test_order.py' == changed_files[3]

def test_ignore_merge_commits():
    log_parser = parser.LogParser()

    changed_files = log_parser.commit(log_fixtures.MERGE_COMMIT_LOG)

    assert 0 == len(changed_files)
