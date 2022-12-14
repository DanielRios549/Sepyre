from dataclasses import dataclass
from main import Sepyre
from app.flet import *
import app


@dataclass()
class Main():
    main: Sepyre

    def __post_init__(self):
        self.nav = Ref[Row]()
        self.content = Ref[Column]()

        self.menu: list[app.types.Menu] = [
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

        self.main.page.add(
            Row(
                [
                    self.navRail(),
                    VerticalDivider(width=1),
                    Column(ref=self.content, expand=True)
                ],
                expand=True,
            )
        )

    def show(self, name: str, body: 'list[Control]', page: int = None):  # type: ignore
        self.content.current.clean()
        self.main.page.appbar = self.appBar(name)

        self.content.current.controls.append(
            Column(
                controls=[item for item in body],
                alignment='start',
                expand=True
            )
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
                IconButton(
                    icons.WB_SUNNY_OUTLINED,
                    width=width,
                    on_click=self.changeTheme
                ),
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
                label=menu['label'],
                icon=menu['icon'],
                selected_icon=menu['selected_icon']
            )
            for menu in self.menu
        ]

        # route = self.main.page.route or 0
        # selected = [index for index, menu in enumerate(self.menu) if menu['route'] == self.menu.index('')][0]
        # print(self.menu.index('route'))

        return NavigationRail(
            # TODO: Fix Selected Index
            selected_index=selected,
            min_extended_width=300,
            extended=True,
            # leading=FloatingActionButton(icon=icons.CREATE, text="Add"),
            trailing=self.main.player.showCard(),
            destinations=[*destinations],
            on_change=lambda event: self.changePage(
                event.control.selected_index
            )
        )

    def changePage(self, index: int):
        self.main.page.route = self.menu[index]['route']
        self.main.page.update()

    def changeTheme(self, event: event.ControlEvent):
        theme = 'light'

        if self.main.page.theme_mode == 'light':
            theme = 'dark'

        self.main.config.update('app', 'theme', theme)

        self.main.page.theme_mode = theme
        self.main.page.update()
