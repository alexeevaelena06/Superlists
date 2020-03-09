from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""
    def setUp(self):
        """установка"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """демонтаж"""
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """Подтверждение строки в таблице списка"""
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Тест: можно начать список и получить его позже"""
        # Эдит слышала про крутое новое онлайн-приложение со списком неотложных дел. Она желает оценить его домашнюю
        # страницу
        self.browser.get("http://localhost:8000")

        # Она видит, что заголовок и шапка страницы говорят о списках неотложных дел
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        # self.fail("Закончить тест!")

        # Ей сразу же предлагается ввести элемент списка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # Она набирает в текстовом поле "Купить павлиньи перья" (её хобби - вязанье рыболовных мушек)
        inputbox.send_keys('Купить павлиньи перья')

        # Когда она нажимает enter, страница обновляется, и теперь страница содержит "1: Купить павлинь перья" в
        # качестве элемента списка.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)
        self.check_for_row_in_list_table('1: Купить павлиньи перья')

        # Текстовое поле по-прежнему приглашает ее добавить ещё один элемент.
        # Она вводит "Cделать мушку из павлиньих перьев" (Эдит очень методична)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Сделать мушку из павлиньих перьев')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)
        # Страница снова обновляется, и теперь показывает оба элемента её списка
        self.check_for_row_in_list_table('1: Купить павлиньи перья')
        self.check_for_row_in_list_table('2: Сделать мушку из павлиньих перьев')
        # Эдит интересно, запомнит ли сайт её список. Далее она видит, что сайт сгенерировал для неё уникальный URL
        # адрес - об этом выводится небольшой текст с объяснениями.
        # Она посещает URL-адрес - её список по-прежнему там.
        self.fail('Закончить тест!')

    # Удовлетворенная, она  снова ложиться спать.
    if __name__ == '__main__':
        unittest.main(warnings='ignore')
