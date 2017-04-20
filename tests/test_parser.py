from saul import parser


def test_parse_single_commit_log_into_list_of_changed_files():
    commit_log = """a083cf6 Add gitconfig dotfile and task to update it
    .gitignore
    dotfiles/gitconfig
    jarvis-cli/jarvis.d/_config.dist
    jarvis-cli/jarvis.d/setup"""

    log_parser = parser.LogParser()

    changed_files = log_parser.commit(commit_log)

    assert 4 == len(changed_files)
    assert '.gitignore' == changed_files[0]
    assert 'dotfiles/gitconfig' == changed_files[1]
    assert 'jarvis-cli/jarvis.d/_config.dist' == changed_files[2]
    assert 'jarvis-cli/jarvis.d/setup' == changed_files[3]
