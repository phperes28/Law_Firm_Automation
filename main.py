from TCU_Scraper import TCUScraper
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import time
from send_email import send_gmail2, send_email
from sheet_manager import SheetManager
from DataManager import DataManager
from File_Manager import FileManager


current_time = time.time()
print("Simbora, carai")



sheet = SheetManager()
bot = TCUScraper()

processos= []
p_number = []

#criar dicionario onde numero do processo eh key e lista de andamento value

# Gets process numbers and pass it to the get_info function to return last updates
column = sheet.get_first_col()
for processo in column[1:]:
    print(processo)
    p_number.append(processo)
    bot.get_info(processo)
    #write all info on sheet



    # Initialize data_manager and calls functions to break lines and formmat date
    try:
        data_m = DataManager(processo, bot.ultimas_mov)
        data_m.break_line()
        data_m.format_content()

    #Get date from sheet and compare with new dates, if new update write nem date to sheet
        if data_m.compare_dates(sheet.get_date()) == True:
            sheet.write_date(data_m.get_last_date(), sheet.get_cell_num(processo))
            processos.append(data_m.format_andamentos())
            #ver se so os processos com data maior esta sendo adicionados
            try:
                novo_dict = zip(p_number, processos)
                processo_com_andamento = dict(novo_dict)
                print(processo_com_andamento)
                send_email(processo_com_andamento)
            except:
                pass




    except AttributeError:
        print(f"falha ao buscar informacoes do processo {processo}")



#----------------------------------------Writes info to TXT Documento-------------------------------------#

# file_manager = FileManager(processos, p_number)
# file_manager.write_info()
# send_gmail2()





end = time.time()

total_time = (end - current_time) / 60

print(f"Processo concluido em {total_time} minutos")


















