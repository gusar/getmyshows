from getmyshows.apis import all_api_helper
from getmyshows.apis import rarbg_api_helper

API_NAME_TO_HELPER_MAP = {
    'rarbg': rarbg_api_helper.RarbgAPIHelper,
    'all': all_api_helper.AllAPIHelper
}

categories = ['movie', 'show']
