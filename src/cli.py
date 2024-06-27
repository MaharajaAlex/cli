import argparse
from commands import *

def main():
    parser = argparse.ArgumentParser(description='Command Line Interface for file management.')
    subparsers = parser.add_subparsers(dest='command')

    parser_list = subparsers.add_parser('list', help='List contents of a directory')
    parser_list.add_argument('path', type=str, help='Path to the directory')

    parser_cd = subparsers.add_parser('cd', help='Change directory')
    parser_cd.add_argument('path', type=str, help='Path to change the current directory to')

    args = parser.parse_args()

    if args.command == 'list':
        try:
            contents = list_directory(args.path)
            for item in contents:
                print(item)
        except Exception as e:
            print(f"Error: {e}")

    elif args.command == 'cd':
        try:
            cd(args.path)
            print(f"Changed directory to {args.path}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
