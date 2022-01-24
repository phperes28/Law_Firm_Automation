from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time

WEBSITE = "https://pesquisa.apps.tcu.gov.br/#/pesquisa/processo"


PROCESS_FIELD = '//*[@id="numero_processo"]'
ULTIMA_MOV = '//*[@id="lista-resultado__itens"]/ul/li/div/div[1]/span/ul[2]/li'
TITULO_PROCESSO = '//*[@id="link_resultado_0"]/h3'
ULTIMAS_MOV = '#conteudo_movimentacoes > ul > li:nth-child(1)'

SEGUNDOS = 6


class TCUScraper:

    def __init__(self):
        chrome_driver_path = "E:\Documentos\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.maximize_window()
        self.processos = []
        self.andamentos = []

        self.numero_andamentos = []

        self.action_chains = ActionChains(self.driver)


    def get_info(self, p_number):   #add date from last update on sheet as variable
        """Opens process and gets last update"""
        try:
            self.processos.append(p_number)
            self.driver.get(WEBSITE)
            time.sleep(3)
            processo = self.driver.find_element_by_xpath(PROCESS_FIELD)
            processo.clear()
            processo.send_keys(p_number)
            time.sleep(1)
            processo.submit()
            time.sleep(SEGUNDOS)
            titulo_processo = self.driver.find_element_by_xpath(TITULO_PROCESSO)
            titulo_processo.click()
            time.sleep(6)
            self.ultimas_mov = self.driver.find_elements_by_id("conteudo_movimentacoes")
            return self.ultimas_mov

        except NoSuchElementException or StaleElementReferenceException:
            self.andamentos.append(f"Erro ao buscar ultima atualizacao do processo {p_number}")






            #PEGA MOVIMENTACOES DIVIDE EM ITENS INDIVIDUAIS E ADICIONA A UMA LISTA DE ANDAMENTOS
            # for mov in ultimas_mov:
            #     andamentos = []
            #     lista_andamentos = []
            #     dict_processos = {}
            #     andamentos.append(mov.text)
            #
            #     nova_lista = andamentos[0].split("\n")
            #     ultima_data = nova_lista[0].split(" -")



                # #pega e formata datas. passar para classe
                # for andamento in nova_lista:
                #     data_andamento = andamento.split(" -")[0]
                #     data_andamento2 = data_andamento.split("/")
                #     dia_andamento = int(data_andamento2[0])
                #     mes_andamento = int(data_andamento2[1])
                #     ano_andamento = int(data_andamento2[2])
                #     data_andamento_formatada = datetime.datetime(ano_andamento, mes_andamento, dia_andamento)
                #
                #     #transformar funcao(p_number, ultima atualizacao
                #     if data_andamento_formatada > datetime.datetime(2021,1,1):
                #         print("data maior")
                #         lista_andamentos.append(andamento)
                #         # lista.where() para python
                #
                #         dict_processos[p_number] = lista_andamentos
                #
                #     else:
                #         pass
                #
                # print(dict_processos)


                        #adiciona andamento a lista para
                    # else:
                        #escreve ultima data de andamento




                #FORMATA DATA DE CADA MOVIMENTACAO PARA ELA PODER SER COMPARADA COM A DATA EM QUE O PROGRAMA RODOU PELA ULTIMA VEZ

                # data = ultima_data[0]
                # # print(nova_lista)
                # calendar = data.split("/")
                # day = int(calendar[0])
                # month = int(calendar[1])
                # year = int(calendar[2])
                #
                # ultima_data_formatada = datetime.datetime(year, month, day)
                # date2 = datetime.datetime(1989, 5,28)
                #
                #
                # if ultima_data_formatada > date2:
                #     print("data maior")

                # for item in nova_lista:
                #      if item.split(" -")[0] > data:
                #          print("cu")
                #         #identificar a atualizacao nova e adicionar ela em uma lista pra enviar por email



            #pega movs do processo e cria dicionario com numero de processo como key e lista de processos como value
            # try:
            #     #append content of the div to a list and splits into bigger list
            #     for mov in ultimas_mov:
            #
            #         self.lista_andamentos.append(mov.text)
            #
            #     self.processos_dict = dict(zip(self.processos, self.lista_andamentos))
            #     print(len(self.lista_andamentos))
            #     # print(self.processos_dict)
            #     print(self.processos_dict)


            #     #USAR SPLIT SOMENTE NA HORA DE ESCREVER
            #
            # except IndexError:
            #     print(f"Falha ao pesquisar processo {p_number}")
            #     self.numero_andamentos.append(0)




            # ultima_mov = self.driver.find_element_by_xpath(ULTIMA_MOV).text
            # self.andamentos.append(ultima_mov)
            # print(ultima_mov)
            # time.sleep(3)




# Comparar len de cada lista de andamentos. se valor for igual nao houveram novos andamentos. se valor for diferente novos andamentos realizados
# quantidade de novos andamentos = len(nova) - len(antiga)





