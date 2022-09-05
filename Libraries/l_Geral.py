from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A2
from datetime import datetime, timedelta
import os
import pandas as pd
from unidecode import unidecode
import time


# Altera o valor do campo conforme o xpath passado
def alteraValorCampo_xpath(driver, xpathCampo, valor):
    driver.find_element("xpath", xpathCampo).click()
    driver.find_element("xpath", xpathCampo).send_keys(Keys.CONTROL + "a")
    driver.find_element("xpath", xpathCampo).send_keys(Keys.DELETE)
    driver.find_element("xpath", xpathCampo).send_keys(Keys.BACKSPACE)
    driver.find_element("xpath", xpathCampo).send_keys(valor)


# Altera o valor do campo conforme o name passado
def alteraValorCampo_name(driver, nameCampo, valor):
    driver.find_element("name", nameCampo).click()
    driver.find_element("name", nameCampo).send_keys(Keys.CONTROL + "a")
    driver.find_element("name", nameCampo).send_keys(Keys.DELETE)
    driver.find_element("name", nameCampo).send_keys(Keys.BACKSPACE)
    driver.find_element("name", nameCampo).send_keys(valor)


# Altera o valor do campo conforme o id passado
def alteraValorCampo_id(driver, idCampo, valor):
    driver.find_element("id", idCampo).click()
    driver.find_element("id", idCampo).send_keys(Keys.CONTROL + "a")
    driver.find_element("id", idCampo).send_keys(Keys.DELETE)
    driver.find_element("id", idCampo).send_keys(valor)


# Tratamento para gerar logs de erro gravados na pasta C:\CISS\LogsAutomacaoWeb
def geraLogErro(driver, erro):
    data = datetime.now().strftime('%d-%m-%Y')

    try:
        os.makedirs("C:\CISS\LogsAutomacaoWeb")
    except:
        print("Pasta C:\CISS\LogsAutomacaoWeb já criada")

    try:
        os.makedirs("C:\CISS\LogsAutomacaoWeb\{0}".format(data))
    except:
        print("Pasta C:\CISS\LogsAutomacaoWeb\{0} já criada".format(data))

    erro = erro.replace("\t", " ")
    erro = erro.replace('"selector":', '"selector":\n')
    erro = erro.replace('Message:', 'Message:\n')
    erro = erro.split("\n")

    hora = datetime.now().strftime('%H-%M-%S')
    time.sleep(2)
    driver.save_screenshot(hora + ".png")
    cnv = canvas.Canvas(
        "C:\CISS\LogsAutomacaoWeb\{0}\{1}.pdf".format(data, hora), pagesize=A2)
    cnv.drawImage(hora + ".png", 88, 850, 1024, 768)

    cont = 750

    for val in erro:
        cnv.drawString(20, cont, val)
        cont = cont - 15

    cnv.save()
    os.remove(hora + ".png")
    driver.quit()


def getValorTabelaXls(plataforma, campoProcurar):
    tabela = pd.read_excel("G:/Drives compartilhados/Novas Tecnologias/Acessos Equipe Novas Tecnologias.xlsx")

    try:
        for i in range(tabela.__len__()):
            if((tabela["Campos"][i]) == plataforma):
                x = i - 1
                while x < tabela.__len__():
                    x = x + 1
                    if((tabela["Campos"][x]) == campoProcurar):
                        return(tabela["Valores"][x])
                        break
    except Exception:
        return("Não encontrou os dados na tabela !")


def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element("xpath", xpath)
    except NoSuchElementException:
        return False
    return True


def validaMsgClickSim(driver, msgCorreta, xpathDaMsg):
    time.sleep(2)
    driver.implicitly_wait(5)    
    msgRetorno = driver.find_element("xpath", xpathDaMsg)
    msgRetorno = msgRetorno.text
    msgRetorno_formatada = unidecode(msgRetorno).lower().strip()
    msgCorreta_formatada = unidecode(msgCorreta).lower().strip()

    if msgCorreta_formatada == msgRetorno_formatada:
        driver.implicitly_wait(3)
        driver.find_element("xpath", "//span[normalize-space()='Sim']").click()
    else:
        raise RuntimeError(
            "Deveria apresentar: {0}\nApresentou: {1}".format(msgCorreta_formatada, msgRetorno_formatada))



def waitNotExist_Xpath(driver, xpath, tempo):    
    tempo = timedelta(seconds = tempo)
    tempo = datetime.now() + tempo    
    tempo = tempo.strftime('%H:%M:%S')
    timeNow = datetime.now().strftime('%H:%M:%S')
    while(True):
        if (timeNow > tempo):
            raise RuntimeError(
                "Xpath passado demorou muito para desaparecer.")
            break
        timeNow = datetime.now().strftime('%H:%M:%S')
        if check_exists_by_xpath(driver, xpath) == False:
            break