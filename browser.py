import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QToolBar, QWidget, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the QWebEngineView
        self.view = QWebEngineView(self)
        self.view.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.view)

        # Create the url bar
        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar_widget = QWidget(self)
        self.url_bar_layout = QHBoxLayout(self.url_bar_widget)
        self.url_bar_layout.addWidget(self.url_bar)
        self.url_bar_layout.setContentsMargins(0, 0, 0, 0)
        self.url_bar_widget.setLayout(self.url_bar_layout)

        # Create the toolbar
        self.toolbar = QToolBar(self)
        self.toolbar.addWidget(self.url_bar_widget)
        self.addToolBar(self.toolbar)

    def navigate_to_url(self):
        url = QUrl(self.url_bar.text())
        if url.scheme() == "":
            url.setScheme("http")
        self.view.setUrl(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())




