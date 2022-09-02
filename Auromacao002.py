from tkinter.tix import Select
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
import time 

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.maximize_window()

# Abrindo a pag
navegador.get('https://demo.automationtesting.in/Register.html')

navegador.find_element('xpath', '//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').send_keys('Fernando')
navegador.find_element('xpath', '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys('Hasckel')
navegador.find_element('xpath', '//*[@id="basicBootstrapForm"]/div[2]/div/textarea').send_keys('Rua Getulio Vargas N°33')
navegador.find_element('xpath', '//*[@id="eid"]/input').send_keys('fernando.hasckel@gmail.com')
navegador.find_element('xpath', '//*[@id="basicBootstrapForm"]/div[4]/div/input').send_keys('9992213131')
navegador.find_element('xpath', '//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()
navegador.find_element('xpath', '//*[@id="checkbox2"]').click()
navegador.find_element('xpath', '//*[@id="Skills"]').click()
navegador.find_element('xpath', '//*[@id="Skills"]/option[11]').click()
navegador.find_element('xpath', '//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span').click()
navegador.find_element('xpath', '/html/body/span/span/span[1]/input').send_keys('Japan')
navegador.find_element('xpath', '//*[@id="country"]/option[7]').click()
navegador.find_element('xpath', '//*[@id="yearbox"]').click()
navegador.find_element('xpath', '//*[@id="yearbox"]/option[88]').click()
navegador.find_element('xpath', '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select').click()
navegador.find_element('xpath', '//*[@id="basicBootstrapForm"]/div[11]/div[2]/select/option[10]').click()
navegador.find_element('xpath', '//*[@id="daybox"]').click()
navegador.find_element('xpath', '//*[@id="daybox"]/option[4]').click()
navegador.find_element('xpath', '//*[@id="firstpassword"]').send_keys('teste@123')
navegador.find_element('xpath', '//*[@id="secondpassword"]').send_keys('teste@123')
navegador.find_element('xpath', '//*[@id="submitbtn"]').click()

time.sleep(6000)