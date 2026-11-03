from PySide6.QtCore import QEvent
from ok import Config, Icon
from ok.ui.qt.kit.buttons import Button
from ok.ui.qt.kit.labels import Label
from ok.ui.qt.widget.CustomTab import CustomTab
from src.tasks.MyOneTimeTask import MyOneTimeTask


class MyTab(CustomTab):
#  可以使用 ok.ui.qt.kit 或 PySide6 写自定义Tab

    def __init__(self):
        super().__init__()
        self.logger.info(f'MyTab init {self.__class__.__name__}')
        self.config = Config(self.__class__.__name__, {
            'config1': 0,
            'config2': "test_value"
        })
        self.icon = Icon.APPLICATION

        self.label = Label("This is a custom Tab")
        self.add_widget(self.label)

        self.button = Button("This is a button", variant="primary")
        self.button.clicked.connect(self.button_clicked)
        self.add_widget(self.button)

    @property
    def name(self):
        return "MyTab"

    def button_clicked(self):
        self.logger.info(f'MyTab clicked {self.__class__.__name__}')
        self.get_task(MyOneTimeTask).run()
        self.logger.info(f'MyTab clicked finished')

    def showEvent(self, event):
        super().showEvent(event)
        if event.type() == QEvent.Show:
            self.logger.info(f'MyTab Show {self.__class__.__name__}')


    def hideEvent(self, event: QEvent):
        super().hideEvent(event)
        self.logger.info(f'MyTab hide {self.__class__.__name__}')
