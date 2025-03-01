import pytz
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime
from google_calendar_manager import GoogleCalendarManager
from datetime import datetime, timedelta


class EventUploader:
    def __init__(self, parent):
        self.parent = parent
        self.calendar_manager = GoogleCalendarManager()

    def upload_event(self, row_data):
        try:
            event_title = "test"
            start_datetime_str = row_data[self.parent.termin_column]
            start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M")

            # Make the datetime object timezone-aware
            local_tz = pytz.timezone("Europe/Berlin")  # Replace with your local timezone
            start_datetime = local_tz.localize(start_datetime)

            duration_str = row_data[self.parent.plandauer_column]
            hours, minutes, seconds = map(int, duration_str.split(':'))
            duration = timedelta(hours=hours, minutes=minutes, seconds=seconds)

            end_datetime = start_datetime + duration

            # Extract address information
            street = row_data[4]  # Straße / Hausnummer
            postal_code = row_data[5]  # PLZ
            city = row_data[6]  # Ort
            address = f"{street}, {postal_code} {city}"

            self.calendar_manager.add_event(event_title, start_datetime, end_datetime, "Event Description", address)
            QMessageBox.information(self.parent, "Success", "Event uploaded to Google Calendar successfully!")
        except Exception as e:
            QMessageBox.critical(self.parent, "Error", f"Failed to upload event: {e}")