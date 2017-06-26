class BaseAPIHelper(object):

    def __init__(self, user_params):
        self._user_params = user_params

    def build_search_url(self):
        raise NotImplementedError

    @property
    def url_base(self):
        raise NotImplementedError
