class FailedPostException(Exception):
    def __init__(self):
        super().__init__("No se ha podido crear el Post")