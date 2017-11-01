from saul.file_info import FileInfo


def test_add_change_when_new_related_file_is_added():
    file_info = FileInfo('home/file_path', [])

    related_file = 'path/to/some_file.py'
    file_info.add_change([related_file])

    assert file_info.related_files.get(related_file)


def test_add_change_when_existent_related_file_is_added():
    file_info = FileInfo('home/file_path', ['path/to/some_file.py'])

    related_file = 'path/to/some_file.py'
    file_info.add_change([related_file])

    assert file_info.related_files.get(related_file) == 2


def test_count_changes_after_add_related_files():
    file_info = FileInfo('home/file_path', ['path/to/some_file.py'])

    related_file = 'path/to/some_file.py'
    file_info.add_change([related_file])

    assert file_info.changes == 2
