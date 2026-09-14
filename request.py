from urllib.parse import parse_qs

class Request:
    def __init__(self, environ):
        self.environ = environ
        self.path = environ.get("PATH_INFO", "/")
        self.method = environ.get("REQUEST_METHOD", "GET").upper()
        raw_query = environ.get("QUERY_STRING", "")
        self.query_params = parse_qs(raw_query)

    def get_param(self, key, default=None):
        values = self.query_params.get(key)
        return values[0] if values else default