from getmyshows.request_manager import RequestManager
from getmyshows.user_input import parse_user_input


def run_program():
    user_input = parse_user_input()
    request_manager = RequestManager(user_input)
