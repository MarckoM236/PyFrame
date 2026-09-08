class Request:

    def __init__(self, request):
        self.request = request

        self.method = None
        self.path = None
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
        self.query_params = self.get_query_params(parts_http[1])

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