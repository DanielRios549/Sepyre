from dataclasses import dataclass
from pathlib import Path
from os import environ, path
from dotenv import load_dotenv
import app

load_dotenv()


@dataclass()
class Sepyre():
    page: app.flet.Page

    def __post_init__(self):
        self.path = path.abspath(path.dirname(__file__))
        self.home = Path.home()

        self.env = environ.get('MODE') or 'prod'
        self.width = self.page.width

        self.folder = self.home.joinpath('Sepyre')
        self.file = environ.get('FILE') or 'sepyre.conf'

        if self.env[:3] == 'dev' and environ.get('FOLDER') is not None:
            self.folder = Path(environ['FOLDER'])

        self.options = {
            'path': self.path,
            'folder': self.folder,
            'file': self.file
        }

        self.layout = app.layouts.Main(self)
        self.config = app.Config(self)
        self.preLoad()

    def preLoad(self):
        self.page.window_maximized = True
        self.page.padding = app.flet.Padding(10, 0, 10, 0)
        self.page.horizontal_alignment = 'center'

        self.current = app.pages.Main(self)
        self.page.theme_mode = self.config.get('app', 'theme', 'dark')
        # self.page.theme = app.flet.Theme(
        #     brightness='dark',
        #     color_scheme_seed='green'
        # )

        self.current.show()
        self.page.on_route_change = self.routeChange
        self.page.on_resize = self.widthChange

    def widthChange(self, event: app.flet.event.ControlEvent):
        newWidth = event.data.split(',')[0]
        self.width = int(newWidth) if newWidth.isdigit() else self.page.width

        self.page.clean()
        self.current.show()

    def routeChange(self, event):  # RouteChangeEvent):
        self.page.appbar = None
        path: str = event.route
        name = path.split('/')[1]
        route = name if name != '' else 'main'

        self.current = self.views(route)
        self.page.clean()

        self.current.show()
        self.page.update()

    def views(self, route: str):  # -> app.pages.Page:
        routes = {
            'main': app.pages.Main(self),
            'song': app.pages.Song(self),
            'settings': app.pages.Settings(self)
        }  # type: ignore

        return routes[route]


if __name__ == "__main__":
    app.flet.app(port=5500, target=Sepyre, view=None)
