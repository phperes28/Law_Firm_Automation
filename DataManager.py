import datetime
from django.utils.encoding import smart_str
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class DataManager:


    def __init__(self, p_number, ultimas_mov):
        self.p_number = p_number
        self.ultimas_mov = ultimas_mov
        self.ultimas_mov_encoded = []
        self.andamentos = []

    def break_line(self):
        try:
            for mov in self.ultimas_mov:
                    andamentos = []
                    andamentos.append(mov.text)
                    self.nova_lista = andamentos[0].split("\n")
                    # print(self.nova_lista)
                    return self.nova_lista
        except NoSuchElementException or StaleElementReferenceException:
            self.andamentos.append(f"Erro ao formatar dados do processo {self.p_number}")



    def format_content(self):
        """formats dates and content extracted from andamentos into datetime format so it can be compared with other dates"""

        self.formated_hour = []
        self.formated_content = []
        self.data_andamento_formatada = []
        self.novos_andamentos = []
        self.andamentos_formated = []

        for andamento in self.nova_lista:

            #FORMAT HOUR
            hora_andamento = andamento.split("-")[1]
            hora_dividida = hora_andamento.split(":")
            hora = int(hora_dividida[0])
            minutos = int(hora_dividida[1])
            segundos = int(hora_dividida[2])

            #Format DATE
            self.data_andamento = andamento.split(" -")[0]
            data_andamento2 = self.data_andamento.split("/")

            self.dia_andamento = int(data_andamento2[0])
            self.mes_andamento = int(data_andamento2[1])
            self.ano_andamento = int(data_andamento2[2])
            data_andamento_formatada = datetime.datetime(self.ano_andamento, self.mes_andamento, self.dia_andamento, hora, minutos, segundos)
            # print(data_andamento_formatada)
            self.data_andamento_formatada.append(data_andamento_formatada)

            #Format Content
            content = andamento.split("-")[2].encode("utf-8", "replace")
            content_encoded = smart_str(content)
            # print(content_encoded)
            self.formated_content.append(content_encoded)
        return self.data_andamento_formatada


    def get_last_date(self):
        just_date = self.nova_lista[0].split("-")
        last_date = just_date[0] + just_date[1]
        return last_date


    def compare_dates(self, last_date):
        num = 0

        for andamento in self.data_andamento_formatada:
            if andamento > last_date:
                self.novos_andamentos.append(self.nova_lista[num])
                print(f"Novo andamento: {self.nova_lista[num]}")
                return True
            num += 1



            #return false otherwise

    def format_andamentos(self):
        num = 0
        for andamento in self.formated_content:
            self.andamentos_formated.append(f"{self.data_andamento_formatada[num].strftime('%d-%b-%Y %H:%M:%S')} {andamento}")
            num += 1
        return self.andamentos_formated








 # def process_info(self):
    #
    #     num = 0
    #     for processo in self.novos_andamentos:
    #         process_info = f"{self.p_number}:\n {self.novos_andamentos[num]}"
    #         num += 1
    #         # print(process_info)




    # def format_hour_content(self):
    #     self.formated_hour = []
    #     self.formated_content = []
    #
    #     for andamento in self.nova_lista:
    #         hora_andamento = andamento.split("-")[1]
    #         self.formated_hour.append(hora_andamento)
    #
    #         content = andamento.split("-")[2]
    #         self.formated_hour.append(content)
    #
    #
    # def format_info(self):
    #
    #     for date in self.data_andamento_formatada:
    #         print(date)


        # RETORNAR INFO DE CADA PROCESSO FORMATADA






