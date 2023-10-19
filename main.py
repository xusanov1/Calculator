from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt6.QtCore import Qt
import sys


class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)

        self.last_written = ""

        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        self.result_label = QLabel("0")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(self.result_label)

        self.last_written_label = QLabel()
        self.last_written_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(self.last_written_label)

        buttons_layout = QGridLayout()
        main_layout.addLayout(buttons_layout)

        buttons = [
            {"text": "7", "row": 0, "col": 0},
            {"text": "8", "row": 0, "col": 1},
            {"text": "9", "row": 0, "col": 2},
            {"text": "4", "row": 1, "col": 0},
            {"text": "5", "row": 1, "col": 1},
            {"text": "6", "row": 1, "col": 2},
            {"text": "1", "row": 2, "col": 0},
            {"text": "2", "row": 2, "col": 1},
            {"text": "3", "row": 2, "col": 2},
            {"text": "0", "row": 3, "col": 0, "col_span": 2},
            {"text": ".", "row": 3, "col": 2},
            {"text": "+", "row": 0, "col": 3},
            {"text": "-", "row": 1, "col": 3},
            {"text": "*", "row": 2, "col": 3},
            {"text": "/", "row": 3, "col": 3},
            {"text": "=", "row": 4, "col": 0, "col_span": 4},
            {"text": "C", "row": 4, "col": 3},
        ]

        for button in buttons:
            btn = QPushButton(button["text"])
            btn.setMinimumSize(60, 60)
            btn.clicked.connect(lambda _, text=button["text"]: self.handle_button_click(text))

            if "col_span" in button:
                buttons_layout.addWidget(btn, button["row"], button["col"], 1, button["col_span"])
            else:
                buttons_layout.addWidget(btn, button["row"], button["col"])

        self.setCentralWidget(main_widget)

    def handle_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.last_written)
                self.result_label.setText(str(result))
                self.last_written = str(result)
            except Exception as e:
                self.result_label.setText("Error")
                print(e)
        elif text == "C":
            self.last_written = ""
            self.result_label.setText("0")
        else:
            self.last_written += text
            self.last_written_label.setText(self.last_written)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())
