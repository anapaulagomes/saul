from saul import parser
import click


@click.command()
@click.argument('log', nargs=1, type=click.Path(exists=True), default='saul.log')
def main(log):
    click.echo('========== Better Call Saul ==========')

    click.echo('\nLoading log...')
    repository_files = parser.log(open(log).read())

    for _, file_info in repository_files.items():
        print(file_info)
