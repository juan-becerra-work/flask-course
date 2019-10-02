import subprocess

import click


@click.command()
@click.option('--name/--noname', default=True,
              help='You have a name, right?')

@click.argument('username')
def cli(username):
    """
    Says hello to the user.

    :param name: The name of the user
    :return: Hello <name>
    """
    cmd = 'echo Hello {0}'.format(username)
    return subprocess.call(cmd, shell=True)
