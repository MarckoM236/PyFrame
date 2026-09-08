from App.Helpers.view import View

class HomeController:
    def index(self,request):
        name = request.query_params.get('name')

        return View.render("home.html",{"name":name})

        