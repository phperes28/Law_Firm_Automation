from TCU_Scraper import TCUScraper
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import time
from send_email import send_gmail
from sheet_manager import DataManager

start = time.time()
print("Hello, let's begin")

#---------------------------------------------------Google Drive and Sheet Connect-------------------------------------

sheet = DataManager()
bot = TCUScraper()
#---------------------------------------------------------------------------------------------------------------------

# Gets process numbers and pass it to the get_info function to return last updates
column = sheet.get_first_col()
for processo in column[1:]:
    print(processo)

    bot.get_info(processo)


sheet.write_updates(bot.andamentos)




# send_gmail(bot.andamentos)   MANDAR EMAIL POR ULTIMO



end = time.time()

total_time = (end-start)/60

print(f"Processo concluido em {total_time} minutos")



# CREATE A DICTIONARY WITH THE DATA WITH PROCESS NUMBER AS KEY AND LAST UPDATE AS VALUE TO SEND AS EMAIL.




#fechar tela no final












