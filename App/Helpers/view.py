from jinja2 import Environment, FileSystemLoader

class View:
    #create jinja environment
    env = Environment(
        loader=FileSystemLoader("Resources/Views")
    )

    #use basic render template
    @staticmethod
    def render(template, data=None):
        with open(
            f"Resources/Views/{template}",
            "r",
            encoding="utf-8"
        ) as file:
            content = file.read()

        if data:
            for key, value in data.items():
                content = content.replace(
                    "{{" + key + "}}",
                    str(value)
                )

        return content,"text/html"

    #use jinja render template
    @staticmethod
    def renderJ(template, data=None):

        load_template = View.env.get_template(template)

        return load_template.render(**data), "text/html"