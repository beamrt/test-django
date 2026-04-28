class Pessoa:

    def __init__ (self, nome, idade):
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        return self._nome
    def get_idade(self):
        return self._idade
    def __str__(self):
        return self._nome
    def __repr__(self):
        return self._nome

jose = Pessoa('José', 10)
maria = Pessoa('Maria', 20)

print(jose.get_nome())

class SuperPoderes:
     def sabe_voar(self):
        return 'sei voar'
    
    def sabe_nadar(self):
        return 'sei nadar'

class Professor(Pessoa, SuperPoderes):
    pass

professor_xavier = Professor('Professor Xavier', 100)