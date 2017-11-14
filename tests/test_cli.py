from saul.cli import main
from click.testing import CliRunner


def test_receive_git_log_by_command_line():
    runner = CliRunner()
    result = runner.invoke(main, ['saul.log'])

    assert result.exit_code == 0


def test_when_the_user_does_not_inform_a_file_assume_one_as_default():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.exit_code == 0


def test_returns_error_if_a_file_does_not_exists():
    runner = CliRunner()
    result = runner.invoke(main, ['i-dont-exist'])

    assert result.exit_code == 2
