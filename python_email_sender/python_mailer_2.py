from http import server
import os,smtplib,ssl
from dotenv import load_dotenv
load_dotenv()

context = ssl.create_default_context()
try:
    server = smtplib.SMTP(os.getenv('SMTP_HOST'),os.getenv('TLS_PORT'))
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(os.getenv('SENDER_MAIL'),os.getenv('SENDER_PASSWORD'))
    server.sendmail('thepythondev@examplemail.com','markonuoha97@gmail.com','always study to attain greater heights')
except Exception as e:
    print(e)
finally:
    server.quit()

