import sys
from PyQt5.QtWidgets import QApplication

from gui import GoogleSheetsApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GoogleSheetsApp("../service_account.json", "Data Link")
    window.show()
    sys.exit(app.exec_())
