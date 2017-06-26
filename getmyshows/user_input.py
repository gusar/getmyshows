import argparse

import humanfriendly

from getmyshows import option_maps


def parse_user_input():
    returned_arg_parser = get_arg_parser()
    args, unknown_args = returned_arg_parser.parse_known_args()

    parsed_size_integer_bytes = parse_filesize_arg(args.filesize)
    tags_list = split_tags_to_list(args.tags)
    search_name = args.name
    search_category = args.category
    search_indexer = args.indexer

    return {
        'name': search_name,
        'tags': tags_list,
        'category': search_category,
        'size': parsed_size_integer_bytes,
        'indexer': search_indexer
    }


def parse_filesize_arg(filesize_string):
    return humanfriendly.parse_size(filesize_string, binary=True)


def split_tags_to_list(tags_string):
    return tags_string.split(',')


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

    arg_parser.add_argument("-c", "--category",
                            choices=option_maps.categories,
                            required=True,
                            action="store",
                            type=str,
                            help="Category: movie/show")

    arg_parser.add_argument("-i", "--indexer",
                            choices=option_maps.API_NAME_TO_HELPER_MAP,
                            required=False,
                            default='all',
                            action='store',
                            type=str,
                            help='Indexer: rarbg')
    return arg_parser


if __name__ == '__main__':
    parse_user_input()
