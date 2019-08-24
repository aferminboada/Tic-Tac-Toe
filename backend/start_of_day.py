import argparse
from backend import (
    welcome_message,
    Play,
    options
)


def could_be_yes(inp):
    inp = inp.lower()
    return (
        inp in ('yes', 'true', 'si') or
        inp[0] in ('y', '1', 's', 't')
    )


if __name__ == '__main__':
    print(welcome_message)
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', help='DEBUG MODE', default='False')
    parser.add_argument('--player', help='CUSTOM PLAYER NAME', default='Player 1')
    args = parser.parse_args()
    options['debug'] = could_be_yes(args.debug)
    options['player'] = args.player
    Play(options)
