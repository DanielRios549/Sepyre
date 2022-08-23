from dataclasses import dataclass
from pathlib import Path
from os import environ
from dotenv import load_dotenv
import app

load_dotenv()


@dataclass()
class Sepyre():
    page: app.flet.Page

    def __post_init__(self):
        self.home = Path.home()
        self.env = environ['MODE']
        self.folder: Path

        if self.env[:3] == 'dev':
            self.folder = Path(environ['FOLDER'])

        else:
            self.folder = self.home.joinpath('Sepyre')

        self.layout = app.layouts.Main(self)
        self.config = app.Config(self)
        self.preLoad()

    def preLoad(self):
        self.page.window_width = 400
        self.page.padding = app.flet.Padding(10, 0, 10, 0)
        self.page.horizontal_alignment = 'center'

        self.current = app.pages.Main(self)

        self.current.show()
        self.page.on_route_change = self.routeChange

    def routeChange(self, change):
        self.page.appbar = None
        path: str = change.route
        name = path.split('/')[1]
        route = name if name != '' else 'main'

        self.current = self.routes(route)
        self.page.clean()

        self.current.show()
        self.page.update()

    def routes(self, route: str):  # -> app.pages.Page:
        routes = {
            'main': app.pages.Main(self),
            'song': app.pages.Song(self),
        }  # type: ignore

        return routes[route]


if __name__ == "__main__":
    app.flet.app(port=5500, target=Sepyre)
