from dataclasses import dataclass
from main import Sepyre
from app.flet import *


@dataclass()
class Main():
    main: Sepyre

    def __post_init__(self):
        self.pages = [
            {
                'label': 'Library',
                'route': '/main',
                'icon': icons.HOME_OUTLINED,
                'selected_icon': icons.HOME
            },
            {
                'label': 'Settings',
                'route': '/settings',
                'icon': icons.SETTINGS_OUTLINED,
                'selected_icon': icons.SETTINGS
            }
        ]

    def show(self, body, name: str, page: int = None):   # type: ignore
        self.main.page.clean()
        self.main.page.appbar = self.appBar(name)

        if self.main.width >= 650:
            self.main.page.add(
                Row(
                    [
                        self.navRail(page),
                        VerticalDivider(width=1),
                        Column(
                            [body],
                            alignment="start",
                            expand=True
                        ),
                    ],
                    expand=True,
                )
            )
        else:
            self.main.page.add(
                body
            )

        self.main.page.update()

    def appBar(self, title: str = 'Sepyre'):
        width = 50

        return AppBar(
            toolbar_height=width,
            bgcolor=colors.SURFACE_VARIANT,
            title=TextButton(
                title,
                scale=1.5,
                on_click=lambda x: self.main.page.go('/')
            ),
            center_title=False,
            actions=[
                IconButton(icons.WB_SUNNY_OUTLINED, width=width, on_click=self.changeTheme),
                PopupMenuButton(
                    width=width,
                    items=[
                        PopupMenuItem(text="Autoplay")  # , on_click=self.item_clicked)
                    ]
                ),
            ],
        )

    def navRail(self, selected: int = None):  # type: ignore
        destinations = [
            NavigationRailDestination(
                label=page['label'],
                icon=page['icon'],
                selected_icon=page['selected_icon']
            )
            for page in self.pages
        ]

        return NavigationRail(
            selected_index=selected,
            label_type="all",
            extended=True,
            # leading=FloatingActionButton(icon=icons.CREATE, text="Add"),
            group_alignment=-0.9,
            destinations=[*destinations],
            on_change=lambda event: self.changePage(event.control.selected_index)
        )

    def changePage(self, index: int):
        self.main.page.route = self.pages[index]['route']
        self.main.page.update()

    def changeTheme(self, event: event.ControlEvent):
        theme = 'light'

        if self.main.page.theme_mode == 'light':
            theme = 'dark'

        self.main.config.update('app', 'theme', theme)

        self.main.page.theme_mode = theme
        self.main.page.update()
