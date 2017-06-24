import argparse


def get_arg_parser():
    arg_parser = argparse.ArgumentParser(prog='GetMyShow')
    arg_parser.add_argument("-n", "--name",
                            required=True,
                            action="store",
                            type=str,
                            help="Name of the show/movie you want to download.")
    arg_parser.add_argument("-t", "--tags",
                            required=False,
                            action="store",
                            type=str,
                            help="Search keywords in tags/name separated by comma.")
    arg_parser.add_argument("-s", "--size",
                            required=True,
                            action="store",
                            type=str,
                            help="Minimum size of the file. E.g. 800MB/1.2GB")
    return arg_parser


def main():
    returned_arg_parser = get_arg_parser()
    args, unknown_args = returned_arg_parser.parse_known_args()
    pass


if __name__ == '__main__':
    main()
