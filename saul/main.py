from saul.parser import LogParser
import argparse


diretory = 'saul.log'
argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-f', '--file', dest='log_file', default='saul.log', help='File from git log')

captured_args = argument_parser.parse_args()


parser = LogParser()
repository_files = parser.log(open(captured_args.log_file).read())

for _, file_info in repository_files.items():
    print(file_info)
