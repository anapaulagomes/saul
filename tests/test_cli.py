from saul.cli import main
from click.testing import CliRunner
import os


def test_receive_git_log_by_command_line():
    log = [os.getcwd() + '/tests/fixtures/saul.log']

    runner = CliRunner()
    result = runner.invoke(main, log)

    assert result.exit_code == 0


def test_returns_error_if_a_file_does_not_exists():
    runner = CliRunner()
    result = runner.invoke(main, ['i-dont-exist'])

    assert result.exit_code == 2
