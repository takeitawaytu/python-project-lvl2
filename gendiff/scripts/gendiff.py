#!/usr/bin/env python3
from gendiff.app import generate_diff
from gendiff.renders import FORMAT
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate differences')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        action='store',
                        dest='format',
                        metavar='FORMAT',
                        default='stylish',
                        help='set format of output: "stylish", "plain"',
                        type=FORMAT.get)
    args = parser.parse_args()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == '__main__':
    main()
