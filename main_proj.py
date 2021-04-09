import sys
import math

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QLabel
from ui_file import Ui_MainWindow
from proj_calc import Ui_Calc

from proj_country import Ui_Country
from first_language import Ui_first_language
from second_language import Ui_second_language
from eng_support import Ui_eng_support
from currency import Ui_currency

from proj_city import Ui_City
from climate import Ui_climate
from rest import Ui_rest

from proj_cafe import Ui_Cafe

from proj_sights import Ui_Sights
from parking import Ui_parking

from cities import Ui_cities
from countries import Ui_countries

import pymysql

# КОЛИЧЕСТВО ВАРИАНТОВ ФИЛЬТРАЦИИ
COUNT_FIRST_LANG = 9
COUNT_SECOND_LANG = 3
COUNT_ENG_SUP = 3
COUNT_CURR = 5

COUNT_CLIMATE = 3
COUNT_REST = 2

COUNT_PARKING = 2

COUNT_CITIES = 13
COUNT_COUNTRIES = 10
# Подключение к бд имя_хоста, логин, пароль, имя_бд
con = pymysql.connect('localhost', 'root',
                      'root', 'proj_travel')
cur = con.cursor()

list_first_lang = []
list_second_lang = []
list_eng_sup = []
list_curr = []

list_climate = []
list_rest = []

list_parking = []

list_cities = []
list_countries = []


# Создание класса исключения


class WrongData(Exception):
    pass


class Parking(QWidget, Ui_parking):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxes = [self.yes, self.no]
        for i in self.boxes:
            if i.text() in list_parking:
                i.setChecked(True)
        self.bt_ok.clicked.connect(self.set_parking)

    def set_parking(self):
        global list_parking
        list_parking = []
        for i in self.boxes:
            if i.isChecked():
                list_parking.append(i.text())
        self.hide()


class Sight(QWidget, Ui_Sights):
    def __init__(self):
        self.cit = Cities_widg()
        self.park = Parking()
        global list_parking
        list_parking = []
        super().__init__()
        self.setupUi(self)
        self.list_sort = [self.price, self.my_rate]
        self.setting.clicked.connect(self.choose_filter)
        self.search.clicked.connect(self.show_table)

    def choose_filter(self):
        if self.filter_select.currentText() == 'Парковка':
            self.park.show()
        if self.filter_select.currentText() == 'Город':
            self.cit.show()

    def show_table(self):
        global list_parking, list_cities
        s1 = ''
        s2 = ''
        sort_string = ''
        if 0 < len(list_parking) < COUNT_PARKING:
            s1 += " parking = '" + "' OR parking = '".join(list_parking) + "'"
        if 0 < len(list_cities) < COUNT_CITIES:
            s2 += " city.name = '" + "' OR city.name = '".join(list_cities) + "'"
        query = '(' + ') AND ('.join(list(filter(lambda h: "''" not in h and h != '', [s1, s2]))) + ')'
        for t in self.list_sort:
            if t.isChecked():
                sort_string = ' ORDER BY ' + t.objectName()
                if t.objectName() == 'my_rate':
                    sort_string += " DESC"
        '''print('SELECT sights.name, city.name, sights.parking, sights.my_rate, sights.price,'
              'sights.adress, sights.advice FROM `sights` '
              'INNER JOIN city ON city.id = sights.cit_id WHERE ' + query + sort_string)'''
        if query != '' and query != '()':
            cur.execute('SELECT sights.name, city.name, sights.parking, sights.my_rate,'
                        'sights.price, sights.adress, sights.advice FROM `sights` '
                        'INNER JOIN city ON city.id = sights.cit_id WHERE ' + query + sort_string)
        else:
            cur.execute('SELECT sights.name, city.name, sights.parking, sights.my_rate, sights.price,'
                        'sights.adress, sights.advice FROM `sights` '
                        'INNER JOIN city ON city.id = sights.cit_id' + sort_string)
        res = cur.fetchall()
        list_title = ['Название', 'Город', 'Парковка', 'Моя оценка',
                      'Стоимость', 'Адрес', 'Рекомендация и описание']
        if res != ():
            vertical_layout = QVBoxLayout(self)
            for i in res:
                lay = QGridLayout(self)
                x, y = 0, 0
                for n, t in enumerate(i):
                    label = QLabel(self)
                    if n != 0:
                        label.setText(list_title[n] + ': ' + str(t))
                        label.setStyleSheet("font: 75 15pt \"MS Sans Serif\";")
                    else:
                        label.setText(str(t))
                        label.setStyleSheet("font: 87 22pt \"Segoe UI Black\";")
                    lay.addWidget(label, n, x)
                w = QWidget()
                w.setLayout(lay)
                vertical_layout.addWidget(w)
            w = QWidget()
            w.setLayout(vertical_layout)
            self.scrollArea.setWidget(w)
            self.scrollArea.show()
        else:
            vertical_layout = QVBoxLayout(self)
            label = QLabel(self)
            label.setText('По вашему запросу ничего не найдено')
            label.setStyleSheet("font: 87 22pt \"Segoe UI Black\";")
            vertical_layout.addWidget(label)
            w = QWidget()
            w.setLayout(vertical_layout)
            self.scrollArea.setWidget(w)
            self.scrollArea.show()


# Следующее окно


class Cities_widg(QWidget, Ui_cities):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxes = [self.agianapa, self.budapesht, self.salszburg, self.larnaca, self.limassol,
                      self.minsk, self.pafos, self.prague, self.riga, self.tallin, self.tbilisi,
                      self.torrevieja, self.narva]
        for i in self.boxes:
            if i.text() in list_cities:
                i.setChecked(True)
        self.bt_ok.clicked.connect(self.set_cities)

    def set_cities(self):
        global list_cities
        list_cities = []
        for i in self.boxes:
            if i.isChecked():
                list_cities.append(i.text())
        self.hide()


class Cafe(QWidget, Ui_Cafe):
    def __init__(self):
        super().__init__()
        self.cit = Cities_widg()
        self.setupUi(self)
        self.list_sort = [self.avg_price, self.my_rate]
        self.search.clicked.connect(self.show_table)
        self.setting.clicked.connect(self.choose_filter)

    def choose_filter(self):
        if self.filter_select.currentText() == 'Город':
            self.cit.show()

    def show_table(self):
        global list_cities
        s1 = ''
        sort_string = ''
        if 0 < len(list_cities) < COUNT_CITIES:
            s1 += " city.name = '" + "' OR city.name = '".join(list_cities) + "'"
        query = '(' + ') AND ('.join(list(filter(lambda h: "''" not in h and h != '', [s1]))) + ')'
        for t in self.list_sort:
            if t.isChecked():
                sort_string = ' ORDER BY ' + t.objectName()
                if t.objectName() == 'my_rate':
                    sort_string += " DESC"
        '''print('SELECT cafes.name, city.name, cafes.my_rate, cafes.avg_price,'
                    'cafes.adress, cafes.advice FROM `cafes` '
                    'INNER JOIN city ON city.id = cafes.cit_id WHERE ' + query + sort_string)'''
        if query != '' and query != '()':
            cur.execute('SELECT cafes.name, city.name, cafes.my_rate, cafes.avg_price,'
                        'cafes.adress, cafes.advice FROM `cafes` '
                        'INNER JOIN city ON city.id = cafes.cit_id WHERE ' + query + sort_string)
        else:
            cur.execute('SELECT cafes.name, city.name, cafes.my_rate, cafes.avg_price,'
                        'cafes.adress, cafes.advice FROM `cafes` '
                        'INNER JOIN city ON city.id = cafes.cit_id' + sort_string)
        res = cur.fetchall()
        list_title = ['Название', 'Город', 'Оценка', 'Средняя стоимость', 'Адрес', 'Рекомендация и описание']
        if res != ():
            vertical_layout = QVBoxLayout(self)
            for i in res:
                lay = QGridLayout(self)
                x, y = 0, 0
                for n, t in enumerate(i):
                    label = QLabel(self)
                    if n != 0:
                        label.setText(list_title[n] + ': ' + str(t))
                        label.setStyleSheet("font: 75 15pt \"MS Sans Serif\";")
                    else:
                        label.setText(str(t))
                        label.setStyleSheet("font: 87 22pt \"Segoe UI Black\";")
                    lay.addWidget(label, n, x)
                w = QWidget()
                w.setLayout(lay)
                vertical_layout.addWidget(w)
            w = QWidget()
            w.setLayout(vertical_layout)
            self.scrollArea.setWidget(w)
            self.scrollArea.show()
        else:
            vertical_layout = QVBoxLayout(self)
            label = QLabel(self)
            label.setText('По вашему запросу ничего не найдено')
            label.setStyleSheet("font: 87 22pt \"Segoe UI Black\";")
            vertical_layout.addWidget(label)
            w = QWidget()
            w.setLayout(vertical_layout)
            self.scrollArea.setWidget(w)
            self.scrollArea.show()


# Следующее окно


class Countries_widg(QWidget, Ui_countries):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxes = [self.austria, self.belarussia, self.greece, self.george,
                      self.hungary, self.spain, self.cyprus, self.estonia, self.latvia, self.chezh]
        for i in self.boxes:
            if i.text() in list_countries:
                i.setChecked(True)
        self.bt_ok.clicked.connect(self.set_countries)

    def set_countries(self):
        global list_countries
        list_countries = []
        for i in self.boxes:
            if i.isChecked():
                list_countries.append(i.text())
        self.hide()


class Rest(QWidget, Ui_rest):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxes = [self.hot, self.sight]
        for i in self.boxes:
            if i.text() in list_rest:
                i.setChecked(True)
        self.bt_ok.clicked.connect(self.set_rest)

    def set_rest(self):
        global list_rest
        list_rest = []
        for i in self.boxes:
            if i.isChecked():
                list_rest.append(i.text())
        self.hide()


class Climate(QWidget, Ui_climate):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxes = [self.hot, self.umeren, self.cold]
        for i in self.boxes:
            if i.text() in list_climate:
                i.setChecked(True)
        self.bt_ok.clicked.connect(self.set_climate)

    def set_climate(self):
        global list_climate
        list_climate = []
        for i in self.boxes:
            if i.isChecked():
                list_climate.append(i.text())
        self.hide()


class City(QWidget, Ui_City):
    def __init__(self):
        self.cou = Countries_widg()
        self.rest = Rest()
        self.clim = Climate()
        global list_climate, list_rest
        list_climate = list_rest = []
        super().__init__()
        self.setupUi(self)
        self.list_sort = [self.avg_temp, self.avg_day_cost]
        self.setting.clicked.connect(self.choose_filter)
        self.search.clicked.connect(self.show_table)

    def choose_filter(self):
        if self.filter_select.currentText() == 'Климат':
            self.clim.show()
        if self.filter_select.currentText() == 'Тип отдыха':
            self.rest.show()
        if self.filter_select.currentText() == 'Страна':
            self.cou.show()

    def show_table(self):
        global list_climate
        s1 = ''
        s2 = ''
        s3 = ''
        sort_string = ''
        if 0 < len(list_climate) < COUNT_CLIMATE:
            s1 += " climate = '" + "' OR climate = '".join(list_climate) + "'"
        if 0 < len(list_rest) < COUNT_REST:
            s2 += " rest_type = '" + "' OR rest_type = '".join(list_rest) + "'"
        if 0 < len(list_countries) < COUNT_COUNTRIES:
            s3 += " country.name = '" + "' OR country.name = '".join(list_countries) + "'"
        query = '(' + ') AND ('.join(list(filter(lambda h: "''" not in h and h != '', [s1, s2, s3]))) + ')'
        for t in self.list_sort:
            if t.isChecked():
                sort_string = ' ORDER BY ' + t.objectName()
        '''print(SELECT city.name, country.name, city.avg_temp, city.climate, city.rest_type, city.avg_day_cost FROM 
        city INNER JOIN country on country.id = city.cou_id WHERE ' + query + sort_string) '''
        if query != '' and query != '()':
            cur.execute(
                'SELECT city.name, country.name, city.avg_temp, city.climate, city.rest_type, city.avg_day_cost FROM '
                'city INNER JOIN country on country.id = city.cou_id WHERE ' + query + sort_string)
        else:
            cur.execute(
                'SELECT city.name, country.name, city.avg_temp, city.climate, city.rest_type, city.avg_day_cost FROM '
                'city INNER JOIN country on country.id = city.cou_id' + sort_string)
        res = cur.fetchall()
        list_title = ['Город', 'Страна', 'Средняя температура', 'Климат', 'Тип отдыха', 'Средняя суточная стоимость']
        if res != ():
            vertical_layout = QVBoxLayout(self)
            for i in res:
                lay = QGridLayout(self)
                x, y = 0, 0
                f = False
                for n, t in enumerate(i):
                    label = QLabel(self)
                    if n != 0:
                        label.setText(list_title[n] + ': ' + str(t))
                        label.setStyleSheet("font: 75 15pt \"MS Sans Serif\";")
                    else:
                        label.setText(str(t))
                        label.setStyleSheet("font: 87 22pt \"Segoe UI Black\";")
                    if not f and n == math.ceil(len(i) / 2):
                        x, y = 1, 1
                        f = True
                    x += 1
                    lay.addWidget(label, y, x)
                w = QWidget()
                w.setLayout(lay)
                vertical_layout.addWidget(w)
            w = QWidget()
            w.setLayout(vertical_layout)
            self.scrollArea.setWidget(w)
            self.scrollArea.show()
        else:
            vertical_layout = QVBoxLayout(self)
            label = QLabel(self)
            label.setText('По вашему запросу ничего не найдено')
            label.setStyleSheet("font: 87 22pt \"Segoe UI Black\";")
            vertical_layout.addWidget(label)
            w = QWidget()
            w.setLayout(vertical_layout)
            self.scrollArea.setWidget(w)
            self.scrollArea.show()


# Следующее окно


class FirstLang(QWidget, Ui_first_language):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxes = [self.espaniol, self.estonian, self.belorussian, self.chezh, self.georgian,
                      self.german, self.greek, self.hungrian, self.latvia]
        for i in self.boxes:
            if i.text() in list_first_lang:
                i.setChecked(True)
        self.bt_ok.clicked.connect(self.set_list_first)

    def set_list_first(self):
        global list_first_lang
        list_first_lang = []
        for i in self.boxes:
            if i.isChecked():
                list_first_lang.append(i.text())
        self.hide()


class SecondLang(QWidget, Ui_second_language):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxes = [self.russian, self.null_2, self.turkish]
        for i in self.boxes:
            if i.text() in list_second_lang:
                i.setChecked(True)
        self.bt_ok.clicked.connect(self.set_list_second)

    def set_list_second(self):
        global list_second_lang
        list_second_lang = []
        for i in self.boxes:
            if i.isChecked():
                list_second_lang.append(i.text())
        self.hide()


class EngSup(QWidget, Ui_eng_support):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxes = [self.nice, self.bad, self.middle]
        for i in self.boxes:
            if i.text() in list_eng_sup:
                i.setChecked(True)
        self.bt_ok.clicked.connect(self.set_eng_sup)

    def set_eng_sup(self):
        global list_eng_sup
        list_eng_sup = []
        for i in self.boxes:
            if i.isChecked():
                list_eng_sup.append(i.text())
        self.hide()


class Curr(QWidget, Ui_currency):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.boxes = [self.belrub, self.crona, self.euro, self.forint, self.lari]
        for i in self.boxes:
            if i.text() in list_curr:
                i.setChecked(True)
        self.bt_ok.clicked.connect(self.set_curr)

    def set_curr(self):
        global list_curr
        list_curr = []
        for i in self.boxes:
            if i.isChecked():
                list_curr.append(i.text())
        self.hide()


class Country(QWidget, Ui_Country):
    def __init__(self):
        self.curr = Curr()
        self.eng = EngSup()
        self.second_lang = SecondLang()
        self.first_lang = FirstLang()
        global list_first_lang, list_second_lang, list_eng_sup, list_curr
        list_first_lang = list_second_lang = list_eng_sup = list_curr = []
        super().__init__()
        self.setupUi(self)
        self.setting.clicked.connect(self.choose_filter)
        self.search.clicked.connect(self.show_table)

    def choose_filter(self):
        global list_first_lang, list_second_lang
        if self.filter_select.currentText() == 'Официальный язык':
            self.first_lang.show()
        if self.filter_select.currentText() == 'Второй язык':
            self.second_lang.show()
        if self.filter_select.currentText() == 'Понимание английского':
            self.eng.show()
        if self.filter_select.currentText() == 'Валюта':
            self.curr.show()

    def show_table(self):
        global list_first_lang, list_second_lang, list_eng_sup, list_curr
        s1 = ''
        s2 = ''
        s3 = ''
        s4 = ''
        if 0 < len(list_first_lang) < COUNT_FIRST_LANG:
            s1 += " first_language = '" + "' OR first_language = '".join(list_first_lang) + "'"
        if 0 < len(list_second_lang) < COUNT_SECOND_LANG:
            s2 += " second_language = '" + "' OR second_language = '".join(list_second_lang) + "'"
        if 0 < len(list_eng_sup) < COUNT_ENG_SUP:
            s3 += " eng_support = '" + "' OR eng_support = '".join(list_eng_sup) + "'"
        if 0 < len(list_curr) < COUNT_CURR:
            s4 += " currency = '" + "' OR currency = '".join(list_curr) + "'"
        query = '(' + ') AND ('.join(list(filter(lambda h: "''" not in h and h != '', [s1, s2, s3, s4]))) + ')'
        if query != '' and query != '()':
            cur.execute('SELECT name, first_language, second_language, eng_support, '
                        'currency FROM country WHERE ' + query)
        else:
            cur.execute('SELECT name, first_language, second_language, eng_support, currency FROM country')
        res = cur.fetchall()
        list_title = ['Страна', 'Официальный язык', 'Второй язык', 'Понимание английского', 'Валюта']
        if res != ():
            vertical_layout = QVBoxLayout(self)
            for i in res:
                lay = QGridLayout(self)
                x, y = 0, 0
                f = False
                for n, t in enumerate(i):
                    label = QLabel(self)
                    if n != 0:
                        label.setText(list_title[n] + ': ' + str(t))
                        label.setStyleSheet("font: 75 15pt \"MS Sans Serif\";")
                    else:
                        label.setText(str(t))
                        label.setStyleSheet("font: 87 22pt \"Segoe UI Black\";")
                    if not f and n == math.ceil(len(i) / 2):
                        x, y = 1, 1
                        f = True
                    x += 1
                    lay.addWidget(label, y, x)
                w = QWidget()
                w.setLayout(lay)
                vertical_layout.addWidget(w)
            w = QWidget()
            w.setLayout(vertical_layout)
            self.scrollArea.setWidget(w)
            self.scrollArea.show()
        else:
            vertical_layout = QVBoxLayout(self)
            label = QLabel(self)
            label.setText('По вашему запросу ничего не найдено')
            label.setStyleSheet("font: 87 22pt \"Segoe UI Black\";")
            vertical_layout.addWidget(label)
            w = QWidget()
            w.setLayout(vertical_layout)
            self.scrollArea.setWidget(w)
            self.scrollArea.show()


# Следующее окно

class Calc(QWidget, Ui_Calc):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        cur.execute("SELECT name From city")
        result = cur.fetchall()
        for i in result:
            self.cit_choice.addItem(i[0])
        self.bt_solve.clicked.connect(self.solve)

    def solve(self):
        selected_city = self.cit_choice.currentText()
        cur.execute("SELECT avg_day_cost FROM city WHERE name = '{}'".format(selected_city))
        daily_price = int(cur.fetchone()[0])
        try:
            if not (self.day_count.text().isdigit()) or not (self.guests_count.text().isdigit()) \
                    or not (self.guests_count_2.text().isdigit()):
                raise WrongData
            else:
                if int(self.guests_count.text()) != 1:
                    self.out_cost.setText(str(int(daily_price *
                                                  int(self.day_count.text()) *
                                                  (int(self.guests_count.text()) / 2 +
                                                   int(self.guests_count_2.text()) / 4))) + ' руб.')
                else:
                    self.out_cost.setText(str(int(daily_price *
                                                  int(self.day_count.text()) *
                                                  (int(self.guests_count.text()) +
                                                   int(self.guests_count_2.text()) / 4))) + ' руб.')
        except WrongData:
            self.out_cost.setText('Введены некоректные данные(')


class Menu(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.sight = Sight()
        self.cafe = Cafe()
        self.city = City()
        self.country = Country()
        self.calc = Calc()
        self.setupUi(self)
        self.bt_calc.clicked.connect(self.opencalc)
        self.bt_country.clicked.connect(self.opencountry)
        self.bt_city.clicked.connect(self.opencity)
        self.bt_cafe.clicked.connect(self.opencafe)
        self.bt_sight.clicked.connect(self.opensights)

    def opencalc(self):
        self.calc.show()

    def opencountry(self):
        self.country.show()

    def opencity(self):
        self.city.show()

    def opencafe(self):
        self.cafe.show()

    def opensights(self):
        self.sight.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec_())
