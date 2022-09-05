# Selenium e WebDriver

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Para baixar o webdriver 
servico = Service(ChromeDriverManager().install())

# Abrindo o navegador
navegador = webdriver.Chrome(service=servico)

# Passo 1: Abrir um pagina de formulario

# Abre o navegador para dai entrar no link
navegador.maximize_window()

navegador.get('https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M')

# Passo 2: Preencher nome, preencher e-mail

# Para encontrar um elemento
navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys('Fernando')

navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[2]/div/input').send_keys('fernandojosehasckel@gmail.com')

navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/button').click()

time.sleep(6000)

# Passo 3: Clicar no botão para enviar formulario