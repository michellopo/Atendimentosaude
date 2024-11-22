
from connect import *
meucursor = banco.cursor()





def cadastrar(nome,cpf,ano_nascimento,peso,altura,telefone,endereco,cep):


        sql = "INSERT INTO Pacientes (Nome, CPF, Idade, Peso, Altura, Telefone, Endereco, CEP) VALUES (%, %, %, %, %, %, %, %)"
        data = (nome,cpf,ano_nascimento,peso,altura,telefone,endereco,cep)
        meucursor.execute(sql,data)
        banco.commit()
