# Para instalar o selenium rodo o seguinte comando:
pip install selenium

# Para instalar o webdriver rodo
pip install webdriver_manager

# Para encontrar um elemento
navegador.find_element('xpath', 'fullname')
- Para encontrar elementos no navegador preciso de dois parametros o primeiro sempre vai ser o xpath e o segundo vai ser o elemento

# Para instalar canvas
pip install canvas

# Para instalar unicode
pip install unicode

# Para instalar pandas
pip install pandas

# Objetos
Os objetos são os meus atributos, no caso desse projeto é o nome, sobrenome dentre outros campos que precisam ser preenchidos
para fazer o cadastro do usuario

# POs
Utilizo elas de 2 formas tenho as POs filhas e as POs pais

- Filhas:
    Tenho as minhas funções para cada objeto no caso desse projeto usei apenas para fazer as funções de set

- Pais:
    Nas POs pais vou ter as funções que chamam as funções das POs filhas no caso do projeto criei a função cadastro de usuario que chama os set's que estão na PO filha e faz a passagem dos parametros.