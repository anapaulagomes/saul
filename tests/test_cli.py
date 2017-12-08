from saul.cli import main
from click.testing import CliRunner
import sys


def test_receive_git_log_by_command_line():
    project_folder = sys.path[0]
    directory = project_folder + '/tests/fixtures/'

    runner = CliRunner()
    result = runner.invoke(main, [directory + 'saul.log'])

    assert result.exit_code == 0


def test_returns_error_if_a_file_does_not_exists():
    runner = CliRunner()
    result = runner.invoke(main, ['i-dont-exist'])

    assert result.exit_code == 2
