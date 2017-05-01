from saul.file_info_repository import *

def test_create_file_with_change_and_related_files():
    auditor = FileInfoRepository()

    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    auditor.add_or_update(a_file, related_files)

    assert 1 == auditor.find(a_file).changes
    assert 2 == len(auditor.find(a_file).related_files)

def test_add_related_files_to_existing_file():
    auditor = FileInfoRepository()

    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    auditor.add_or_update(a_file, related_files)

    more_related_files = ['path/to/yet_another_file']
    auditor.add_or_update(a_file, more_related_files)


    assert 2 == auditor.find(a_file).changes
    assert 3 == len(auditor.find(a_file).related_files)

def test_increase_changes_when_file_is_already_related():
    auditor = FileInfoRepository()

    a_file = 'path/to/file.py'
    related_file = 'path/to/some_file.py'
    related_files = ['path/to/another_file.py',related_file]
    auditor.add_or_update(a_file, related_files)

    more_related_files = [related_file]
    auditor.add_or_update(a_file, more_related_files)


    assert 2 == auditor.find(a_file).changes
    assert 2 == len(auditor.find(a_file).related_files)
    assert 2 == auditor.find(a_file).related_files[related_file]
