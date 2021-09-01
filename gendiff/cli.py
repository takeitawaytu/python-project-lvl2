import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='Generate differences')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        action='store',
                        dest='format',
                        metavar='FORMAT',
                        default='stylish',
                        help='set format of output: "stylish", "plain"',
                        choices=['plain', 'json', 'stylish'],
                        type=str)
    return parser.parse_args()
