from saul import parser
from tests.fixtures import log_fixtures

log_parser = parser.LogParser()

def test_parse_single_commit_log_into_list_of_changed_files():
    changed_files = log_parser.commit(log_fixtures.COMMIT_LOG)

    assert len(changed_files) == 4
    assert changed_files[0] == 'path/to/another/file/client.py'
    assert changed_files[1] == 'path/to/file/order.py'
    assert changed_files[2] == 'path/to/tests/test_client.py'
    assert changed_files[3] == 'path/to/tests/test_order.py'

def test_ignore_merge_commits():
    changed_files = log_parser.commit(log_fixtures.MERGE_COMMIT_LOG)

    assert len(changed_files) == 0

def test_parse_log_message_into_list_of_changed_files():
    changed_files = log_parser.log(log_fixtures.SAMPLE_LOG)

    assert len(changed_files) == 4
    assert changed_files['path/to/another/file/client.py'].changes == 2
    assert changed_files['path/to/file/order.py'].changes == 2
    assert changed_files['path/to/tests/test_client.py'].changes == 2
    assert changed_files['path/to/tests/test_order.py'].changes == 2
