from getmyshows import option_maps


class RequestManager(object):

    def __init__(self, user_params_dict):
        self.user_params = user_params_dict
        self._api_helper = None

    @property
    def api_helper(self):
        if self._api_helper is None:
            self._api_helper = option_maps.API_NAME_TO_HELPER_MAP[self.user_params['indexer']](self.user_params)
        return self._api_helper

    def build_search_request(self):
        self.api_helper.build_search_url()
