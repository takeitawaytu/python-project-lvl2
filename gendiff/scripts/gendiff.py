#!/usr/bin/env python3
from gendiff import generate_diff
from gendiff.cli import get_parser


def main():
    args = get_parser()
    result = generate_diff(args.first_file, args.second_file, args.format)
    print(result)


if __name__ == '__main__':
    main()
