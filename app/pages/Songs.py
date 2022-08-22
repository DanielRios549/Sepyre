from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Songs():
    main: Sepyre
    page: app.flet.Page

    def __post_init__(self):
        self.items = ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=False
        )

    def show(self):
        folder = self.main.folder.joinpath('separation')

        if folder.exists() is False:
            folder.mkdir(0o775, False, False)

        for song in folder.iterdir():
            file = song.joinpath('info.conf')

            if file.exists() is True:
                options = app.parser.config(f'{file}')

                self.items.controls.append(
                    Row(
                        alignment='end',
                        controls=[
                            TextButton(
                                options['info']['name'],
                                data=song.name,
                                on_click=self.songOpen,
                                expand=True,
                            ),
                            IconButton(
                                data=song.name,
                                icon=icons.EDIT,
                                content=Text(options['info']['name']),
                                on_click=self.songRename,
                            )
                        ]
                    )
                )

        return self.items

    def songOpen(self, event: event.ControlEvent):
        song = event.data

    def songRename(self, event: event.ControlEvent):
        print(f'Song Rename: {event.data}')

    def showEdit(self):
        self.items = Text("Updated")
        self.page.update()

        return self.items
