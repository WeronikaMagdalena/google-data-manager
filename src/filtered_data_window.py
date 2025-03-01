import smtplib

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton, QMessageBox


class FilteredDataWindow(QDialog):
    def __init__(self, filtered_data, parent):
        super().__init__()
        self.parent = parent
        self.filtered_data = filtered_data
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Filtered Data by Termin")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint | Qt.WindowMaximizeButtonHint)
        layout = QVBoxLayout()

        if self.filtered_data:
            self.table = QTableWidget()
            self.table.setRowCount(len(self.filtered_data))
            self.table.setColumnCount(len(self.filtered_data[0]))

            for row_idx, row in enumerate(self.filtered_data):
                for col_idx, cell in enumerate(row):
                    self.table.setItem(row_idx, col_idx, QTableWidgetItem(cell))

            layout.addWidget(self.table)

            # Add "Send Email Reminder" button
            self.email_button = QPushButton("Send Email Reminder")
            self.email_button.clicked.connect(self.send_email_reminder)
            layout.addWidget(self.email_button)

        else:
            layout.addWidget(QLabel("No data found for the selected Termin date."))

        self.setLayout(layout)

    def send_email_reminder(self):
        # TODO: Proper address
        sender_email = "noname01015501@gmail.com"  # Replace with your email
        # TODO: Secure method
        sender_password = "roof wewn eyoc zddo"  # Replace with your email password or app password

        subject = "Reminder: Upcoming Termin Date"
        body = "This is a reminder for your scheduled Termin."

        email_column_index = self.parent.parent.sheets_manager.get_headers().index("AS E-Mail")
        recipients = [row[email_column_index] for row in self.filtered_data if row[email_column_index]]
        print(recipients)

        server = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        server.ehlo()

        msg = f"""\
        From: {sender_email}
        To: {", ".join(recipients)}
        Subject: {subject}

        {body}"""

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipients, msg)
                print("Emails sent successfully!")
                QMessageBox.information(self, "Success", "Emails sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
            QMessageBox.critical(self, "Error", f"Failed to send email: {e}")
