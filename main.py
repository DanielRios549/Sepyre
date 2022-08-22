from dataclasses import dataclass
from app import flet, pages


@dataclass()
class Sepyre():
    page: flet.Page

    def __post_init__(self):
        print('APPLICATION STARTED')
        self.page.window_width = 400
        self.page.horizontal_alignment = 'center'

        pages.Main(self, self.page)
        self.page.update()


if __name__ == "__main__":
    flet.app(port=5500, target=Sepyre)  # , view=app.flet.WEB_BROWSER)
