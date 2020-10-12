# Standard library imports.

# Related third party imports.
import click

# Local application/library specific imports.
from todo_template.render_template import TodoTemplate

@click.group()
def cli():
    """
    A Command line tool for uploading weekly todo lists to hackmd.io
    """
    pass

@cli.command()
def today():
    todo = TodoTemplate()
    todo.render_today_template()

if __name__ == "__main__":
    cli()
