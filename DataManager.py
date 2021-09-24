import datetime


class DataManager:

    def __init__(self, p_number, ultimas_mov):
        self.p_number = p_number
        self.ultimas_mov = ultimas_mov
        self.andamentos = []

    def break_line(self):
        for mov in self.ultimas_mov:
                andamentos = []
                andamentos.append(mov.text)
                self.nova_lista = andamentos[0].split("\n")
                # print(self.nova_lista)
                return self.nova_lista



    def format_content(self):
        """formats dates and content extracted from andamentos into datetime format so it can be compared with other dates"""

        self.formated_hour = []
        self.formated_content = []
        self.data_andamento_formatada = []
        self.novos_andamentos = []
        self.andamentos_dict = {}

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
            #TODO ENCODE TO UTF-8 TO SEND VIA EMAIL
            content = andamento.split("-")[2]
            self.formated_content.append(content)

        # print(self.data_andamento_formatada)
        return self.data_andamento_formatada


#TODO COLLECT DATE FROM SHEET, TURN INTO DATETIME OBJECT AND PASS IT TO FUNCTION AS ARGUMENT FOR COMPARISON
    def compare_dates(self):
        num = 0
        for andamento in self.data_andamento_formatada:
            if andamento > datetime.datetime(2010, 12, 10, 14, 35, 16):
                self.novos_andamentos.append(self.nova_lista[num])
            else:
                pass
            num += 1



    def process_info(self):
        num = 0
        for processo in self.novos_andamentos:
            process_info = f"{self.p_number}:\n {self.novos_andamentos[num]}"
            num += 1
            # print(process_info)

    def to_dict(self):
        self.andamentos_dict[self.p_number] = self.novos_andamentos
        # print(self.andamentos_dict)
        return self.andamentos_dict







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






