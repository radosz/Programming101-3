import smtplib
import json


class MailSender:

    def __init__(self, filename):
        param = MailSender.load_config_file(filename)
        self.fromaddr = param["from"]
        self.to = param["to"]
        self.user = param["username"]
        self.username = param["username"]
        self.password = param["password"]
        self.server = param["server"]

    @staticmethod
    def load_config_file(filename):
        with open(filename, "r") as mail:
            jso_f = json.load(mail)
        mail.close()
        return jso_f

    def mail_send(self, subject, txt):
        fromaddr = self.fromaddr
        toaddrs = self.to
        msg = 'Subject: %s\n\n%s' % (subject, txt)
        username = self.user
        password = self.password
        server = smtplib.SMTP(self.server)
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
