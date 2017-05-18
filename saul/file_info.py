class FileInfo(object):

    def __init__(self, file_path, related_files):
        self.file_path = file_path
        self.changes = 1
        self.related_files = {}
        for related_file in related_files:
            self.related_files[related_file] = 1

    def __str__(self):
        return 'File Path: {} Changes: {} Related Files: {}'.format(self.file_path, self.changes, self.related_files)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def add_change(self, related_files):
        self.changes += 1
        for related_file in related_files:
            if related_file in self.related_files:
                self.related_files[related_file] += 1
            else:
                self.related_files[related_file] = 1
