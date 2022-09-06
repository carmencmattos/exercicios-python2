""" Crie um professor de classe com atributos nome, idade e salário, onde o salário deve ter um método privado que não pode ser acessado fora da classe.
a. Crie um método para acessar o método privado, onde é passada a identificação do usuário se ele pode ou não acessar."""

class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        
    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.idade
    
    def __get_salario(self):
        return "Aqui está o valor do seu salário."
    
    def access_salario(self, nome):
        if nome == "Marcus":
            return self.__get_salario()
        else:
            return ("Usuário sem permissão")

professor = Professor('Marcus', '34', '4000')      
access = professor.access_salario("João")
print(access)
            