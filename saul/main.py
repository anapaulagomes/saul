from saul.parser import LogParser
import argparse


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-f', '--file', dest='log_file', default='saul.log', help='File from git log')

captured_args = argument_parser.parse_args()

parser = LogParser()
try:
    repository_files = parser.log(open(captured_args.log_file).read())
    for _, file_info in repository_files.items():
        print(file_info)
except FileNotFoundError:
    print("Could not find {}! Use 'git log --raw --no-merges > {}' to generate a log file.".format(captured_args.log_file, captured_args.log_file))

