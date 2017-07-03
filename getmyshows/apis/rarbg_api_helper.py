from urllib.parse import urlencode, urljoin

from getmyshows.apis.base_api_helper import BaseAPIHelper


class RarbgAPIHelper(BaseAPIHelper):

    def __init__(self, user_params):
        super().__init__(user_params)
        self._user_params = user_params

    def build_search_url(self):
        # TODO: fix url building ("torrents.php?" missing)
        search_url = urljoin(self.url_base, self.url_params)
        print(1)
        return

    @property
    def url_base(self):
        return 'https://rarbg.to/torrents.php'

    @property
    def url_params(self):
        categories = urlencode(self._get_category_tuples())
        search = urlencode(self._get_search_tuple())
        return urljoin(search, categories)

    def _get_search_tuple(self):
        return [('search', self._user_params['name'].split(' '))]

    def _get_category_tuples(self):
        return [('category[]', cat_number)
                for cat_number
                in self._category_map[self._user_params['category']]]

    @property
    def _category_map(self):
        return {
            'movie': ['18', '41', '49'],
            'show': ['27', '28', '40', '32']
        }
