from saul.parser import LogParser


diretory = 'saul.log'

parser = LogParser()
repository_files = parser.log(open(diretory).read())

for _, file_info in repository_files.items():
    print(file_info)
