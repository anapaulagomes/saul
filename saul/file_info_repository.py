from saul.file_info import FileInfo


class FileInfoRepository(object):

    def __init__(self):
        self.files = {}

    def add_or_update(self, main_file, related_files):
        if main_file in self.files:
            self.files[main_file].add_change(related_files)
        else:
            self.files[main_file] = FileInfo(main_file, related_files)

    def find(self, file_name):
        return self.files[file_name]
