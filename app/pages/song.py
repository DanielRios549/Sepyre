from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Song(app.types.Page):
    main: Sepyre

    def __post_init__(self):
        pass

    def show(self):
        self.route: str = self.main.page.route
        self.name = self.route.split('/')[2]

        self.main.layout.show(
            self.mixer(),
            f'Library > Song'
        )

        self.main.page.update()

    def mixer(self):
        folder = self.main.config.separation.joinpath(self.name)
        files = ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=False
        )

        if folder.exists() is True:
            for track in folder.iterdir():
                if track.is_file() and str(track).endswith('.wav'):
                    files.controls.append(Text(track.name))

        return files
