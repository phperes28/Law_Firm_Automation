from email.message import EmailMessage
from email_creds import MY_PASS, MY_EMAIL
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_gmail2():
    msg = EmailMessage()
    msg["Subject"] = "Novos Andamentos"
    msg["From"] = "EHJC Advogados"
    msg["To"] = "pedrodev28@gmail.com"

    with open("andamentos.txt", "rb") as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data, maintype="application", subtype="txt",filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

        server.login(user= MY_EMAIL, password= MY_PASS)
        server.send_message(msg)


def send_email(processos):

    msg = MIMEMultipart("alternative")

    msg['from'] = "pedro.tramit@gmail.com"
    msg['to'] = "pedrodev28@gmail.com"		# Target's Email
    msg['subject'] = 'Novos Andamentos'
    part1 = MIMEText(u'\u3053\u3093\u306b\u3061\u306f\u3001\u4e16\u754c\uff01\n',
             "plain",)
    msg.attach(part1)
    print('Sending the Mail..')
    try:
        print(f"Imprimindo processos passados pra send_email {processos}")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("pedro.tramit@gmail.com", os.getenv("PASSWORD"))

        mensagem = f'Novos andamentos: {processos}'.encode("utf-8")
        server.sendmail(from_addr="pedro.tramit@gmail.com",
                        to_addrs="pedrodev28@gmail.com",
                        msg=mensagem,

                        mail_options="SMTPUTF8"
                        )

        server.quit()
        print(mensagem)
        print("Sua mensagem foi enviada!")


    except Exception as e :
        print('Erro ao enviar mensagem')
        print(e)
        print(os.getenv("PASSWORD"))
        # print(os.environ)
