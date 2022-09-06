""" Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma classe onde teremos o retorno do documento, o retorno do nome e verificação de tipo de pessoa, onde um método irá receber como parâmetro “F” ou “N” para trazer fumante ou não fumante. Feito isso, crie uma instância e retorne esses valores. """

class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def get_nome(self):
        return f"O nome da pessoa é {self.nome}"
    
    def get_cpf(self):
        return f"O CPF da pessoa é {self.cpf}"
       
class TipoPessoa(Pessoa):
    def __init__(self, nome, cpf, idade, tipo):
        self.tipo = tipo
        super().__init__(nome, cpf, idade) 
    
    def get_tipo(self):
        if self.tipo == 'F':
            return f"{self.nome} é fumante."
        
        if self.tipo == 'N':
            return f"{self.nome} não é fumante." 
        
carmen = TipoPessoa ('Carmen', '11102452412', '36', 'N')
print(carmen.get_tipo())