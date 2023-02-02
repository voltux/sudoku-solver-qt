import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from Ui_Sudoku import Ui_MainWindow
import solver


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.btn_solve.clicked.connect(self.solve)

    def solve(self):
        grid = []
        for i in range(9):
            grid.append([0]*9)

        for i in range(9):
            for j in range(9):
                try:
                    number = int(self.tbl_sudoku.item(i, j).text())
                    if number not in range(10):
                        number = 0
                except Exception:
                    number = 0
                grid[i][j] = number

        solver.solve_gen(grid)
        for i in range(9):
            for j in range(9):
                new_item = QTableWidgetItem(str(solver.solution[i, j]))
                self.tbl_sudoku.setItem(i, j, new_item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
