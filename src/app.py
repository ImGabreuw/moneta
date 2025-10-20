from wsgiref.simple_server import make_server

from falcon import Request, Response, App, HTTP_200, HTTP_201


class TestResource:

    def on_get(self, req: Request, resp: Response):
        resp.media = {"message": "GET request received"}
        resp.status = HTTP_200
        
    def on_post(self, req: Request, resp: Response):
        data = req.media
        
        resp.media = {"message": "POST request received", "data": data}
        resp.status = HTTP_201

app = App()

test_resource = TestResource()
app.add_route('/test', test_resource)

if __name__ == '__main__':
    with make_server("", 8080, app) as httpd:
        print(f"Serving on port {httpd.server_port}...")
        httpd.serve_forever()
