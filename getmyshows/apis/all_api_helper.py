from getmyshows.apis.base_api_helper import BaseAPIHelper


class AllAPIHelper(BaseAPIHelper):

    def build_search_url(self):
        raise NotImplementedError

    @property
    def url_base(self):
        raise NotImplementedError
