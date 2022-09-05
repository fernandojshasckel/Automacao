import webbrowser
from objects.o_Usuario import o_Usuario
from POs_automacaoCadastro.Usuario.po_Cadastro_Usuario import *
from POs_automacaoCadastro.po_Usuario import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriver
from selenium import webdriver

servico = Service(ChromeDriver().install())
driver = webdriver.Chrome(service=servico)

obj_Usuario = o_Usuario
obj_Usuario.nome = 'Fernando'
obj_Usuario.sobrenome = 'Hasckel'
obj_Usuario.endereco = 'R. Tiburcio Never N°1212'
obj_Usuario.email = 'fernando.hasckel@gmail.com'
obj_Usuario.telefone = '9990000000'
obj_Usuario.genero = ''
obj_Usuario.hobbies = ''
obj_Usuario.linguagem = ''
obj_Usuario.habilidade = ''
obj_Usuario.anoAniversario = ''
obj_Usuario.mesAniversario = ''
obj_Usuario.diaAniversario = ''
obj_Usuario.senha = 'fernando@123'
obj_Usuario.confirmacaoSenha = 'fernando@123'