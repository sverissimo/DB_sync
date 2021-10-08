import requests
from datetime import datetime


def send_mail(host, headers, message):
    # to = 'sandro.verissimo@infraestrutura.mg.gov.br'
    # to = 'sandroverissimo@live.com'
    to = ['sverissimo2@gmail.com', 'sandroverissimo@live.com', 'sandro.verissimo@infraestrutura.mg.gov.br']
    subject = 'New error trying to sync SGTI-CadTI'
    vocativo = 'Dear svom'
    message = str(message)
    footer = str(datetime.now())

    mail = {'to': to, 'subject': subject, 'vocativo': vocativo, 'message': message, 'footer': footer}

    r = requests.post(host + '/sync/notifyError', json=mail, headers=headers)
    print(r.text)
    exit()