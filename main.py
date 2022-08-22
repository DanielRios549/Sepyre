from dataclasses import dataclass
from pathlib import Path
from os import environ
from dotenv import load_dotenv
from app import flet, pages

load_dotenv()


@dataclass()
class Sepyre():
    page: flet.Page

    def __post_init__(self):
        self.home = Path.home()
        self.env = environ['MODE']
        self.folder: Path

        if self.env[:3] == 'dev':
            self.folder = Path(environ['FOLDER'])

        else:
            self.folder = self.home.joinpath('Sepyre')

        self.preLoad()

    def preLoad(self):
        self.page.window_width = 400
        self.page.padding = flet.Padding(10, 0, 10, 0)
        self.page.horizontal_alignment = 'center'

        self.current = pages.Main(self, self.page)

        self.page.appbar = self.appBar()
        self.page.update()

        self.current.show()

    def appBar(self):
        width = 50

        return flet.AppBar(
            toolbar_height=width,
            bgcolor=flet.colors.SURFACE_VARIANT,
            leading_width=width,
            leading=flet.IconButton(
                bgcolor=flet.colors.SURFACE_VARIANT,
                icon=flet.icons.MENU
            ),
            title=flet.Text("Library"),
            center_title=False,
            actions=[
                flet.IconButton(flet.icons.WB_SUNNY_OUTLINED, width=width),
                flet.PopupMenuButton(
                    width=width,
                    items=[
                        flet.PopupMenuItem(text="Autoplay")  # , on_click=self.item_clicked)
                    ]
                ),
            ],
        )


if __name__ == "__main__":
    flet.app(port=5500, target=Sepyre)  # , view=app.flet.WEB_BROWSER)
