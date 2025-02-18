from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDateEdit, QPushButton

from filtered_data_window import FilteredDataWindow


class TerminFilterWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Select a Termin Date:")
        layout.addWidget(self.label)

        self.date_picker = QDateEdit(self)
        self.date_picker.setCalendarPopup(True)
        layout.addWidget(self.date_picker)

        self.filter_button = QPushButton("Filter by Termin", self)
        self.filter_button.clicked.connect(self.filter_data)
        self.date_picker.setDate(QDate.currentDate())
        layout.addWidget(self.filter_button)

        self.setLayout(layout)

    def filter_data(self):
        selected_date = self.date_picker.date().toString("yyyy-MM-dd")
        filtered_data = self.filter_by_termin(selected_date)

        # Create a new window or dialog to show filtered data
        self.filtered_window = FilteredDataWindow(filtered_data)
        self.filtered_window.exec_()

    def filter_by_termin(self, selected_date):
        """Filter rows where the 'Termin' column matches the selected date."""
        data = self.parent.original_data
        termin_column_index = self.parent.sheets_manager.get_headers().index("Termin")
        termin_column = [row[termin_column_index] for row in data]

        # Filter rows based on the selected date
        filtered_data = [row for row in data if row[termin_column_index] == selected_date]
        return filtered_data
