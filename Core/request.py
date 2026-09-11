import routes

class Request:

    def __init__(self, request):
        self.request = request

        self.method = None
        self.path = None
        self.route = None
        self.routes_params = {}
        self.query_params = {}


    def parse(self):
        if not self.request:
            return None 
        
        lines = self.request.split('\r\n')
        
        if not lines:
            return None
        
        http = lines[0]
        
        parts_http = http.split(' ')
        
        if len(parts_http) < 2:
            return None

        self.method = parts_http[0]
        self.path = self.get_only_path(parts_http[1])
        self.route = self.find_route(self.path,self.method,routes.routes)
        self.query_params = self.get_query_params(parts_http[1])
        self.route_params = self.get_route_params(self.path,self.method,routes.routes)

    def get_only_path(self,path):
        parts = path.split('?')
        return parts[0]
    
    def get_query_params(self,path):
        params = {}
        first_split = path.split('?')

        if len(first_split) > 1:
            params_split = first_split[1].split('&')
            for var in params_split:
                var_split = var.split('=')

                if len(var_split) != 2:
                    continue

                key=var_split[0]
                value=var_split[1]

                params[key]=value

        return params

    def get_route_params(self,path,method,routes):
        params = {}
        
        route = self.find_route(path,method,routes)

        if not route:
            return {}
        
        path_parts = path.strip('/').split('/')
        route_parts = route.strip('/').split('/')

        for route_part, path_part in zip(route_parts, path_parts):

            # params
            if route_part.startswith('[') and route_part.endswith(']'):
                key = route_part[1:-1]

                if key.endswith('?'):
                    key = key[:-1]
                value = path_part

                params[key] = value

            # segments
            elif route_part != path_part:
                return {}

        return params

    def find_route(self,path,method, routes):
        path_parts = path.strip('/').split('/')

        for route,config in routes.items():
            if config.get("method") != method:
                continue

            route_parts = route.strip('/').split('/')

            #optional only last param whit ?
            last = route_parts[-1]

            is_optional = (
                last.startswith('[') and
                last.endswith('?]')
            )

            if is_optional:
                min_parts = len(route_parts) - 1
                max_parts = len(route_parts)

                if len(path_parts) < min_parts or len(path_parts) > max_parts:
                    continue
            else:
                if len(path_parts) != len(route_parts):
                    continue

            match = True

            for route_part, path_part in zip(route_parts, path_parts):

                if route_part.startswith('[') and route_part.endswith(']'):
                    continue

                if route_part != path_part:
                    match = False
                    break

            if match:
                return route

        return None


