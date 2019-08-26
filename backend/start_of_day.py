import argparse
from backend import (
    welcome_message,
    Play,
    options
)


if __name__ == '__main__':
    print(welcome_message)
    parser = argparse.ArgumentParser()
    parser.add_argument('--player', help='CUSTOM PLAYER NAME', default='Player 1')
    args = parser.parse_args()
    options['player'] = args.player
    Play().do_start(**options)
