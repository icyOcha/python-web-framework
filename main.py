from wsgiref.simple_server import make_server
from framework import Framework
from response import Response
if __name__ == "__main__":
    app = Framework()

    @app.route("/", method="GET")
    def home_page():
        return Response("<h1> Home Page </h1>")

    # dynamic route testing
    @app.route("/users/<id>", method="GET")
    def user_profile(id: str):
        return Response({"user_id": id, "status": "active"})

    @app.route("/about", method="POST")
    def create_about():
        return Response({"message": "POST request received for /about"})
    
    print("Server running on http://localhost:8000")
    server = make_server("localhost", 8000, app)
    server.serve_forever()