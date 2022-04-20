# 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
import time
from collections import defaultdict
from pages.logger import Logger
import allure
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
import urllib3
# from manager.manager_base import МенеджерСайта
from pages.base_page import BasePage
#from dictionary.dict_functions import DictionaryFunctions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import keys
import os

@allure.feature('Автотест тарифного плана "Крипто"')
class TestGeneral:

    @allure.story('1 ШАГ Сведения об организации')
    @allure.title('Проверка раздела "Общие сведения"')
    def test_step1(self):
        with allure.step('Переход на шаг "Общие сведения"'):
            self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/common")
            BasePage.ожидание_прогрузки_страницы(self.browser)

        with allure.step('Поиск панеля "Общие сведения"'):
            panel = BasePage.Panel.get_panel_by_name(self,"Общие сведения")

        with allure.step('Поиск параметра "ИНН"'):
            panel.search_parametr("ИНН")

        with allure.step('Поиск параметра "КПП"'):
            kpp_parametr = panel.search_parametr("КПП")

        with allure.step('Ввод данных в поле "КПП"'):
            kpp_parametr.set_value("123456789")

        with allure.step('Поиск параметра "ОГРН"'):
            panel.search_parametr("ОГРН")

        with allure.step('Поиск параметра "Краткое наименование организации"'):
            panel.search_parametr("Краткое наименование организации")

        with allure.step('Поиск параметра "Полное наименование организации"'):
            panel.search_parametr("Полное наименование организации")

        with allure.step('Поиск параметра "Условное сокращение"'):
            panel.search_parametr("Условное сокращение")

        with allure.step('Поиск параметра "Тип организации"'):
            panel.search_parametr("Тип организации")

        with allure.step('Поиск параметра "Наименование и реквизиты учредительного документа"'):
            name_doc_parametr = panel.search_parametr("Наименование и реквизиты учредительного документа")

        with allure.step('Ввод данных в поле "Наименование и реквизиты учредительного документа"'):
            name_doc_parametr.set_value("НИРУД тестовый 1")

        with allure.step('Поиск параметра "Лицензии на вид деятельности"'):
            panel.search_parametr("Лицензии на вид деятельности")

        with allure.step('Поиск параметра "Населённый пункт"'):
            panel.search_parametr("Населённый пункт")

        with allure.step('Поиск параметра "Юридический адрес"'):
            panel.search_parametr("Юридический адрес")

        with allure.step('Поиск параметра "Фактический адрес"'):
            panel.search_parametr("Фактический адрес")

        with allure.step('Поиск параметра "Почтовый адрес"'):
            panel.search_parametr("Почтовый адрес")

        with allure.step('Поиск параметра "Адрес электронной почты"'):
            panel.search_parametr("Адрес электронной почты")
    time.sleep(5)

    @allure.story('2 ШАГ Структурные подразделения')
    @allure.title('Првоерка таблицы "Структурные подрзаделения"')
    def test_step2(self):

        with allure.step('Проверка перехода на шаг "Структурные подразделения"'):
            self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/structure")
            BasePage.ожидание_прогрузки_страницы(self.browser)

        with allure.step('Поиск таблицы "Структурные подразделения"'):
            table = BasePage.Table.get_table_by_name(self, "Структурные подразделения")

        with allure.step('Нажатие на кнопку "Добавить структурное подразделение"'):
            table.command("Добавить структурное подразделение")
            BasePage.ожидание_прогрузки_страницы(self.browser)

        with allure.step("Проверка наименования формы 'Добавление структурного подразделения'"):
            add_modal = BasePage.ModalWindow.searchByHeaderText(self,"Добавление структурного подразделения")
            BasePage.ожидание_прогрузки_страницы(self.browser)

        with allure.step("Поиск поля 'Добавление структурного подразделения'"):
            name_patametr = add_modal.search_parametr("Наименование структурного подразделения")

        with allure.step("Ввод параметра 'Наименование структурного подразделения '"):
            name_patametr.set_value("Наименование СП")

        with allure.step("Сохранение модального окна 'Добавление структурного подразделения'"):
            add_modal.command("Добавить структурное подразделение")
            BasePage.ожидание_прогрузки_страницы(self.browser)

        with allure.step("Поиск добавленной записи "):
            search_add = table.search_record_by_value("СТРУКТУРНОЕ ПОДРАЗДЕЛЕНИЕ", "Наименование СП")
            BasePage.ожидание_прогрузки_страницы(self.browser)
        time.sleep(10)

        '''
        with allure.step('Проверка наличия колонки "СТРУКТУРНОЕ ПОДРАЗДЕЛЕНИЕ"'):
            table.check_table_have_column("СТРУКТУРНОЕ ПОДРАЗДЕЛЕНИЕ")
            assert True, f'Нет колонки "СТРУКТУРНОЕ ПОДРАЗДЕЛЕНИЕ"'

        with allure.step('Проверка наличия колонки "ФИЛИАЛ"'):
            table.check_table_have_column("ФИЛИАЛ")
            assert True, f'Нет колонки "ФИЛИАЛ"'

        with allure.step('Проверка наличия колонки "КПП"'):
            table.check_table_have_column("КПП")
            assert True, f'Нет колонки "КПП"'

    #    with allure.step('Првоерка загрузки структурных подразделений'):
     #       name_file = 'SP.xlsx'
      #      BasePage.file_upload(self, name_file)
       #     assert True, f'Ошибка при загрузке структурных подразделений'

        BasePage.ожидание_прогрузки_страницы(self.browser)
        with allure.step('Поиск по колонке "СТРУКТУРНОЕ ПОДРАЗДЕЛЕНИЕ"'):
            table.check_rows_search("СТРУКТУРНОЕ ПОДРАЗДЕЛЕНИЕ")
            assert True, f'Ошибка при поиске по колонке"СТРУКТУРНОЕ ПОДРАЗДЕЛЕНИЕ"'

        BasePage.ожидание_прогрузки_страницы(self.browser)
        #with allure.step('Поиск по колонке "КПП"'):
         #   table.check_rows_search("КПП")
          #  assert True, f'Ошибка при поиске по колонке"КПП"

        BasePage.ожидание_прогрузки_страницы(self.browser)
        with allure.step('Изменение кол-ва отображаемых элементов на странице'):
            table.check_rows_count()
            assert True, f'Ошибка при изменение кол-ва элементов на странице'

        with allure.step('Проверка возможности выбора записей'):
            table.check_rows_have_select()
            assert True, f'Отсутствует возможность выбора записей таблицы'

        with allure.step('Перемещеине записей в таблице "СТРУКТУРНОЕ ПОДРАЗДЕЛЕНИЕ"'):
            table.check_rows_replace(count=10)
            assert True, f'Ошибка при перемещении записей в таблице "СТРУКТУРНОЕ ПОДРАЗДЕЛЕНИЕ"'\


        with allure.step('Проверка на наличие ошибки таблицы'):
            table.check_have_errors()
            assert True, f'Ошибка таблицы присутствует'
    '''
    @allure.story('3 ШАГ Сотрудники организации')
    @allure.title('Првоерка таблицы "Сотрудники организации"')
    def test_step3(self):
        with allure.step('Проверка прехода на шаг "Сотрудники организации"'):
            self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/employees")
            BasePage.ожидание_прогрузки_страницы(self.browser)
            assert True,f'Ошибка припереходе на шаг "Сотрудники организации"'

        '''
        name_file = 'worker.xlsx'
        BasePage.file_upload(self, name_file)
        BasePage.file_upload(self, name_file, delete=False)

        table = BasePage.Table.get_table_by_name(self, "Сотрудники организации")
        # table.search_record_by_value("ФИО СОТРУДНИКА", "Иванов Иван Иванович")

        """Поиск"""
        table.check_rows_search("ФИО СОТРУДНИКА")
        table.check_rows_search("ДОЛЖНОСТЬ СОТРУДНИКА")
        # table.check_rows_search("КОНТАКТНЫЕ ТЕЛЕФОНЫ")
        # table.check_rows_search("АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ")

        table.check_have_filtercontrol()

        """Кол-во элементов на странице"""
        table.check_rows_count()

        table.check_table_have_column("ФИО СОТРУДНИКА")
        table.check_table_have_column("ДОЛЖНОСТЬ СОТРУДНИКА")
        table.check_table_have_column("КОНТАКТНЫЕ ТЕЛЕФОНЫ")
        table.check_table_have_column("АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ")
        table.check_table_have_column("ДАТА ПРИЁМА")
        table.check_table_have_column("СОЗДАНО")
        table.check_table_have_column("ИЗМЕНЕНО")

        """Проверка на возможность изменения порядка записей"""
        table.check_rows_have_reorder()

        """Перемещение"""
        #table.check_rows_replace(count=10)

        """Првоерка выбора записей"""
        table.check_rows_have_select()

        """Ошибка таблицы"""
        table.check_have_errors()

        """Экспорт в Excel"""
        BasePage.file_export(self)
        time.sleep(5)

        """Удаление"""
        BasePage.all_delete(self)
        time.sleep(5)
        '''
        BasePage.not_next_step(self)


    def test_step4(self):
        self.browser.get(self.common_address + "cabinet/main_wizard/personal_data_crypto_standalone/#step/crypto-access-std")
        BasePage.ожидание_прогрузки_страницы(self.browser)

        """
        Ответственный пользователь криптосредств
        

        self.browser.find_element_by_xpath("//*[@class='btn btn-info']").click()
        BasePage.ожидание_прогрузки_страницы(self.browser)
        table = BasePage.Table.get_table_by_name(self, "Выбор сотрудника")
        rows = table.search_record_by_value("ФИО СОТРУДНИКА", "Коварный Отголосок Спинозович")
        rows = table.search_record_by_value("ДОЛЖНОСТЬ СОТРУДНИКА", "телохранитель")
        self.browser.find_elements_by_xpath("//*[@class='radio radio-awesome radio-success radio-inline']")
        self.browser.find_element_by_xpath("//*[@class='modal-footer']/*[contains(text(), 'Выбрать сотрудника')]").click()
        """

        table = BasePage.Table.get_table_by_name(self, "Перечень лиц, имеющих доступ в помещения")
        BasePage.FormGroup

        table.check_table_have_column("ФИО")
        table.check_table_have_column("ДОЛЖНОСТЬ")
        table.check_table_have_column("ДОПУСК К КРИПТОСРЕДСТВАМ")

        """Поиск"""
        table.check_rows_search("ФИО")
        table.check_rows_search("ДОЛЖНОСТЬ")

        """ФИЛЬТР"""
        table.check_have_not_filtercontrol()

        """Кол-во элементов на странице"""
        table.check_rows_count()

        """Проверка на отсутствие кнопки перемещения"""
        table.check_rows_have_not_reorder()

        """Перемещение"""
        # table.check_rows_replace(count=10)

        """Првоерка выбора записей"""
        table.check_rows_have_select()

        """Ошибка таблицы"""
        table.check_have_errors()

        # """Удаление"""
        # BasePage.all_delete(self)
        # time.sleep(5)

        BasePage.not_next_step(self)

    # allure.bat serve C:\Auto_test\alfadocselenium\tests\test_volkov\reports
    @allure.story('5 ШАГ Перечень помещений и хранилищ')
    @allure.title('Проверка таблицы Перечень помещений')
    def test_step5_1(self):

        with allure.step('Переход на шаг "Перечень помещений"'):
            self.browser.get(self.common_address + "cabinet/main_wizard/#step/rooms_vaults")
            BasePage.ожидание_прогрузки_страницы(self.browser)
            assert True, f'Ошибка при переходе на шаг Перечень Помещений"'

        with allure.step('Поиск таблицы Перечень помещений'):
            table = BasePage.Table.get_table_by_name(self, "Перечень помещений")
            assert True, f'Ошибка при поиске таблицы"Перечень помещений"'
        '''
        with allure.step('Провоерка наличия колонки ПОМЕЩЕНИЯ'):
            table.check_table_have_column("ПОМЕЩЕНИЕ")
            assert True, f'Нет колонки ПОМЕЩЕНИЯ'

        with allure.step('Проверка наличия колонки АДРЕС'):
            table.check_table_have_column("АДРЕС")
            assert True, f'Нет колонки АДРЕС'

        with allure.step('Поиск по колонке ПОМЕЩЕНИЕ'):
            table.check_rows_search("ПОМЕЩЕНИЕ")
            assert True, f'Ошибка при поиске'

        with allure.step('Изменение кол-ва отображаемых элементов на странице'):
            table.check_rows_count()
            assert True, f'Ошибка при изменение кол-ва элементов на странице'

        with allure.step('Перемещеине записей в таблице Перечень помещений'):
            table.check_rows_replace(count=10)
            assert True, f'Ошибка при перемещении записей'

        with allure.step('Проверка возможности выбора записей'):
            table.check_rows_have_select()
            assert True, f'Отсутствует возможность выбора записей таблицы'

        with allure.step('Удаление всех помещений'):
            BasePage.all_delete(self)
            time.sleep(5)
            assert True, f'Ошибка при удалении всех помещений'

        with allure.step('Загрука помещений'):
            name_file = 'cabinet.xls'
            BasePage.file_upload(self, name_file)
            pass

        with allure.step('Выгрузка помещений в Excel'):
            BasePage.file_export(self)
            pass
        '''
        with allure.step('Проверка на наличие возможности изменения порядка записей'):
            table.check_rows_have_reorder()
            assert True, f'Отсутствует возможность изменения порядка записей'

        with allure.step('Проверка на наличие ошибки таблицы'):
            table.check_have_errors()
            assert True, f'Ошибка таблицы присутствует'

    # allure.bat serve C:\Auto_test\alfadocselenium\tests\test_volkov\reports
    @allure.story('5 ШАГ Перечень помещений и хранилищ')
    @allure.title('Проверка таблицы "Перечень хранилищ"')
    def test_step5_2(self):

        with allure.step('Переход на шаг "Перечень помещений"'):
            self.browser.get(self.common_address + "cabinet/main_wizard/#step/rooms_vaults")
            BasePage.ожидание_прогрузки_страницы(self.browser)
            assert True, f'Ошибка при переходе на шаг "Перечень Помещений"'

        with allure.step('Поиск таблицы "Перечень хранилищ"'):
            table = BasePage.Table.get_table_by_name(self, "Перечень хранилищ")
            assert True, f'Ошибка при поиске таблицы "Перечень хранилищ"'

        with allure.step('Проверка наличия колонки УЧЁТНЫЙ НОМЕР"'):
            table.check_table_have_column("УЧЁТНЫЙ НОМЕР")
            assert True, f'Нет колонки УЧЁТНЫЙ НОМЕР"'

        with allure.step('Проверка наличия колонки "НАИМЕНОВАНИЕ ХРАНИЛИЩА (СЕЙФ, МЕТАЛЛИЧЕСКИЙ ШКАФ)"'):
            table.check_table_have_column("НАИМЕНОВАНИЕ ХРАНИЛИЩА (СЕЙФ, МЕТАЛЛИЧЕСКИЙ ШКАФ)")
            assert True, f'Нет колонки "НАИМЕНОВАНИЕ ХРАНИЛИЩА (СЕЙФ, МЕТАЛЛИЧЕСКИЙ ШКАФ)"'

        with allure.step('Проверка наличия колонки "ИНВЕНТАРНЫЙ НОМЕР"'):
            table.check_table_have_column("ИНВЕНТАРНЫЙ НОМЕР")
            assert True, f'Нет колонки "ИНВЕНТАРНЫЙ НОМЕР"'

        with allure.step('Проверка наличия колонки "МЕСТОНАХОЖДЕНИЕ (ПОДРАЗДЕЛЕНИЕ, НОМЕР КОМНАТЫ)"'):
            table.check_table_have_column("МЕСТОНАХОЖДЕНИЕ (ПОДРАЗДЕЛЕНИЕ, НОМЕР КОМНАТЫ)")
            assert True, f'Нет колонки "МЕСТОНАХОЖДЕНИЕ (ПОДРАЗДЕЛЕНИЕ, НОМЕР КОМНАТЫ)"'

        with allure.step('Проверка наличия колонки "ЧТО НАХОДИТСЯ (НАИМЕНОВАНИЕ МАТЕРИАЛЬНЫХ НОСИТЕЛЕЙ)"'):
            table.check_table_have_column("ЧТО НАХОДИТСЯ (НАИМЕНОВАНИЕ МАТЕРИАЛЬНЫХ НОСИТЕЛЕЙ)")
            assert True, f'Нет колонки "ЧТО НАХОДИТСЯ (НАИМЕНОВАНИЕ МАТЕРИАЛЬНЫХ НОСИТЕЛЕЙ)"'

        with allure.step('Проверка наличия колонки "ФАМИЛИЯ ОТВЕТСТВЕННОГО ЗА СЕЙФ (ШКАФ)"'):
            table.check_table_have_column("ФАМИЛИЯ ОТВЕТСТВЕННОГО ЗА СЕЙФ (ШКАФ)")
            assert True, f'Нет колонки "ФАМИЛИЯ ОТВЕТСТВЕННОГО ЗА СЕЙФ (ШКАФ)"'

        with allure.step('Проверка наличия колонки "КОЛИЧЕСТВО КОМПЛЕКТОВ КЛЮЧЕЙ И ИХ НОМЕРА"'):
            table.check_table_have_column("КОЛИЧЕСТВО КОМПЛЕКТОВ КЛЮЧЕЙ И ИХ НОМЕРА")
            assert True, f'Нет колонки "КОЛИЧЕСТВО КОМПЛЕКТОВ КЛЮЧЕЙ И ИХ НОМЕРА"'

        BasePage.ожидание_прогрузки_страницы(self.browser)
        with allure.step('Проверка поиска по колонке "УЧЁТНЫЙ НОМЕР"'):
            table.check_rows_search("УЧЁТНЫЙ НОМЕР")
            assert True, f'Ошибка при поиске по колонке "УЧЁТНЫЙ НОМЕР"'

        BasePage.ожидание_прогрузки_страницы(self.browser)
        with allure.step('Проверка поиска по колонке "НАИМЕНОВАНИЕ ХРАНИЛИЩА (СЕЙФ, МЕТАЛЛИЧЕСКИЙ ШКАФ)"'):
            table.check_rows_search("НАИМЕНОВАНИЕ ХРАНИЛИЩА (СЕЙФ, МЕТАЛЛИЧЕСКИЙ ШКАФ)")
            assert True, f'Ошибка при поиске по колонке "НАИМЕНОВАНИЕ ХРАНИЛИЩА (СЕЙФ, МЕТАЛЛИЧЕСКИЙ ШКАФ)"'

        BasePage.ожидание_прогрузки_страницы(self.browser)
        with allure.step('Проверка поиска по колонке "ИНВЕНТАРНЫЙ НОМЕР"'):
            table.check_rows_search("ИНВЕНТАРНЫЙ НОМЕР")
            assert True, f'Ошибка при поиске по колонке "ИНВЕНТАРНЫЙ НОМЕР"'

        BasePage.ожидание_прогрузки_страницы(self.browser)
        with allure.step('Проверка поиска по клонке "МЕСТОНАХОЖДЕНИЕ (ПОДРАЗДЕЛЕНИЕ, НОМЕР КОМНАТЫ)"'):
            table.check_rows_search("МЕСТОНАХОЖДЕНИЕ (ПОДРАЗДЕЛЕНИЕ, НОМЕР КОМНАТЫ)")
            assert True, f'Ошибка при поиске по колонке "МЕСТОНАХОЖДЕНИЕ (ПОДРАЗДЕЛЕНИЕ, НОМЕР КОМНАТЫ)"'

        BasePage.ожидание_прогрузки_страницы(self.browser)
        with allure.step('Проверка поиска в колонке "ЧТО НАХОДИТСЯ (НАИМЕНОВАНИЕ МАТЕРИАЛЬНЫХ НОСИТЕЛЕЙ)"'):
            table.check_rows_search("ЧТО НАХОДИТСЯ (НАИМЕНОВАНИЕ МАТЕРИАЛЬНЫХ НОСИТЕЛЕЙ)")
            assert True, f'Ошибка при поиске по колонке "ЧТО НАХОДИТСЯ (НАИМЕНОВАНИЕ МАТЕРИАЛЬНЫХ НОСИТЕЛЕЙ)"'

        BasePage.ожидание_прогрузки_страницы(self.browser)
        with allure.step('Проверка поиска по колонке "КОЛИЧЕСТВО КОМПЛЕКТОВ КЛЮЧЕЙ И ИХ НОМЕРА"'):
            table.check_rows_search("КОЛИЧЕСТВО КОМПЛЕКТОВ КЛЮЕЙ И ИХ НОМЕРА")
            assert True, f'Ошибка при поиске по колонке "КОЛИЧЕСТВО КОМПЛЕКТОВ КЛЮЧЕЙ И ИХ НОМЕРА"'
      
        BasePage.ожидание_прогрузки_страницы(self.browser)
        with allure.step('Изменение кол-ва отображаемых элементов на странице'):
            table.check_rows_count()
            assert True, f'Ошибка при изменение кол-ва элементов на странице'
          

        with allure.step('Проверка на наличие возможности изменения порядка записей'):
            table.check_rows_have_reorder()
            assert True, f'Отсутствует возможность изменения порядка записей'
        '''
        with allure.step('Перемещеине записей в таблице Перечень помещений'):
            table.check_rows_replace(count=10)
            assert True, f'Ошибка при перемещении записей'
        '''
        with allure.step('Проверка возможности выбора записей'):
            table.check_rows_have_select()
            assert True, f'Отсутствует возможность выбора записей таблицы'

        with allure.step('Проверка на наличие ошибки таблицы'):
            table.check_have_errors()
            assert True, f'Ошибка таблицы присутствует'
