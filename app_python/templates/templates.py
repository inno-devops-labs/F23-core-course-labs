from starlette.templating import Jinja2Templates


def SetUpTemplates(path):
    return Jinja2Templates(directory=path)

