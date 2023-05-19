#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import *

class Question():
    def __init__(self,question1,btn_answer1,btn_answer2,btn_answer3,btn_answer4):
        self.question1 = question1
        self.btn_answer1 = btn_answer1
        self.btn_answer2 = btn_answer2
        self.btn_answer3 = btn_answer3
        self.btn_answer4 = btn_answer4


app = QApplication([])

main_win = QWidget()
main_win.cur = -1
main_win.cur1 = 0
main_win.setWindowTitle('Конкурс от Crazy People')


question = QLabel('ой?')
#группа
RadioGroupBox = QGroupBox('Варианты ответа')
#элементы
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')
a = [btn_answer1,btn_answer2,btn_answer3,btn_answer4]


line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()

line4 =QVBoxLayout()
line5 =QVBoxLayout()

line2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
line2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
line3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
line3.addWidget(btn_answer4, alignment = Qt.AlignCenter)

line1.addLayout(line2)
line1.addLayout(line3)

layout_main = QVBoxLayout()
RadioGroupBox.setLayout(line1)

button = QPushButton('ответить')
btn_answer11 = QLabel('Верно/неправильно')
btn_answer22 = QLabel('ы')
RadioGroupBox1 = QGroupBox('Результат теста')
line4.addWidget(btn_answer11, alignment = Qt.AlignCenter)
line4.addWidget(btn_answer22, alignment = Qt.AlignCenter)
line5.addLayout(line4)


Radio = QButtonGroup()
Radio.addButton(btn_answer1)
Radio.addButton(btn_answer2)
Radio.addButton(btn_answer3)
Radio.addButton(btn_answer4)
RadioGroupBox.setLayout(line1)
RadioGroupBox1.setLayout(line5)


layout_main.addWidget(question,alignment = Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox,alignment = Qt.AlignCenter)
layout_main.addWidget(RadioGroupBox1,alignment = Qt.AlignCenter)
layout_main.addWidget(button,alignment = Qt.AlignCenter)
RadioGroupBox1.hide()
main_win.setLayout(layout_main)
main_win.show()



main_win.setLayout(layout_main)
RadioGroupBox1.hide()
def show_res():  
    RadioGroupBox1.hide()
    RadioGroupBox.show()
    button.setText('Следующий вопрос')
def show_ans():
    main_win.cur += 1
    cheked_ans()
    random(list_q[main_win.cur])
    RadioGroupBox.hide()
    RadioGroupBox1.show()
    button.setText('ответить')
def proverka():
    if button.text() == 'ответить':
        show_res()
    else:
        show_ans()
def ask():
    Radio.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    Radio.setExclusive(True)
def random(Obj_q):
    shuffle(a)
    question.setText(Obj_q.question1)
    a[0].setText(Obj_q.btn_answer1)
    a[1].setText(Obj_q.btn_answer2)
    a[2].setText(Obj_q.btn_answer3)
    a[3].setText(Obj_q.btn_answer4)

def cheked_ans():
    if a[0].isChecked():
        btn_answer11.setText("Правильно")
        main_win.cur1 +=1
    else:
        btn_answer11.setText("Неправильно")
    btn_answer22.setText(a[0].text())

if main_win.cur == 2:
    setText(main_win.cur1/2*100)
list_q = []
list_q.append(Question('Вопрос 1','1','2','3','4'))
list_q.append(Question('Вопрос 2','1','2','3','4'))
ask()
button.clicked.connect(proverka) 
proverka()
main_win.show()
app.exec_()