import sqlite3
import sys
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtGui import QFont
import time


class PomodoroTimer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pomodoro Timer")
        self.resize(800, 600)

        # Create the database and table
        self.create_database()

        # Create the main layout
        self.main_layout = QVBoxLayout()

        # Create the task input widgets
        self.task_label = QLabel("Task:")
        self.task_input = QLineEdit()
        self.duration_label = QLabel("Duration (minutes):")
        self.duration_input = QLineEdit()

        # Create the add task button
        self.add_task_button = QPushButton("Add Task")
        self.add_task_button.clicked.connect(self.add_task)

        # Create the timer display
        self.timer_label = QLabel()
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.timer_label.setFont(QFont("Arial", 36))

        # Create the start timer button
        self.start_timer_button = QPushButton("Start Timer")
        self.start_timer_button.clicked.connect(self.start_timer)

        # Create the tasks table
        self.tasks_table = QTableWidget()
        self.tasks_table.setColumnCount(3)
        self.tasks_table.setHorizontalHeaderLabels(
            ["Task", "Duration", "Completed"])
        self.tasks_table.verticalHeader().setVisible(False)
        self.tasks_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.populate_tasks_table()

        # Add the widgets to the layout
        self.main_layout.addWidget(self.task_label)
        self.main_layout.addWidget(self.task_input)
        self.main_layout.addWidget(self.duration_label)
        self.main_layout.addWidget(self.duration_input)
        self.main_layout.addWidget(self.add_task_button)
        self.main_layout.addWidget(self.timer_label)
        self.main_layout.addWidget(self.start_timer_button)
        self.main_layout.addWidget(self.tasks_table)

        # Set the central widget
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.central_widget)

        # Create the timer
        self.timer = QTimer()
        self.timer.setInterval(1000)  # 1 second
        self.timer.timeout.connect(self.update_timer)

        # Start the application
        self.show()

    def create_database(self):
        conn = sqlite3.connect('pomodoro_timer.db')
        c = conn.cursor()

        # Create the table
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT,
            duration INTEGER,
            completed INTEGER
        )''')

        # Save the changes
        conn.commit()

        # Close the connection
        conn.close()

    def add_task(self):
        # Get the task and duration from the input fields
        task = self.task_input.text()
        duration = int(self.duration_input.text())

        # Add the task to the database
        self.add_task_to_database(task, duration)

        # Populate the tasks table
        self.populate_tasks_table()

        # Clear the input fields
        self.task_input.clear()
        self.duration_input.clear()

    def add_task_to_database(self, task, duration):
        conn = sqlite3.connect('pomodoro_timer.db')
        c = conn.cursor()

        # Insert the task into the table
        c.execute(
            "INSERT INTO tasks (task, duration, completed) VALUES (?, ?, ?)", (task, duration, 0))

        # Save the changes
        conn.commit()

        # Close the connection
        conn.close()

    def populate_tasks_table(self):
        # Get all tasks from the database
        tasks = self.get_all_tasks()

        # Clear the tasks table
        self.tasks_table.clearContents()
        self.tasks_table.setRowCount(0)

        # Add the tasks to the table
        for task in tasks:
            row = self.tasks_table.rowCount()
            self.tasks_table.insertRow(row)
            self.tasks_table.setItem(row, 0, QTableWidgetItem(task[1]))
            self.tasks_table.setItem(row, 1, QTableWidgetItem(str(task[2])))
            self.tasks_table.setItem(
                row, 2, QTableWidgetItem("Yes" if task[3] else "No"))

    def get_all_tasks(self):
        conn = sqlite3.connect('pomodoro_timer.db')
        c = conn.cursor()

        # Get all tasks from the table
        tasks = c.execute("SELECT * FROM tasks").fetchall()

        # Close the connection
        conn.close()

        # Return the tasks
        return tasks

    def start_timer(self):
        # Get the duration from the input field
        duration = int(self.duration_input.text())

        # Convert the duration to seconds
        duration_seconds = duration * 60

        # Set the timer label
        self.timer_label.setText(
            f"{duration_seconds // 60:02d}:{duration_seconds % 60:02d}")

        # Start the timer
        self.timer.start()

    def update_timer(self):
        # Get the current time
        current_time = time.time()

        # Calculate the remaining time
        remaining_seconds = self.duration_input.text() * 60 - \
            (current_time - self.start_time)

        # If the timer is complete, stop the timer and mark the task as completed in the database
        if remaining_seconds <= 0:
            self.timer.stop()
            self.update_task_as_completed(self.task_input.text())

        # Update the timer label
        self.timer_label.setText(
            f"{remaining_seconds // 60:02d}:{remaining_seconds % 60:02d}")

    def update_task_as_completed(self, task):
        conn = sqlite3.connect('pomodoro_timer.db')
        c = conn.cursor()

        # Update the task as completed
        c.execute("UPDATE tasks SET completed = 1 WHERE task = ?", (task,))

        # Save the changes
        conn.commit()

        # Close the connection
        conn.close()

        # Populate the tasks table
        self.populate_tasks_table()


# Create the application
app = QApplication(sys.argv)

# Create the main window
window = PomodoroTimer()

# Run the application
sys.exit(app.exec())
