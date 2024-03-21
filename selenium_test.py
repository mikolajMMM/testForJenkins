from selenium import webdriver
import unittest


class HerokuAppTest(unittest.TestCase):
    def setUp(self):
        # Inicjalizacja przeglądarki
        self.driver = webdriver.Chrome()

    def test_login_page(self):
        driver = self.driver
        # Otwórz stronę Heroku
        driver.get("https://the-internet.herokuapp.com/login")

        # Sprawdź tytuł strony
        self.assertIn("The Internet", driver.title)

        # Znajdź pole do wprowadzenia loginu i hasła
        username_field = driver.find_element_by_id("username")
        password_field = driver.find_element_by_id("password")

        # Wprowadź dane logowania
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")

        # Znajdź i kliknij przycisk "Login"
        login_button = driver.find_element_by_css_selector("button[type='submit']")
        login_button.click()

        # Sprawdź, czy zalogowanie się powiodło
        success_message = driver.find_element_by_css_selector(".flash.success")
        self.assertTrue(success_message.is_displayed())

        # Zapisz wynik testu do pliku txt
        with open("test_result.txt", "w") as file:
            file.write("Test przebiegł pomyślnie.")

    def tearDown(self):
        # Zamknij przeglądarkę po zakończeniu testu
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
