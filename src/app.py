from wsgiref.simple_server import make_server

import falcon
from falcon import Request, Response, App


class TestResource:

    def on_get(self, req: Request, resp: Response):
        resp.media = {"message": "GET request received"}
        resp.status = falcon.HTTP_200

app = App()

test_resource = TestResource()
app.add_route('/test', test_resource)

if __name__ == '__main__':
    with make_server("", 8080, app) as httpd:
        print(f"Serving on port {httpd.server_port}...")
        httpd.serve_forever()
