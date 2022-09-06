# Escreva uma classe “PessoaFisica” e herde Pessoa, crie um método exclusivo para a classe e acesse-o.

class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
       
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def get_cpf(self):
        return self.cpf
    
class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf, tipo):
        super().__init__(nome, idade, cpf)
        self.tipo = tipo
        
    def get_tipo(self):
        if self.tipo == 'PF':
            return f"{self.nome} é pessoa física."
        
        else:
            return f"{self.nome} não é uma pessoa física"
        
paulo = PessoaFisica ('Paulo', '12345678910', '28','PF')
print(paulo.get_tipo())
