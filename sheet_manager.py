import gspread
from oauth2client.service_account import ServiceAccountCredentials

import time
import datetime

#Gets Current date and time
date = datetime.datetime.now()
current_day = date.strftime("%H:%M %d/%m/%Y")
print(current_day)

# Shit to hook up to the Google drive and Google sheet with creds file from google

scope =["https://spreadsheets.google.com/feeds",
        'https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Processos").sheet1


class SheetManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.scope = scope
        self.creds = creds
        self.client = client
        self.client = sheet
        self.destination_data = {}

    def get_records(self):
        data = sheet.get_all_records()
        return data

    def get_row(self, row_num):
       row = sheet.row_values(row_num)
       return row

    def get_first_col(self):
        column = sheet.col_values(1)
        return column


    def get_cell(self,row,col):
        cell = sheet.cell(row, col).value
        return cell

    def insert(self):
        row = ["I'm","inserting","a","row","into","a,","Spreadsheet","with","Python"]
        index = 13
        sheet.insert_row(row, index)

    def write_updates(self, andamentos):
        row_num = 2
        for value in andamentos:
            if value == sheet.cell(row_num, 2).value:
                sheet.update_cell(row_num,3, f"Sem novas atualizacoes para o processo em {current_day}")
                print("sem nova atualizacao para processo ")
                row_num = row_num +1
                time.sleep(3)

            else:
                #TODO FAZER ESCREVER ANDAMENTOS: VALUES DO DICTIONARY CRIADO SELF.DICT_ANDAMENTOS
                sheet.update_cell(row_num, 2, value) # has to target value to write not key
                sheet.update_cell(row_num,3, f"Nova atualizacao detectada em {current_day}")
                row_num = row_num +1
                print(row_num)
                time.sleep(3)


    def get_date(self):
        row_num = 2

