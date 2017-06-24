import argparse

import humanfriendly


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
    arg_parser.add_argument("-s", "--filesize",
                            required=True,
                            action="store",
                            type=str,
                            help="Minimum size of the file. E.g. 800MB/1.2GB")
    return arg_parser


def parse_filesize_arg(filesize_string):
    return humanfriendly.parse_size(filesize_string, binary=True)


def split_tags_to_list(tags_string):
    return tags_string.split(',')


def main():
    returned_arg_parser = get_arg_parser()
    args, unknown_args = returned_arg_parser.parse_known_args()

    parsed_size_integer_bytes = parse_filesize_arg(args.filesize)

    tags_list = split_tags_to_list(args.tags)
    pass


if __name__ == '__main__':
    main()
