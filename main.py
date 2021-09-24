from TCU_Scraper import TCUScraper
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import time
from send_email import send_gmail
from sheet_manager import SheetManager
from DataManager import DataManager


current_time = time.time()
print("Simbora, carai")

#---------------------------------------------------Google Drive and Sheet Connect-------------------------------------

sheet = SheetManager()
bot = TCUScraper()


#---------------------------------------------------------------------------------------------------------------------
processos= []



# Gets process numbers and pass it to the get_info function to return last updates
column = sheet.get_first_col()
for processo in column[1:]:
    print(processo)
    bot.get_info(processo)

    # Initialize data_manager and calls functions to break lines and formmat date
    try:
        data_m = DataManager(processo, bot.ultimas_mov)
        data_m.break_line()
        data_m.format_content()
        data_m.compare_dates()
        # data_m.process_info()
        processos.append(data_m.to_dict())

    except AttributeError:
        print(f"falha ao buscar informacoes do processo {processo}")


    send_gmail(current_time, processos)



    # data_m.format_hour()
    # data_m.format_content()


    # if data_m.format_dates() > ultima_data_planilha:
    #     data_m.format_dates()


sheet.write_updates(bot.processos_dict)




# send_gmail(bot.andamentos)   MANDAR EMAIL POR ULTIMO



end = time.time()

total_time = (end - current_time) / 60

print(f"Processo concluido em {total_time} minutos")



bot.Andamentos()


# CREATE A DICTIONARY WITH THE DATA WITH PROCESS NUMBER AS KEY AND LAST UPDATE AS VALUE TO SEND AS EMAIL.




#fechar tela no final












