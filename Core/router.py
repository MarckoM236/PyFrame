import routes
from Core.response import Response

class Router:
    def __init__(self,path,method,environment,params):
        self.path = path
        self.method = method
        self.environment = environment
        self.params = params

    def dispatch(self):
        if routes.routes.get(self.path) and routes.routes[self.path]["method"] == self.method:
            controller_class = routes.routes[self.path]["class"]
            controller_function = routes.routes[self.path]["function"]
            
            try:
                controller = controller_class()
                
                if not hasattr(controller, controller_function):
                    response = Response("500 Internal Server Error", "text/plain", "Method not found in controller").http_response()
                else:
                    action = getattr(controller, controller_function)
                    body,response_type = action(self.params)

                    res_type = response_type if response_type else "text/plain"
                    response = Response("200 OK", res_type, body).http_response()
            except Exception as e:
                if self.environment == "development":
                    response = Response("500 Internal Server Error", "text/plain", f"Error: {str(e)}").http_response()
                else:
                    response = Response("500 Internal Server Error", "text/plain", "Internal Server Error").http_response()
    
        else:
            response = Response("404 Not Found", "text/plain", "404 Not Found").http_response()

        return response