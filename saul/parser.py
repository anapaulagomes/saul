class LogParser(object):

    def commit(self, commit_log):
        changed_files_log = self.__extract_changed_files_log(commit_log.split('\n'))
        return [self.__extract_file_name(changed_file_log) for changed_file_log in changed_files_log]

    def __extract_file_name(self, changed_file_log):
        return changed_file_log.split(' ')[-1]

    def __extract_changed_files_log(self, commit_log_lines):
        if (commit_log_lines[1].startswith('Merge:')): return []
        return commit_log_lines[6:]
