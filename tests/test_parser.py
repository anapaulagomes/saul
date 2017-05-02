from saul import parser
from tests.fixtures import log_fixtures

log_parser = parser.LogParser()

def test_parse_single_commit_log_into_list_of_changed_files():
    changed_files = log_parser.commit(log_fixtures.COMMIT_LOG)

    assert 4 == len(changed_files)
    assert 'path/to/another/file/client.py' == changed_files[0]
    assert 'path/to/file/order.py' == changed_files[1]
    assert 'path/to/tests/test_client.py' == changed_files[2]
    assert 'path/to/tests/test_order.py' == changed_files[3]

def test_ignore_merge_commits():
    changed_files = log_parser.commit(log_fixtures.MERGE_COMMIT_LOG)

    assert 0 == len(changed_files)

def test_parse_log_message_into_list_of_changed_files():
    changed_files = log_parser.log(log_fixtures.SAMPLE_LOG)

    assert 4 == len(changed_files)
    assert 2 == changed_files['path/to/another/file/client.py'].changes
    assert 2 == changed_files['path/to/file/order.py'].changes
    assert 2 == changed_files['path/to/tests/test_client.py'].changes
    assert 2 == changed_files['path/to/tests/test_order.py'].changes
