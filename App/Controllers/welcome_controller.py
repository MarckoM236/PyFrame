from App.Helpers.view import View

class WelcomeController:
    def index(self,request):
        name = request.query_params.get('name')

        return View.renderJ("welcome.html",{"name":name})

        