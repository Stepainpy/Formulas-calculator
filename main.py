import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget
from formulas import *


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(600, 200, 800, 600)
        self.setWindowTitle('Решение по формулам')

        self.label_list = QLabel(self)
        self.label_list.setText('Формулы:')
        self.label_list.move(5, 0)

        self.formulas_list = QListWidget(self)
        self.formulas_list.setGeometry(5, 25, 200, 570)

        self.empty_grb = QGroupBox(self)
        self.empty_grb.setGeometry(210, 5, 585, 590)

        form = {
              'Скорость': [False, self.empty_grb],
              'ускорение через силу': [False, self.empty_grb],
              'ускорение через скорость': [False, self.empty_grb],
              'Сила трения': [False, self.empty_grb],
              'Сила упругости': [False, self.empty_grb],
              'Сила тяжести': [False, self.empty_grb],
              'Радиус по дуге': [False, self.empty_grb]
                }

        self.formulas_list.addItems(form)

        func_name = [
            [set_box_speed, 'Скорость'],
            [set_box_bp, 'ускорение через силу'],
            [set_box_bs, 'ускорение через скорость'],
            [set_box_ff, 'Сила трения'],
            [set_box_soe, 'Сила упругости'],
            [set_box_gravity, 'Сила тяжести'],
            [set_box_rpd, 'Радиус по дуге']
        ]

        for i in func_name:
            form[i[1]].pop(-1)
            form[i[1]].append(i[0](self, form[i[1]][0]))

        def show_box():
            name = self.formulas_list.selectedItems()[0].text()

            for grb in form:
                form[grb][1].setVisible(False)

            form[name][0] = True
            form[name][1].setVisible(True)

        self.formulas_list.itemClicked.connect(show_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    style = """
    QPushButton{
        font-size:17px;
    }
    QLineEdit{
        font-size:17px;
    }
    QLabel{
        font-size:20px;
    }
    QListWidget{
        font-size:15px;
    }
    QCheckBox{
        font-size:17px;
    }
    QCheckBox::indicator{
        width:24px;
        height:24px;
    }
    """
    app.setStyleSheet(style)

    ex = Window()
    ex.show()
    sys.exit(app.exec())
