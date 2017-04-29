class LogParser(object):

    def log(self, log):
        commits = log.split("\n\ncommit")
        changed_files_per_commit = [self.commit(commit) for commit in commits]
        return self.__map_changes_per_files(changed_files_per_commit)

    def commit(self, commit_log):
        commit_log_lines = commit_log.split('\n')
        changed_files_log = self.__extract_changed_files_log(commit_log_lines)
        return [self.__extract_file_name(changed_file_log) for changed_file_log in changed_files_log]

    def __extract_file_name(self, changed_file_log):
        return changed_file_log.split(' ')[-1]

    def __extract_changed_files_log(self, commit_log_lines):
        return [] if commit_log_lines[1].startswith('Merge:') else commit_log_lines[6:]

    def __map_changes_per_files(self, changed_files_per_commit):
        changes_per_file = {}
        for changed_files in changed_files_per_commit:
            for changed_file in changed_files:
                if changed_file in changes_per_file:
                    changes_per_file[changed_file] += 1
                else:
                    changes_per_file[changed_file] = 1
        return changes_per_file
