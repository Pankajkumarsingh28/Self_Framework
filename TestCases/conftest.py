import os
import shutil
from datetime import datetime
from pathlib import Path
import pytest
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



#@pytest.hookimpl(tryfirst=True)
#def pytest_configure(config):
    # set custom options only if none are provided from command line
    # if not config.option.htmlpath:
        ##now = datetime.now()
        # create report target dir
        ##reports_dir = Path('Reports', now.strftime('%Y-%m-%d'))
        ##reports_dir.mkdir(parents=True, exist_ok=True)
        # custom report file
        ##report = reports_dir / f"report_{now.strftime('%Y-%m-%d %H:%M:%S')}.html"
        # adjust plugin options
        ##config.option.htmlpath =report
        ##config.option.self_contained_html =True
@pytest.fixture(scope='session')
def cleanup_report():
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        os.chdir("./Reports")
        os.mkdir(timestamp)

        yield

        shutil.move("./tmp_report.html", "./%s/test_report.html" % timestamp)

        fromaddr = "pankajkumarsingh0589@gmail.com"
        toaddr = "pankajkumarsingh28@gmail.com"

        # instance of MIMEMultipart
        msg = MIMEMultipart()

        # storing the senders email address
        msg['From'] = fromaddr

        # storing the receivers email address
        msg['To'] = toaddr

        # storing the subject
        msg['Subject'] = "Subject of the Mail"

        # string to store the body of the mail
        body = "Body_of_the_mail"

        # attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = "Rent.docx" #"C:\Users\nirup\Desktop\Rent.docx"
        attachment = open("C:\\Users\\nirup\\Desktop\\Rent.docx", "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload((attachment).read())

        # encode into base64
        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(fromaddr,"Advocate@3173")

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(fromaddr, toaddr, text)

        # terminating the session
        attachment.close()
        s.quit()

