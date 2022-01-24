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
        self.date = []
        self.row_num = 2
        self.col_num = 2

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


    def write_updates(self, andamentos):
        row_num = 2
        for value in andamentos:
            if value == sheet.cell(row_num, 2).value:
                sheet.update_cell(row_num,3, f"Sem novas atualizacoes para o processo em {current_day}")
                print("sem nova atualizacao para processo ")
                row_num = row_num +1
                time.sleep(3)

            else:

                sheet.update_cell(row_num, 2, value) # has to target value to write not key
                sheet.update_cell(row_num,3, f"Nova atualizacao detectada em {current_day}")
                row_num = row_num +1
                print(row_num)
                time.sleep(3)


    def get_date(self):

        cell = sheet.cell(self.row_num, self.col_num).value
        self.row_num += 1
        try:
            datetime_date = datetime.datetime.strptime(cell, "%d/%m/%Y %H:%M:%S")
        except ValueError:
            datetime_date = datetime.datetime.strptime(cell, "%d/%m/%Y %H:%M:%S")
        except TypeError:
            pass
            #if Null, must get last update date and write it to sheet
        return datetime_date


    def write_date(self, last_date,row_num):
        sheet.update_cell(row_num, 2, last_date)


    def get_cell_num(self,p_number):
        cell = sheet.find(p_number)
        cell_row = cell.row
        return cell_row




        #TODO- WRITE DATE OF LAST ANDAMENTO ON SHEET

