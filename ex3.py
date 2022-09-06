""" Escreva uma classe “PessoaJuridica” e herde Pessoa, agora modificando o comportamento, retorne o cnpj. Crie uma instância e acesse os dados. """

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
       
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
class PessoaJuridica(Pessoa):
    def __init__(self, nome, idade, cnpj, tipo):
        super().__init__(nome, idade)
        self.cnpj = cnpj
        self.tipo = tipo
        
    def get_cnpj(self):
        return self.cnpj
    
    def get_tipo(self):
        if self.tipo == 'PJ':
            return f"{self.nome}, {self.cnpj}, é uma pessoa jurídica."
        else:
            return f"{self.nome} não é uma pessoa jurídica." 
        
auroraconsulting = PessoaJuridica ('Aurora Consulting', '1', '12345678000100', 'PJ')
print(auroraconsulting.get_tipo())