import math
import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from design import Ui_MainWindow


class MainWidget(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # loadUi('calculator.ui', self)
        self.setupUi(self)
        self.stackedWidget.setCurrentWidget(self.main)
        self.select.clicked.connect(self.select_shape)
        self.back.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main))

    def select_shape(self):
        shape_name = self.shape_group.checkedButton().objectName()
        self.stackedWidget.setCurrentWidget(
            getattr(self, f'{shape_name}_page', self.main))

        if shape_name == "wre":
            self.calculate.clicked.connect(self.wre_calc)
        elif shape_name == "samkutxedi":
            self.calculate.clicked.connect(self.samkutxedi_calc)
        elif shape_name == "trapecia":
            self.calculate.clicked.connect(self.trapecia_calc)
        else:
            self.calculate.clicked.connect(self.kvadrati_calc)

    def wre_calc(self):
        radius = self.r1.value()

        area = math.pi * (radius ** 2)
        perimeter = 2 * math.pi * radius

        self.lcd_r_area.display(area)
        self.lcd_r_perimeter.display(perimeter)

    def samkutxedi_calc(self):
        a, b, c = self.s1.value(), self.s2.value(), self.s3.value()

        s = (a + b + c) / 2
        # Calculate the area using Heron's formula
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        self.lcd_s_area.display(area)
        self.lcd_s_perimeter.display(s * 2)


    def trapecia_calc(self):
        a, b, c, d, h = self.t1.value(), self.t2.value(), self.t3.value(), self.t4.value(), self.h.value()

        base1 = a
        base2 = b

        area = (base1 + base2) * h / 2
        perimeter = a + b + c + h

        self.lcd_t_area.display(area)
        self.lcd_t_perimeter.display(perimeter)

    def kvadrati_calc(self):
        a = self.sq_1.value()

        area = a * a
        perimeter = 4 * a

        self.lcd_sq_area.display(area)
        self.lcd_sq_perimeter.display(perimeter)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWidget()
    window.show()

    sys.exit(app.exec_())
