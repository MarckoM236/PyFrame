from App.Controllers.HomeController import HomeController

routes = {
    "/": {"method": "GET", "class": HomeController, "function": "index"},
}