from dataclasses import dataclass
from genericpath import isfile
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Song():
    main: Sepyre

    def __post_init__(self):
        pass

    def show(self):
        self.route: str = self.main.page.route
        self.name = self.route.split('/')[2]

        self.main.page.add(
            Text(self.name)
        )

        self.main.page.appbar = self.main.layout.appBar(f'Library > Song')

        self.mixer()
        self.main.page.update()

    def mixer(self):
        folder = self.main.config.separation.joinpath(self.name)
        files = []

        if folder.exists() is True:
            for track in folder.iterdir():
                if track.is_file() and str(track).endswith('.wav'):
                    files.append(track)
