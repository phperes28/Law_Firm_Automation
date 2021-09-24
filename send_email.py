from email_creds import MY_PASS, MY_EMAIL
import smtplib


def send_gmail(current_time, processos):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()  #secures connection
        connection.login(user= MY_EMAIL, password= MY_PASS)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= 'pedrodev28@gmail.com',
            msg=f'Subject: Novos andamentos \n\n{processos}'
            )
