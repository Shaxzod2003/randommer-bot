class Randommer:
    def __init__(self) -> None:
        self.base_url = 'https://randommer.io/api/'

    def get_url(self) -> str:
        '''get url'''
        return self.base_url