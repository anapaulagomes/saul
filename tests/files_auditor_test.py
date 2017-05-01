from saul.files_auditor import *

def test_create_file_with_change_and_related_files():
    auditor = FilesAuditor()

    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    auditor.update_file(a_file, related_files)

    assert 1 == auditor.file_info(a_file).changes
    assert 2 == len(auditor.file_info(a_file).related_files)

def test_add_related_files_to_existing_file():
    auditor = FilesAuditor()

    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    auditor.update_file(a_file, related_files)

    more_related_files = ['path/to/yet_another_file']
    auditor.update_file(a_file, more_related_files)


    assert 2 == auditor.file_info(a_file).changes
    assert 3 == len(auditor.file_info(a_file).related_files)

def test_increase_changes_when_file_is_already_related():
    auditor = FilesAuditor()

    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    auditor.update_file(a_file, related_files)

    more_related_files = ['path/to/some_file.py']
    auditor.update_file(a_file, more_related_files)


    assert 2 == auditor.file_info(a_file).changes
    assert 2 == len(auditor.file_info(a_file).related_files)
    assert 2 == auditor.file_info(a_file).related_files['path/to/some_file.py']
