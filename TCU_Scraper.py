from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import time



WEBSITE = "https://pesquisa.apps.tcu.gov.br/#/pesquisa/processo"


PROCESS_FIELD = '//*[@id="numero_processo"]'
ULTIMA_MOV = '//*[@id="lista-resultado__itens"]/ul/li/div/div[1]/span/ul[2]/li'



class TCUScraper:

    def __init__(self):
        chrome_driver_path = "E:\Documentos\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.maximize_window()
        self.processos = []
        self.andamentos = []
        self.action_chains = ActionChains(self.driver)


    def get_info(self, p_number):
        """Opens process and gets last update"""
        try:
            self.driver.get(WEBSITE)
            time.sleep(3)
            processo = self.driver.find_element_by_xpath(PROCESS_FIELD)
            processo.clear()
            processo.send_keys(p_number)
            time.sleep(2)
            processo.submit()
            time.sleep(4)
            ultima_mov = self.driver.find_element_by_xpath(ULTIMA_MOV).text
            self.andamentos.append(ultima_mov)
            print(ultima_mov)
            time.sleep(3)

        except NoSuchElementException:
            self.andamentos.append(f"Erro ao buscar ultima atualizacao do processo {p_number}")





