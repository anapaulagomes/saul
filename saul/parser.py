from saul.file_info_repository import FileInfoRepository
import re


def log(log_content):
    file_repository = FileInfoRepository()
    commits = log_content.split("\n\ncommit")

    for commit in commits:
        changed_files = changed_files_from(commit)
        for changed_file in changed_files:
            file_repository.add_or_update(changed_file, changed_files)
    return file_repository.files


def changed_files_from(commit_log):
    commit_log_lines = commit_log.split('\n')
    changed_files_log = _lines_with_changed_files(commit_log_lines)
    return [
        _extract_file_name(changed_file_log)
        for changed_file_log in changed_files_log
    ]


def _extract_file_name(changed_file_log):
    return re.split("\s|\t", changed_file_log)[-1]


def _lines_with_changed_files(commit_log_lines):
    return [line for line in commit_log_lines if line.lstrip().startswith(':')]
