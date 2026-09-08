class View:

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