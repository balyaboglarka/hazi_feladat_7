from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

DEBUG_MODE = True
URL = 'https://high-flyer.hu/hetihazi/feladat1_teglalap.html'

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

    def test_helyes(self):
        a_old = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'a')))
        b_old = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'b')))
        kalkulal = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'submit')))

        a_old.send_keys("74")
        b_old.send_keys("32")
        kalkulal.click()
        eredm = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@id="result"]'))).text
        assert '212' in eredm

    def test_nem_szamok(self):
        a_old = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'a')))
        b_old = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'b')))
        kalkulal = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'submit')))

        a_old.send_keys("kiskutya")
        b_old.send_keys("32")
        kalkulal.click()
        eredm = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@id="result"]'))).text
        assert 'NaN' in eredm
    def test_ures(self):
        a_old = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'a')))
        b_old = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'b')))
        kalkulal = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'submit')))

        a_old.send_keys(" ")
        b_old.send_keys(" ")
        kalkulal.click()
        eredm = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//span[@id="result"]'))).text
        assert 'NaN' in eredm
