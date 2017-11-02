from saul.file_info_repository import FileInfoRepository


def test_create_file_with_change_and_related_files():
    repository = FileInfoRepository()

    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    repository.add_or_update(a_file, related_files)

    assert repository.find(a_file).changes == 1
    assert len(repository.find(a_file).related_files) == 2


def test_add_related_files_to_existing_file():
    repository = FileInfoRepository()

    a_file = 'path/to/file.py'
    related_files = ['path/to/another_file.py', 'path/to/some_file.py']
    repository.add_or_update(a_file, related_files)

    more_related_files = ['path/to/yet_another_file']
    repository.add_or_update(a_file, more_related_files)

    assert repository.find(a_file).changes == 2
    assert len(repository.find(a_file).related_files) == 3


def test_increase_changes_when_file_is_already_related():
    repository = FileInfoRepository()

    a_file = 'path/to/file.py'
    related_file = 'path/to/some_file.py'
    related_files = ['path/to/another_file.py', related_file]
    repository.add_or_update(a_file, related_files)

    more_related_files = [related_file]
    repository.add_or_update(a_file, more_related_files)

    assert repository.find(a_file).changes == 2
    assert len(repository.find(a_file).related_files) == 2
    assert repository.find(a_file).related_files[related_file] == 2
