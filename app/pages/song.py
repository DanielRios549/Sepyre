from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Song(app.types.Page):
    main: Sepyre

    def __post_init__(self):
        self.files: list[Audio] = []
        self.playing: bool = False
        self.current: int = 0

    def show(self):
        self.route = str(self.main.page.route)
        self.name = self.route.split('/')[2]

        self.main.layout.show(
            name=f'{self.name}',
            body=[
                ElevatedButton("Play", on_click=lambda _: self.play()),
                self.mixer(),
            ],
        )

    def mixer(self) -> ListView:
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
                    audio = Audio(
                        src=f'file://{folder}/{track.name}',
                        autoplay=False,
                        # on_duration_changed=lambda e: print("Duration changed:", e.data),
                        on_position_changed=lambda e: self.setPosition(e.data)
                    )

                    self.main.page.overlay.append(audio)
                    self.files.append(audio)

                    files.controls.append(Text(track.name[:-4]))

        return files

    def setPosition(self, time: int):
        self.current = time

    def play(self):
        for file in self.files:
            if self.playing is True:
                file.pause()
            else:
                if self.current == 0:
                    file.play()
                else:
                    file.resume()

        self.playing = not self.playing
