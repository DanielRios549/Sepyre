from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Player():
    main: Sepyre

    def __post_init__(self):
        self.files: list[Audio] = []
        self.playing: bool = False

        self.name = Ref[Text]()
        self.time = Ref[Text]()
        self.total = Ref[Text]()
        self.card = Ref[Card]()

    def updateTime(self, time: int, current: bool = False):
        if current is True:
            self.time.current.value = app.parser.time(time)
        else:
            self.total.current.value = app.parser.time(time)

        self.main.page.update()

    def playPause(self, files: 'list[Audio]', name: str):
        if name == self.name.current:
            self.playAll()
        else:
            [file.pause() for file in self.files]
            self.files.clear()

            self.name.current.value = name
            self.files = files

            self.playAll()

        self.main.page.update()

    def playAll(self):
        for file in self.files:
            if self.playing is True:
                file.pause()
            else:
                if self.total.current == 0:
                    file.play()
                else:
                    file.resume()

        self.playing = not self.playing

    def showCard(self) -> Card:
        return Card(
            ref=self.card,
            content=Column(
                expand=True,
                alignment='end',
                height=680,
                # alignment=app.flet.alignment.bottom_center,
                controls=[
                    Row(
                        controls=[
                            Text(ref=self.name, value='No Song Playing.', text_align='center', width=280)
                        ]
                    ),
                    Row(
                        alignment='center',
                        controls=[
                            IconButton(
                                icon=icons.PLAY_CIRCLE_FILL,
                                icon_size=50
                            ),
                            Slider(
                                height=50,
                                width=200
                            )
                        ]
                    )
                ]
            )
        )
