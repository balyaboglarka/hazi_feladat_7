from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

DEBUG_MODE = True
URL = 'https://high-flyer.hu/hetihazi/feladat2_email.html'

class TestTC(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        options.add_argument('--headless')
        self.browser.maximize_window()
        self.browser.get(URL)

    def teardown_method(self):
       self.browser.quit()

    def test_helytelen(self):
        mezo = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'email')))
        submit = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'submit')))
        mezo.send_keys('teszt@')
        submit.click()
        danger_m = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'validation-error'))).text
        assert 'cím nem teljes' in danger_m
    def test_ures(self):
        mezo = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'email')))
        submit = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'submit')))
        mezo.send_keys(" ")
        submit.click()
        danger_m = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'validation-error'))).text
        assert 'töltse' in danger_m
    def test_helyes(self):
        mezo = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'email')))
        submit = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'submit')))
        mezo.send_keys("teszt@elek.hu")
        submit.click()
        assert submit.is_enabled()
