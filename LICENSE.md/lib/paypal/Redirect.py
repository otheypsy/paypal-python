class Redirect:

    def __init__(self):
        self.__return_url = ''
        self.__cancel_url = ''

    def set_return_url(self, url):
        self.__return_url = url

    def set_cancel_url(self, url):
        self.__cancel_url = url

    def create_array(self):
        return {
            "return_url": self.__return_url,
            "cancel_url": self.__cancel_url
        }