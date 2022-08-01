from PyQt5.QtWidgets import QLabel, QGroupBox, QGridLayout, QPushButton, QLineEdit, QCheckBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


def set_box_bp(s, visit):
    s.grb_bp = QGroupBox(s)
    s.grb_bp.setGeometry(210, 5, 585, 590)
    s.grb_bp.setVisible(visit)

    s.lay_bp = QGridLayout(s)
    s.grb_bp.setLayout(s.lay_bp)

    s.btn_bp = QPushButton('Решить', s.grb_bp)
    s.btn_bp.setGeometry(480, 555, 100, 30)

    s.title_bp = QLabel('Ускорение через силу', s.grb_bp)
    s.title_bp.move(240, 0)

    s.lbl_img_bp = QLabel(s.grb_bp)
    s.image_bp = QPixmap('formulas_image\\boost_through_power.png')
    w, h = 120, 120
    s.image_bp = s.image_bp.scaled(w, h, Qt.KeepAspectRatio)
    s.lbl_img_bp.setPixmap(s.image_bp)
    s.lbl_img_bp.setGeometry(232, 30, w, h)

    s.lbl_f_bp = QLabel('F [н] - сила =', s.grb_bp)
    s.lbl_m_bp = QLabel('m [кг] - масса =', s.grb_bp)
    s.lbl_a_bp = QLabel('a [м/с^2] - ускорение =', s.grb_bp)

    s.lbl_f_bp.setGeometry(10, 160, 220, 25)
    s.lbl_m_bp.setGeometry(10, 190, 220, 25)
    s.lbl_a_bp.setGeometry(10, 220, 220, 25)

    s.le_f_bp = QLineEdit(s.grb_bp)
    s.le_m_bp = QLineEdit(s.grb_bp)
    s.le_a_bp = QLineEdit(s.grb_bp)

    s.le_f_bp.setGeometry(240, 160, 150, 30)
    s.le_m_bp.setGeometry(240, 190, 150, 30)
    s.le_a_bp.setGeometry(240, 220, 150, 30)

    def decision():
        try:
            answer = str(float(s.le_f_bp.text())/float(s.le_m_bp.text()))
        except ValueError:
            answer = 0
        s.le_a_bp.setText(answer)

    s.btn_bp.clicked.connect(decision)

    return s.grb_bp


def set_box_bs(s, visit):
    s.grb_bs = QGroupBox(s)
    s.grb_bs.setGeometry(210, 5, 585, 590)
    s.grb_bs.setVisible(visit)

    s.lay_bs = QGridLayout(s)
    s.grb_bs.setLayout(s.lay_bs)

    s.btn_bs = QPushButton('Решить', s.grb_bs)
    s.btn_bs.setGeometry(480, 555, 100, 30)

    s.title_bs = QLabel('Ускорение через скорость', s.grb_bs)
    s.title_bs.move(240, 0)

    s.lbl_img_bs = QLabel(s.grb_bs)
    s.image_bs = QPixmap('formulas_image\\boost_through_speed.png')
    w, h = 120, 120
    s.image_bs = s.image_bs.scaled(w, h, Qt.KeepAspectRatio)
    s.lbl_img_bs.setPixmap(s.image_bs)
    s.lbl_img_bs.setGeometry(232, 30, w, h)

    s.lbl_v_bs = QLabel('v [м/с] - скорость =', s.grb_bs)
    s.lbl_t_bs = QLabel('t [с] - время =', s.grb_bs)
    s.lbl_a_bs = QLabel('a [м/с^2] - ускорение =', s.grb_bs)

    s.lbl_v_bs.setGeometry(10, 160, 220, 25)
    s.lbl_t_bs.setGeometry(10, 190, 220, 25)
    s.lbl_a_bs.setGeometry(10, 220, 220, 25)

    s.le_v_bs = QLineEdit(s.grb_bs)
    s.le_t_bs = QLineEdit(s.grb_bs)
    s.le_a_bs = QLineEdit(s.grb_bs)

    s.le_v_bs.setGeometry(240, 160, 150, 30)
    s.le_t_bs.setGeometry(240, 190, 150, 30)
    s.le_a_bs.setGeometry(240, 220, 150, 30)

    def decision():
        try:
            answer = str(float(s.le_v_bs.text())/float(s.le_t_bs.text()))
        except ValueError:
            answer = 0
        s.le_a_bs.setText(answer)

    s.btn_bs.clicked.connect(decision)

    return s.grb_bs


def set_box_speed(s, visit):
    s.grb_sp = QGroupBox(s)
    s.grb_sp.setGeometry(210, 5, 585, 590)
    s.grb_sp.setVisible(visit)

    s.lay_sp = QGridLayout(s)
    s.grb_sp.setLayout(s.lay_sp)

    s.btn_sp = QPushButton('Решить', s.grb_sp)
    s.btn_sp.setGeometry(480, 555, 100, 30)

    s.title_sp = QLabel('Скорость', s.grb_sp)
    s.title_sp.move(240, 0)

    s.lbl_img_sp = QLabel(s.grb_sp)
    s.image_sp = QPixmap('formulas_image\\speed.png')
    w, h = 120, 120
    s.image_sp = s.image_sp.scaled(w, h, Qt.KeepAspectRatio)
    s.lbl_img_sp.setPixmap(s.image_sp)
    s.lbl_img_sp.setGeometry(232, 30, w, h)

    s.lbl_s_sp = QLabel('∆s [м] - расстояние =', s.grb_sp)
    s.lbl_t_sp = QLabel('∆t [с] - время =', s.grb_sp)
    s.lbl_v_sp = QLabel('v [м/с] - скорость =', s.grb_sp)

    s.lbl_s_sp.setGeometry(10, 160, 220, 25)
    s.lbl_t_sp.setGeometry(10, 190, 220, 25)
    s.lbl_v_sp.setGeometry(10, 220, 220, 25)

    s.le_s_sp = QLineEdit(s.grb_sp)
    s.le_t_sp = QLineEdit(s.grb_sp)
    s.le_v_sp = QLineEdit(s.grb_sp)

    s.le_s_sp.setGeometry(240, 160, 150, 30)
    s.le_t_sp.setGeometry(240, 190, 150, 30)
    s.le_v_sp.setGeometry(240, 220, 150, 30)

    def decision():
        try:
            answer = str(float(s.le_s_sp.text()) / float(s.le_t_sp.text()))
        except ValueError:
            answer = 0
        s.le_v_sp.setText(answer)

    s.btn_sp.clicked.connect(decision)

    return s.grb_sp


def set_box_gravity(s, visit):
    s.grb_gr = QGroupBox(s)
    s.grb_gr.setGeometry(210, 5, 585, 590)
    s.grb_gr.setVisible(visit)

    s.lay_gr = QGridLayout(s)
    s.grb_gr.setLayout(s.lay_gr)

    s.btn_gr = QPushButton('Решить', s.grb_gr)
    s.btn_gr.setGeometry(480, 555, 100, 30)

    s.title_gr = QLabel('Сила тяжести', s.grb_gr)
    s.title_gr.setGeometry(210, 0, 200, 30)

    s.lbl_img_gr = QLabel(s.grb_gr)
    s.image_gr = QPixmap('formulas_image\\gravity.png')
    w, h = 300, 120
    s.image_gr = s.image_gr.scaled(w, h, Qt.KeepAspectRatio)
    s.lbl_img_gr.setPixmap(s.image_gr)
    s.lbl_img_gr.setGeometry(142, 30, w, h)

    s.lbl_m1_gr = QLabel('m1 [кг] - масса 1-го объекта =', s.grb_gr)
    s.lbl_m2_gr = QLabel('m1 [кг] - масса 2-го объекта =', s.grb_gr)
    s.lbl_r_gr = QLabel('r [м] - расстояние между объектами =', s.grb_gr)
    s.lbl_g_gr = QLabel('G - гравитационная постоянная', s.grb_gr)
    s.lbl_f_gr = QLabel('F [н] - сила =', s.grb_gr)

    s.lbl_m1_gr.setGeometry(10, 160, 300, 25)
    s.lbl_m2_gr.setGeometry(10, 190, 300, 25)
    s.lbl_r_gr.setGeometry(10, 220, 360, 25)
    s.lbl_g_gr.setGeometry(10, 250, 330, 25)
    s.lbl_f_gr.setGeometry(10, 280, 330, 25)

    s.le_m1_gr = QLineEdit(s.grb_gr)
    s.le_m2_gr = QLineEdit(s.grb_gr)
    s.le_r_gr = QLineEdit(s.grb_gr)
    s.le_f_gr = QLineEdit(s.grb_gr)

    s.cb_gr = QCheckBox('Использовать', s.grb_gr)

    s.le_m1_gr.setGeometry(375, 160, 150, 30)
    s.le_m2_gr.setGeometry(375, 190, 150, 30)
    s.le_r_gr.setGeometry(375, 220, 150, 30)
    s.le_f_gr.setGeometry(375, 280, 150, 30)

    s.cb_gr.setGeometry(375, 250, 150, 30)

    def decision():
        try:
            if s.cb_gr.checkState():
                g = 6.6743015 * 10**-11
                answer = str((float(s.le_m1_gr.text()) * float(s.le_m2_gr.text()) / float(s.le_r_gr.text())**2) * g)
            else:
                answer = str((float(s.le_m1_gr.text()) * float(s.le_m2_gr.text())) / float(s.le_r_gr.text()) ** 2)
        except ValueError:
            answer = 0
        s.le_f_gr.setText(answer)

    s.btn_gr.clicked.connect(decision)

    return s.grb_gr


def set_box_ff(s, visit):
    s.grb_ff = QGroupBox(s)
    s.grb_ff.setGeometry(210, 5, 585, 590)
    s.grb_ff.setVisible(visit)

    s.lay_ff = QGridLayout(s)
    s.grb_ff.setLayout(s.lay_ff)

    s.btn_ff = QPushButton('Решить', s.grb_ff)
    s.btn_ff.setGeometry(480, 555, 100, 30)

    s.title_ff = QLabel('Сила трения', s.grb_ff)
    s.title_ff.setGeometry(230, 0, 200, 30)

    s.lbl_img_ff = QLabel(s.grb_ff)
    s.image_ff = QPixmap('formulas_image\\friction_force.png')
    w, h = 300, 120
    s.image_ff = s.image_ff.scaled(w, h, Qt.KeepAspectRatio)
    s.lbl_img_ff.setPixmap(s.image_ff)
    s.lbl_img_ff.setGeometry(142, 30, w, h)

    s.lbl_nu_ff = QLabel('µ [] - коэффициент трения =', s.grb_ff)
    s.lbl_N_ff = QLabel('N [н] - сила реакции опоры =', s.grb_ff)
    s.lbl_f_ff = QLabel('F [н] - ускорение =', s.grb_ff)

    s.lbl_nu_ff.setGeometry(10, 160, 300, 25)
    s.lbl_N_ff.setGeometry(10, 190, 300, 25)
    s.lbl_f_ff.setGeometry(10, 220, 300, 25)

    s.le_nu_ff = QLineEdit(s.grb_ff)
    s.le_N_ff = QLineEdit(s.grb_ff)
    s.le_f_ff = QLineEdit(s.grb_ff)

    s.le_nu_ff.setGeometry(290, 160, 150, 30)
    s.le_N_ff.setGeometry(290, 190, 150, 30)
    s.le_f_ff.setGeometry(290, 220, 150, 30)

    def decision():
        try:
            answer = str(float(s.le_nu_ff.text()) * float(s.le_N_ff.text()))
        except ValueError:
            answer = 0
        s.le_f_ff.setText(answer)

    s.btn_ff.clicked.connect(decision)

    return s.grb_ff


def set_box_soe(s, visit):
    s.grb_soe = QGroupBox(s)
    s.grb_soe.setGeometry(210, 5, 585, 590)
    s.grb_soe.setVisible(visit)

    s.lay_soe = QGridLayout(s)
    s.grb_soe.setLayout(s.lay_soe)

    s.btn_soe = QPushButton('Решить', s.grb_soe)
    s.btn_soe.setGeometry(480, 555, 100, 30)

    s.title_soe = QLabel('Ускорение через скорость', s.grb_soe)
    s.title_soe.move(240, 0)

    s.lbl_img_soe = QLabel(s.grb_soe)
    s.image_soe = QPixmap('formulas_image\\the_strength_of_elasticity.png')
    w, h = 300, 120
    s.image_soe = s.image_soe.scaled(w, h, Qt.KeepAspectRatio)
    s.lbl_img_soe.setPixmap(s.image_soe)
    s.lbl_img_soe.setGeometry(152, 30, w, h)

    s.lbl_k_soe = QLabel('k [н/м] - коэффициент упругости =', s.grb_soe)
    s.lbl_l_soe = QLabel('∆l [м] - на сколько растянулось =', s.grb_soe)
    s.lbl_f_soe = QLabel('F [н] - сила =', s.grb_soe)

    s.lbl_k_soe.setGeometry(10, 160, 330, 25)
    s.lbl_l_soe.setGeometry(10, 190, 330, 25)
    s.lbl_f_soe.setGeometry(10, 220, 330, 25)

    s.le_k_soe = QLineEdit(s.grb_soe)
    s.le_l_soe = QLineEdit(s.grb_soe)
    s.le_f_soe = QLineEdit(s.grb_soe)

    s.le_k_soe.setGeometry(340, 160, 150, 30)
    s.le_l_soe.setGeometry(340, 190, 150, 30)
    s.le_f_soe.setGeometry(340, 220, 150, 30)

    def decision():
        try:
            answer = str(float(s.le_k_soe.text()) * float(s.le_l_soe.text()))
        except ValueError:
            answer = 0
        s.le_f_soe.setText(answer)

    s.btn_soe.clicked.connect(decision)

    return s.grb_soe


def set_box_rpd(s, visit):
    s.grb_rpd = QGroupBox(s)
    s.grb_rpd.setGeometry(210, 5, 585, 590)
    s.grb_rpd.setVisible(visit)

    s.lay_rpd = QGridLayout(s)
    s.grb_rpd.setLayout(s.lay_rpd)

    s.btn_rpd = QPushButton('Решить', s.grb_rpd)
    s.btn_rpd.setGeometry(480, 555, 100, 30)

    s.title_rpd = QLabel('Нахождение радиуса по дуге', s.grb_rpd)
    s.title_rpd.setGeometry(160, 0, 300, 30)

    s.lbl_img_rpd = QLabel(s.grb_rpd)
    s.image_rpd = QPixmap('formulas_image\\radius_po_arc.png')
    w, h = 400, 120
    s.image_rpd = s.image_rpd.scaled(w, h, Qt.KeepAspectRatio)
    s.lbl_img_rpd.setPixmap(s.image_rpd)
    s.lbl_img_rpd.setGeometry(175, 30, w, h)

    s.lbl_info_img_rpd = QLabel(s.grb_rpd)
    s.image_info_rpd = QPixmap('formulas_image\\info_rpd.png')
    wi, hi = 400, 230
    s.image_info_rpd = s.image_info_rpd.scaled(wi, hi, Qt.KeepAspectRatio)
    s.lbl_info_img_rpd.setPixmap(s.image_info_rpd)
    s.lbl_info_img_rpd.setGeometry(10, 350, wi, hi)

    s.lbl_h_rpd = QLabel('h [м] - высота =', s.grb_rpd)
    s.lbl_l_rpd = QLabel('l [м] - длина =', s.grb_rpd)
    s.lbl_r_rpd = QLabel('R [м] - радиус круга =', s.grb_rpd)
    s.lbl_info_rpd = QLabel('Эта формула используется для нахождения радиуса\n'
                            'окружности по параметрам её дуги как\n'
                            'l - расстояние между концами дуги\n'
                            'h - перпендикулярный отрезок от середины l до края дуги', s.grb_rpd)

    s.lbl_h_rpd.setGeometry(10, 160, 220, 25)
    s.lbl_l_rpd.setGeometry(10, 190, 220, 25)
    s.lbl_r_rpd.setGeometry(10, 220, 220, 25)
    s.lbl_info_rpd.setGeometry(10, 250, 550, 100)

    s.le_h_rpd = QLineEdit(s.grb_rpd)
    s.le_l_rpd = QLineEdit(s.grb_rpd)
    s.le_r_rpd = QLineEdit(s.grb_rpd)

    s.le_h_rpd.setGeometry(220, 160, 150, 30)
    s.le_l_rpd.setGeometry(220, 190, 150, 30)
    s.le_r_rpd.setGeometry(220, 220, 150, 30)

    def decision():
        try:
            answer = str((float(s.le_h_rpd.text())**2 + (float(s.le_l_rpd.text()) / 2)**2) /
                         (float(s.le_h_rpd.text()) * 2))
        except ValueError:
            answer = 0
        s.le_r_rpd.setText(answer)

    s.btn_rpd.clicked.connect(decision)

    return s.grb_rpd
