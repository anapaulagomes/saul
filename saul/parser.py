from saul.file_info_repository import FileInfoRepository

class LogParser(object):

    def __init__(self):
        self.file_repository = FileInfoRepository()

    def log(self, log_content):
        commits = log_content.split("\n\ncommit")
        for commit in commits:
            changed_files = self.commit(commit)
            for changed_file in changed_files:
                self.file_repository.add_or_update(changed_file, changed_files)
        return self.file_repository.files

    def commit(self, commit_log):
        commit_log_lines = commit_log.split('\n')
        changed_files_log = self.__extract_changed_files_log(commit_log_lines)
        return [self.__extract_file_name(changed_file_log) for changed_file_log in changed_files_log]

    def __extract_file_name(self, changed_file_log):
        return changed_file_log.split(' ')[-1]

    def __extract_changed_files_log(self, commit_log_lines):
        return [] if commit_log_lines[1].startswith('Merge:') else commit_log_lines[6:]

    def __map_changes_per_files(self, changed_files_per_commit):
        for changed_files in changed_files_per_commit:
            for changed_file in changed_files:
                self.file_repository.add_or_update(changed_file, changed_files)
