import re
from request import Request
from response import Response

class Framework:
    def __init__(self):
            self.routes = []

    def __call__(self, environ, start_response):
        req = Request(environ=environ)

        # Delegate business logic execution
        res = self.handle_req(req)

        start_response(res.status, res.headers)
        return [res.body]

    def handle_req(self, req: Request) -> Response:
        for route_method, pattern, handler in self.routes:
             if route_method == req.method:
                match = pattern.match(req.path)
                if match:
                     # extract url parameter as kwargs : {'id': '42'}
                    kwargs = match.groupdict()
                    return handler(**kwargs)
        return Response("<h1>404 Not Found</h1>", status="404 Not Found") 
              
    def route(self, path, method="GET"):
         def decorator(func):
            self.routes.append((method.upper(), Framework.compile_route_path(path), func))
            return func
         return decorator

    @staticmethod
    def compile_route_path(path_pattern: str) -> re.Pattern:
        # FIX 2: Added missing '>' to match whole bracketed parameter
        regex_pattern = re.sub(r"<([^>]+)>", r"(?P<\1>[^/]+)", path_pattern)
        full_regex = f"^{regex_pattern}$"
        return re.compile(full_regex)
    

    
        

    
         
         

    