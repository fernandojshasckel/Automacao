class o_Usuario:
    def __init__(self):
        self.nome = ''
        self.sobrenome = ''
        self.endereco = ''
        self.email = ''
        self.telefone = ''
        self.genero = ''
        self.hobbies = ''
        self.linguagem = ''
        self.habilidade = ''
        self.estado = ''
        self.pais = ''
        self.diaAniversario = ''
        self.mesAniversario = ''
        self.anoAniversario = ''
        self.senha = ''
        self.confirmacaoSenha = ''

    @property
    def nome(self):
        return self.nome 

    @nome.setter
    def nome(self, nome):
        self.nome = nome 
    
    @property
    def sobrenome(self):
        return self.sobrenome 

    @sobrenome.setter 
    def sobrenome(self, sobrenome):
        self.sobrenome = sobrenome 

    @property 
    def endereco(self):
        return self.endereco

    @endereco.setter 
    def endereco(self, endereco):
        self.endereco = endereco 

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.email = email

    @property
    def telefone(self):
        return self.telefone

    @telefone.setter
    def telefone(self, telefone):
        self.telefone = telefone

    @property
    def genero(self):
        return self.genero

    @genero.setter
    def genero(self, genero):
        self.genero = genero 

    @property
    def hobbies(self):
        return self.hobbies

    @hobbies.setter
    def hobbies(self, hobbies):
        self.hobbies = hobbies

    @property
    def linguagem(self):
        return self.linguagem

    @linguagem.setter
    def linguagem(self, linguagem):
        self.linguagem = linguagem

    @property
    def habilidade(self):
        return self.habilidade

    @habilidade.setter
    def habilidade(self, habilidade):
        self.habilidade = habilidade

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estado):
        self.estado = estado

    @property
    def pais(self):
        return self.pais

    @pais.setter
    def pais(self, pais):
        self.pais = pais

    @property
    def diaAniversario(self):
        return self.diaAniversario

    @diaAniversario.setter
    def diaAniversarioa(self, diaAniversario):
        self.diaAniversario = diaAniversario

    @property
    def mesAniversario(self):
        return self.mesAniversario

    @mesAniversario.setter
    def mesAniversario(self, mesAniversario):
        self.mesAniversario = mesAniversario

    @property
    def anoAniversario(self):
        return self.anoAniversario

    @anoAniversario.setter
    def anoAniversario(self, anoAniversario):
        self.anoAniversario = anoAniversario

    @property
    def senha(self):
        return self.senha
    
    @senha.setter
    def senha(self, senha):
        self.senha = senha

    @property
    def confirmacaoSenha(self):
        return self.confirmacaoSenha

    @confirmacaoSenha.setter
    def confirmacaoSenha(self, confirmacaoSenha):
        self.confirmacaoSenha = confirmacaoSenha