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

        self.time = Ref[Text]()
        self.total = Ref[Text]()

    def updateTime(self, time: int, current: bool = False):
        if current is True:
            self.time.current.value = app.parser.time(time)
        else:
            self.total.current.value = app.parser.time(time)

        self.main.page.update()

    def show(self):
        self.route = str(self.main.page.route)
        self.name = self.route.split('/')[2]

        self.main.layout.show(
            name=f'{self.name}',
            body=[
                ElevatedButton("Play", on_click=lambda _: self.play()),
                Row(
                    [
                        Text(ref=self.time),
                        Text(ref=self.total)
                    ],
                    alignment='spaceBetween'
                ),
                Slider(
                    height=50,
                    width=1280,
                ),
                self.mixer(),
            ],
        )

        # if self.total.current.value is None and len(self.files) >= 1:
        #     time = self.files[0].get_duration()
        #     self.total.current.value = app.parser.time(time)

        # self.main.page.update()

    def mixer(self) -> ListView:
        folder = self.main.config.separation.joinpath(self.name)
        files = ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=False
        )

        if folder.exists() is True:
            for index, track in enumerate(folder.iterdir()):
                if track.is_file() and str(track).endswith('.wav'):
                    path = f'{folder}/{track.name}'

                    audio = Audio(
                        src=f'file://{path}',
                        autoplay=False,
                        on_position_changed=lambda e: self.updateTime(e.data, True)
                    )

                    self.main.page.overlay.append(audio)
                    self.files.append(audio)

                    border = [[0, 0, 0, 0], [0, 0, 0, 0]]

                    if index == 0:
                        border[0][0] = 6
                        border[1][1] = 6

                    elif index == len(list(folder.iterdir())) - 1:
                        border[0][2] = 6
                        border[1][3] = 6

                    files.controls.append(
                        Row(
                            [
                                Column(
                                    [
                                        Container(
                                            border_radius=app.flet.radius.BorderRadius(
                                                *border[0]),
                                            content=Text(
                                                track.name[:-4].capitalize()),
                                            bgcolor='blue',
                                            width=100,
                                            expand=True,
                                            padding=5
                                        )
                                    ],
                                ),
                                Column(
                                    [
                                        Container(
                                            border_radius=app.flet.radius.BorderRadius(
                                                *border[1]),
                                            content=Text(
                                                'Right', text_align='right'),
                                            bgcolor='red',
                                            expand=True,
                                            width=1280,
                                            padding=5
                                        )
                                    ],
                                    expand=True
                                )
                            ],
                            height=100,
                            alignment='spaceBetween'
                        )
                    )

        return files

    def play(self):
        for file in self.files:
            if self.playing is True:
                file.pause()
            else:
                if self.total.current == 0:
                    file.play()
                else:
                    file.resume()

        self.playing = not self.playing
