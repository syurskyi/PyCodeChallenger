from typing import List
from collections import defaultdict
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QComboBox, QHBoxLayout


class TwoSumFinder:
    # Defines a class named TwoSumFinder to encapsulate the functionality
    # of finding two numbers that sum up to a target value.
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        # def twoSum(nums: List[int], target: int) -> List[int]: Defines a static method named twoSum that takes
        # a list of integers nums and a target value target as arguments.
        # It returns a list of integers that are the indices of the two numbers in nums that add up to the target value.
        seen = defaultdict(int)
        # seen = defaultdict(int): Creates a defaultdict object called seen with a default value of 0. This dictionary
        # will be used to keep track of the numbers encountered during the iteration.
        for index, num in enumerate(nums):
            #  Iterates over the nums list using the enumerate function to access both the index and the value
            #  of each number.
            complement = target - num
            # Calculates the complement of the current number by subtracting it from the target value.
            if complement in seen:
                # Checks if the complement exists in the seen dictionary. If it does, it means that the complement
                # and the current number add up to the target value.
                # Returns a list containing the indices of the complement and the current number.
                return [seen[complement], index]
            seen[num] = index
            # Adds the current number to the seen dictionary with its index as the value.
        return []
    # Returns an empty list if no two numbers are found that add up to the target value.


class TwoSumFinderWindow(QMainWindow):
    @staticmethod
    def test_cases():
        return [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
        ]
    def __init__(self):
        #  Defines the constructor __init__ method. It sets up the main window, including the title,
        #  geometry, and layout.
        super().__init__()

        self.setWindowTitle("Two Sum Finder")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel()
        # Creates a QLabel widget called self.label to display the test case information and result.
        self.layout = QVBoxLayout()
        # Creates a QVBoxLayout object called self.layout to organize the widgets vertically.
        self.layout.addWidget(self.label)

        self.combo_box = QComboBox()
        # Creates a QComboBox widget called self.combo_box to select the test case.
        # It iterates over the test cases and adds them as items to the combo box.
        self.populate_combo_box()
        self.layout.addWidget(self.combo_box)

        self.calculate_button = QPushButton("Calculate")
        # Creates a QPushButton widget called self.calculate_button with the label "Calculate" and connects
        # its clicked signal to the calculate method.
        self.calculate_button.clicked.connect(self.calculate)
        self.layout.addWidget(self.calculate_button)

        central_widget = QWidget()
        # Creates a QWidget called central_widget and sets the layout to self.layout.
        # Then, sets the central widget of the main window to central_widget.
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def populate_combo_box(self):
        test_cases = self.test_cases()
        for idx, _ in enumerate(test_cases):
            self.combo_box.addItem(f"Test {idx + 1}")

    def calculate(self):
        # Defines the calculate method. It retrieves the selected index from the combo box, extracts
        # the corresponding test case, and calculates the result using the TwoSumFinder class.
        # It compares the result with the expected output and updates the label
        # with the test case information and result.

        selected_index = self.combo_box.currentIndex()
        if selected_index >= 0 and selected_index < len(self.test_cases()):
            nums, target, expected = self.test_cases()[selected_index]
            result = TwoSumFinder.twoSum(nums, target)
            if result == expected:
                result_str = "Test Passed"
            else:
                result_str = "Test Failed"

            test_info = f"Input: nums={nums}, target={target}\n"
            test_info += f"Result: {result}\n"
            test_info += f"Expected output: {expected}\n"
            test_info += f"Test Result: {result_str}\n\n"

            self.label.setText(test_info)

    def run(self):
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    window = TwoSumFinderWindow()
    window.run()
    app.exec_()
