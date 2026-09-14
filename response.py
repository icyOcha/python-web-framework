import json

class Response:
    def __init__(self, body="", status="200 OK", content_type="text/html; charset=utf-8"):
        self.status = status
        self.headers = [("Content-Type", content_type)]  # Fixed casing: Content-Type

        if isinstance(body, (dict, list)):
            self.body = json.dumps(body).encode("utf-8")
            self.headers = [("Content-Type", "application/json")]
        elif isinstance(body, str):
            self.body = body.encode("utf-8")
        elif isinstance(body, bytes):
            self.body = body
        else:
            self.body = str(body).encode("utf-8")