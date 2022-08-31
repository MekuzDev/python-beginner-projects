from base64 import encode
import email
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import smtplib,ssl
import pathlib 


# Loads available enviroment variables
load_dotenv()

# contruct your message 
message = MIMEMultipart('alternative')
message['subject'] = "The advice from a python developer"
message['from'] =os.getenv('SENDER_MAIL')
message['to'] ="markonuoha6@gmail.com"
message['Bcc'] = "markonuoha6@gmail.com"    

filename = pathlib.Path('full_python_tutorial.pdf')

with open('full_python_tutorial.pdf','r+b') as attachment:
    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Alumni+Sans+Pinstripe&display=swap" rel="stylesheet">
    <title>Mail Body</title>
    <style>
        *{
            
        }
        body{
            font-family: 'Alumni Sans Pinstripe', Arial;
            margin: 0;
            height: 100vh;
            padding: relative;
            background-color: rgba(50, 79, 79, 0.535);
        }
        .mail-header{
            background-color: rgb(17, 17, 52);
            color:#fff;
            font-weight: 700;
            text-align: center;
            margin: 0;
            padding: 20px;
        }
    
        .mail-body {
            width: 90%;
            margin: 0 auto;
            text-align: center;
            padding: 2rem;
        }
    
        .mail-body p{
           width: 500px;
           font-size: 1rem;
           font-weight: bolder;
           margin: 0 auto;
        }
    
        .mail-button{
            padding: 1rem 2rem;
            font-weight: bold;
            font-size: 1.1rem;
            background-color: orangered;
            color:#fff;
            cursor: pointer;
        }
    
        footer{
    
            display: flex;
            justify-content: space-between;
            padding: 20px;
            background-color: rgb(17, 17, 52);
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
    
        }
    
        footer .right ul{
            display: flex;
            list-style: none;
        }
        footer .right ul li a{
            text-decoration: none;
            color: #fff;
        }
        footer .left{
            color:#fff;
        }
        .thanks{
            text-decoration: underline;
            font-weight: bolder;
        }
    </style>
</head>

<body>
    <main>
        <header>
            <div class="mail-header">
                <h1>Get updates from inspiri-tech</h1>
            </div>
        </header>
        <section class="mail-body">
                <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eum aliquid in nostrum distinctio temporibus facere voluptatem. Ipsa nobis ad sunt, obcaecati tenetur modi quas. Placeat autem neque obcaecati natus ullam enim temporibus beatae. Minima reiciendis minus nisi expedita cupiditate debitis ipsam, nam nemo. Delectus repellat temporibus quisquam cumque tempore alias?</p>
            <h2 class="thanks">Thanks for subscribing to our newsletter</h2>
            <button class="mail-button">Confirm Account</button>
            <h2>see attached documents below</h2>
        </section>

        <footer>
            <div class="left">
                <p>Copyright &copy; inspiri-tech 2022</p>
            </div>
            <div class="right">
                <ul>
                    <li><a href="#">unsuscribe from our newsletter</a></li>
                    
                </ul>
            </div>
        </footer>
    </main>
</body>
</html>
"""
plain_text = MIMEText(text,'plain')
html_format = MIMEText(html,'html')

message.attach(plain_text)
message.attach(html_format)
message.attach(part)




# Creation of a secure SSL context
context = ssl.create_default_context()

# Establishing connection to smtp server to login
with smtplib.SMTP_SSL(os.getenv('SMTP_HOST'),os.getenv('SSL_PORT'),context=context) as server:
    server.login(os.getenv('SENDER_MAIL'),os.getenv('SENDER_PASSWORD'))
    server.sendmail('thepythondev@examplemail.com','markonuoha6@gmail.com',message.as_string())