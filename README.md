# PyFrame Framework

A lightweight Python micro-framework built from scratch for learning how modern web frameworks work internally.

PyFrame provides a minimal architecture based on:

* Routing
* Controllers
* Requests
* Responses
* Views
* Query Builder (coming soon)

The goal of this project is educational: understanding the internals of web frameworks by implementing each component from the ground up using Python sockets and core language features.

---

## Features

* Custom HTTP server
* Request parsing
* Route management
* Controller dispatching
* HTML view rendering
* Jinja2 template engine support
* Environment configuration
* Lightweight architecture
* Minimal external dependencies

---

## Project Structure

```text
PyFrame/
│
├── App/
│   ├── Controllers/
│   └── Helpers/
│
├── Core/
│   ├── request.py
│   ├── response.py
│   ├── router.py
│   └── server.py
│
├── Resources/
│   └── Views/
│
├── routes.py
├── main.py
└── .env
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-user/PyFrame.git
```

Move into the project directory:

```bash
cd PyFrame
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
APP_PORT=8000
APP_ENV=development
```

---

## Running the Server

```bash
python main.py
```

The application will be available at:

```text
http://localhost:8000
```

---

## Creating Routes

Example:

```python
from App.Controllers.welcome_controller import WelcomeController

routes = {
    "/": {
        "method": "GET",
        "class": WelcomeController,
        "function": "index"
    }
}
```

---

## Controllers

Example controller:

```python
class WelcomeController:

    def index(self, request):
        return "Hello World"
```

---

## Views

Example:

```python
#basic render template (only data text)
return View.render(
    "welcome.html",
    {
        "name": "Marco"
    }
)

#jinja2 render template (accept list,dicts)
return View.renderJ(
    "welcome.html",
    {
        "name":name
    }
)
```

Template:

```html
<h1>Welcome {{name}}</h1>
```

---

## Roadmap

* [x] HTTP Server
* [x] Request Parsing
* [x] Routing
* [x] Controllers
* [x] Views
* [ ] Route Parameters
* [ ] Middleware
* [ ] Query Builder
* [ ] Database Layer
* [ ] CLI Commands
* [ ] Template Engine
* [ ] Dependency Injection
* [ ] Session Management
* [ ] Authentication

---

## Motivation

PyFrame was created as an educational project to explore the internal mechanics of modern frameworks such as Laravel, Flask, Django and Express.

Rather than relying on existing abstractions, the framework implements core concepts manually to provide a deeper understanding of backend development.

---

## License

MIT License
