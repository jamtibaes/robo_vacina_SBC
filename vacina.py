import schedule
import smtplib
import config
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = "Subject: {}\n{}".format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_EVERNOTE , message)
        server.quit()
        print("Email Enviado")

    except:
        print("Falha ao enviar o email")


def regex(texto):
    padrao = r"39"

    if not (re.search("^PESSOAS COM COMORBIDADES$", texto)):
        return re.findall(padrao, texto)


def site_prefeitura():

    browser = webdriver.Chrome('C://chromedriver.exe')
    browser.get('https://vacinacovid.saobernardo.sp.gov.br/VacinaSBCProd/servlet/inicial')

    sleep(5)
    #select_box = Select(browser.find_element_by_id('vPUBLICOALVOVACINAID_D1'))
    select_box = Select(browser.find_element_by_id('vPUBLICOALVOVACINAID_D2'))

    for option in select_box.options:
        
        if(regex(option.text)):
            subject = "Vacina"
            msg = 'Chegou a sua vez!!!'
            send_email(subject,msg)

    browser.quit()

schedule.every(1).minutes.do(site_prefeitura)

while True:
    schedule.run_pending()
    sleep(1)
