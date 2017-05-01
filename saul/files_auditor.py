class FilesAuditor(object):

    def __init__(self):
        self.files = {}

    def update_file(self, main_file, related_files):
        if main_file in self.files:
            self.files[main_file].add_change(related_files)
        else:
            self.files[main_file] = FileInfo(main_file, related_files)

    def file_info(self, file_name):
        return self.files[file_name]


class FileInfo(object):

    def __init__(self, file_path, related_files):
        self.file_path = file_path
        self.changes = 1
        self.related_files = {}
        for related_file in related_files:
            self.related_files[related_file] = 1

    def add_change(self, related_files):
        self.changes += 1
        for related_file in related_files:
            if related_file in self.related_files:
                self.related_files[related_file] += 1
            else:
                self.related_files[related_file] = 1
