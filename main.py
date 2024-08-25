import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from utils import validators

class SpotifyValidatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Enter Spotify URL:")
        layout.addWidget(self.label)

        self.url_input = QLineEdit(self)
        layout.addWidget(self.url_input)

        self.validate_button = QPushButton("Validate", self)
        self.validate_button.clicked.connect(self.validate_url)
        layout.addWidget(self.validate_button)

        self.setLayout(layout)
        self.setWindowTitle('Spotify URL Validator')
        self.setGeometry(300, 300, 400, 150)

    def validate_url(self):
        url = self.url_input.text()
        
        try:
            valid_uri = validators.extract_and_validate_spotify_uri(url)
            QMessageBox.information(self, "Result", f"Valid URL: {valid_uri}")
        except ValueError:
            QMessageBox.critical(self, "Result", "Invalid URL")

def main():
    app = QApplication(sys.argv)

    validator_app = SpotifyValidatorApp()
    validator_app.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
