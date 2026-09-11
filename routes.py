from App.Controllers.welcome_controller import WelcomeController

routes = {
    "/": {"method": "GET", "class": WelcomeController, "function": "index"},
    "/home/[name?]": {"method": "GET", "class": WelcomeController, "function": "index"},
}