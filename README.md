# Para instalar o selenium rodo o seguinte comando:
pip install selenium

# Para instalar o webdriver rodo
pip install webdriver_manager

# Para encontrar um elemento
navegador.find_element('xpath', 'fullname')
- Para encontrar elementos no navegador preciso de dois parametros o primeiro sempre vai ser o xpath e o segundo vai ser o elemento

# Manipulando elementos

.click() - Clicar no elemento
nome = navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').click()

.send_keys() - Funciona como um set
nome = navegador.find_element('xpath', '//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys()