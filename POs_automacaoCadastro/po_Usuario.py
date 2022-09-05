import traceback
from l_Geral import *
from POs_automacaoCadastro.Usuario.po_Cadastro_Usuario import *

def cadastroUsuario(driver, nome, sobrenome, endereco, email, telefone, genero, hobbies, linguagem, habilidade, 
                        diaAniversario, mesAniversario, anoAniversario, senha, confirmacaoSenha):
    try:
        setNome(driver, nome)
        setSobrenome(driver, sobrenome)
        setEndereco(driver, endereco)
        setEmail(driver, email)
        setTelefone(driver, telefone)
        setGenero(driver, genero)
        setHobbies(driver, hobbies)
        setLinguagem(driver, linguagem)
        setHabilidade(driver, habilidade)
        setAnoAniversario(driver, anoAniversario)
        setMesAniversario(driver, mesAniversario)
        setDiaAniversario(driver, diaAniversario)
        setSenha(driver, senha)
        setConfirmarSenha(driver, confirmacaoSenha)
        
    except Exception:
        geraLogErro(driver, traceback.format_exc())