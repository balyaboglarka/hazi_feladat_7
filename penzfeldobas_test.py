from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

DEBUG_MODE = True
URL = 'https://high-flyer.hu/hetihazi/feladat3_penzfeldobas.html'

class TestTC(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options)
        self.browser.maximize_window()
        self.browser.get(URL)

    def teardown_method(self):
        self.browser.quit()

    def test_tc1(self):
        penzfeldobas = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.ID, 'submit')))
        for pf in range(100):
            penzfeldobas.click()
        eredm = WebDriverWait(self.browser, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//ul[@id="results"]//li')))
        szoveg = []
        for ered in eredm:
            szoveg.append(ered.text)
        assert "fej" in szoveg
        print(szoveg)
        from collections import Counter
        c = Counter(szoveg)
        print(c['fej'])
        assert (szoveg.count("fej")) >= 30











