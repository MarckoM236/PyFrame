class Response:

    def __init__(self, status_code, content_type, body):
        self.status_code = status_code
        self.content_type = content_type
        self.body = body

        
    def http_response(self):
        body_bytes = self.body.encode()

        return (
            f"HTTP/1.1 {self.status_code}\r\n"
            f"Content-Type: {self.content_type}\r\n"
            f"Content-Length: {len(body_bytes)}\r\n"
            "\r\n"
            f"{self.body}"
        )