class LogParser(object):

    def commit(self, commit_log):
        return [changed_file.strip() for changed_file in commit_log.split('\n')[1:]]
