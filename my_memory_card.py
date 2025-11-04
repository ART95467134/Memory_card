from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QRadioButton, QPushButton, QGroupBox, QMessageBox
)
from random import shuffle

class Question():
    def __init__(
    self, question, right_answer, wrong_answer1, wrong_answer2,
    wrong_answer3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

question_list = []
question_list.append(question('Какой национальности несуществует?','Энцы','Смурфы','Чульмцы','Алеуты'))
question_list.append(question('Государственный язык Бразилии','Португальский','Испанский','Итальянский','Английский'))
question_list.append(question('Какого цвета нет на флаге России?','Зелёный','Синий','Красный','Белый'))

app = QApplication([])

# Основное окно
window = QWidget()
window.setWindowTitle("Приложение Memory Card")
window.resize(400, 300)

# Вопрос
question_label = QLabel("Какой национальности не существует?")

# Группа с вариантами ответов
radio_group_box = QGroupBox("Варианты ответов")

button_1 = QRadioButton("Энцы")
button_2 = QRadioButton("Смурфы")
button_3 = QRadioButton("Чулымцы")
button_4 = QRadioButton("Алеуты")

# Макеты для кнопок
layout_ans2 = QVBoxLayout()
layout_ans2.addWidget(button_1)
layout_ans2.addWidget(button_2)

layout_ans3 = QVBoxLayout()
layout_ans3.addWidget(button_3)
layout_ans3.addWidget(button_4)

layout_ans1 = QHBoxLayout()
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radio_group_box.setLayout(layout_ans1)

# Кнопка "Ответить"
answer_button = QPushButton("Ответить")

# Результат

# Основной макет
main_layout = QVBoxLayout()
main_layout.addWidget(question_label, alignment=Qt.AlignCenter)
main_layout.addWidget(radio_group_box)
main_layout.addWidget(answer_button, alignment=Qt.AlignCenter)
#main_layout.addWidget(result_label, alignment=Qt.AlignCenter)
main_layout.setSpacing(10)

window.setLayout(main_layout)

answer = [button_1, button_2, button_3, button_4]

def ask(q:Question):
    shuffle(answer)

    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong_answer1)
    answer[2].setText(q.wrong_answer2)
    answer[3].setText(q.wrong_answer3)
    question_label.setText(question)

    correct.setText(q.right_answer)

def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    button_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnswerGroupBox.hide()
    button_OK.setText('Ответить')
    RadioGroupBox.setExclusive(False)
    button_1.setChecked(False)
    button_2.setChecked(False)
    button_3.setChecked(False)
    button_4.setChecked(False)
    RadioGroupBox.setExclusive(True)

def show_correct():
    result_label.setText
    show_result()
    
    
def check_answer():
    show_correct('Правильно')

def click_ok():
    if button_OK == 'Ответить':
        check_answer()
    else:
        next_question()

window.score = 0
window.total = 0
def next_question():
    window.total +=1
    print('Статистика\n-Всего вопросов:\n-Правильных ответов:\n-Рейтинг:')
    cur_question = randint

answer_button.clicked.connect(click_ok)

window.show()
app.exec_()