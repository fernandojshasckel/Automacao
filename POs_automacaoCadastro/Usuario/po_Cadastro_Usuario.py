from l_Geral import *

def setNome(driver, nome):
    driver.find_element('xpath', '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').send_keys(nome)

def setSobrenome(driver, sobrenome):
    driver.find_element("xpath", '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').sendKeys(sobrenome)

def setEndereco(driver, endereco):
   driver.find_element("xpath", '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').sendKeys(endereco)

def setEmail(driver, email):
    driver.find_element("xpath", '//*[@id="eid"]/input').sendKeys(email)

def setTelefone(driver, telefone):
    driver.find_element("xpath", '//*[@id="basicBootstrapForm"]/div[4]/div/input').sendKeys(telefone)

def setLinguagem(driver, linguagem):
    driver.find_element("xpath", '//*[@id="msdd"]').sendKeys(linguagem)

def setSenha(driver, senha):
    driver.find_element("xpath", '//*[@id="firstpassword"]').sendKeys(senha)

def setConfirmarSenha(driver, confirmacaoSenha):
    driver.find_element("xpath", '//*[@id="secondpassword"]').sendKeys(confirmacaoSenha)    

def setGenero(driver):
    driver.implicitly_wait(3)
    driver.find_element("name", 'radiooptions').click()

def setHobbies(driver):
    driver.implicitly_wait(3)
    driver.find_element("id", 'checkbox2').click()

def setHabilidade(driver, habilidade):
    driver.implicitly_wait(3)
    driver.find_element("id", 'Skill').click()
    driver.implicitly_wait(3)
    driver.find_element("xpath", '//*[@id="Skills"]/option[12]'.format(habilidade)).click()

def setAnoAniversario(driver, anoAniversario):
    driver.implicitly_wait(3)
    driver.find_element("id", 'yearbox').click()
    driver.implicitly_wait(3)
    driver.find_element("xpath", '//*[@id="yearbox"]/option[88]'.format(anoAniversario)).click()

def setMesAniversario(driver, mesAniversario):
    driver.implicitly_wait(3)
    driver.find_element("xpath", '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select').click()
    driver.implicitly_wait(3)
    driver.find_element("xpath", '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select/option[10]'.format(mesAniversario)).click()

def setDiaAniversario(driver, diaAniversario):
    driver.implicitly_wait(3)
    driver.find_element("xpath", '//*[@id="daybox"]').click()
    driver.implicitly_wait(3)
    driver.find_element("xpath", '//*[@id="daybox"]/option[4]'.format(diaAniversario)).click()