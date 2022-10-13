from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Songs():
    main: Sepyre

    def __post_init__(self):
        self.items = ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=False
        )

    def show(self):
        folder = self.main.config.separation

        if folder.exists() is False:
            folder.mkdir(0o775, False, False)

        count = len(list(folder.iterdir()))

        if count <= 1:
            self.items.controls.append(app.forms.Add(self.main).show())
        else:
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
        self.main.page.go(f'/song/{event.control.data}')
        self.main.page.update()

    def songRename(self, event: event.ControlEvent):
        print(f'Song Rename: {event.control.data}')

    def showEdit(self):
        self.items.controls.append(Text("Updated"))
        self.main.page.update()

        return self.items
