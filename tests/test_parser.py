from saul import parser as log_parser


def test_parse_single_commit_log_into_list_of_changed_files(commit_log):
    changed_files = log_parser.changed_files_from(commit_log)

    assert len(changed_files) == 4
    assert changed_files[0] == 'path/to/another/file/client.py'
    assert changed_files[1] == 'path/to/file/order.py'
    assert changed_files[2] == 'path/to/tests/test_client.py'
    assert changed_files[3] == 'path/to/tests/test_order.py'


def test_ignore_merge_commits(merge_commit_log):
    changed_files = log_parser.changed_files_from(merge_commit_log)

    assert len(changed_files) == 0


def test_parse_log_message_into_list_of_changed_files(sample_log):
    changed_files = log_parser.log(sample_log)

    assert len(changed_files) == 4
    assert changed_files['path/to/another/file/client.py'].changes == 2
    assert changed_files['path/to/file/order.py'].changes == 2
    assert changed_files['path/to/tests/test_client.py'].changes == 2
    assert changed_files['path/to/tests/test_order.py'].changes == 2


def test_parse_multi_line_log_message(multi_line_log):
    changed_files = log_parser.log(multi_line_log)

    assert len(changed_files) == 3
    assert changed_files['patroni/scripts/wale_restore.py'].changes == 1
    assert changed_files['requirements.txt'].changes == 1
    assert changed_files['tests/test_wale_restore.py'].changes == 1
