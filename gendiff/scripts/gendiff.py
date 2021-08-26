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
                        default='jsontxt',
                        help='set format of output: "jsontxt", "plain"',
                        type=FORMAT.get)
    args = parser.parse_args()
    result = generate_diff(args.format, args.first_file, args.second_file)
    print(result)


if __name__ == '__main__':
    main()
