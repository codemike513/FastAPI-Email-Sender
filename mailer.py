from config import HOST, PORT, USERNAME, PASSWORD, MailBody
from ssl import create_default_context
from email.mime.text import MIMEText
from smtplib import SMTP

def send_main(data:dict|None = None ):
    msg = MailBody(**data)
    message = MIMEText(msg.body, 'html')
    message['From'] = USERNAME
    message['To'] = ", ".join(msg.to)
    message['Subject'] = msg.subject

    ctx = create_default_context()

    try:        
        with SMTP(HOST, PORT) as server:
            server.ehlo()
            server.starttls(context=ctx)
            server.ehlo()
            server.login(USERNAME, PASSWORD)
            server.send_message(message)
            server.quit()
        return {"status": 200, "message": "Mail Sent Successfully"}
    except Exception as e:
        return {"status": 500, "errors": str(e)}