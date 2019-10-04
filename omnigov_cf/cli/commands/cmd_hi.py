import subprocess

import click


@click.command()
@click.argument('name', default='snakeeyes')
def cli(name):
    """
    Says hello to the user.

    :param name: The name of the user
    :return: Hello <name>
    """
    cmd = 'echo Hi {0}'.format(name)
    return subprocess.call(cmd, shell=True)
