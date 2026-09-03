# Gato.py
"""Definicao da classe Gato"""

class Gato:
    """ Classe exemplo sobre gato """
    especie = "gato" #atributo de classe

    def __init__(self,nome_do_gato,idade_do_gato,
                 cor_do_gato): #construtor
        """Inicializa um objeto da classe Gato"""
        #atributos de instancia
        self.nome = nome_do_gato 
        self.idade = idade_do_gato
        self.cor = cor_do_gato
        self._nome_dos_amigos = []
        self.__numero_de_vidas = 7
        print(f"...Criando {nome_do_gato} como {cor_do_gato}, com {idade_do_gato} anos e {self.__numero_de_vidas} vidas")

    
    def beber_agua(self):
        """Faz o gato beber água"""
        print(f"...{self.nome} está bebendo agua!")
    

    def brincar(self,outro_gato):
        """Faz os gatos brincarem"""
        print(f"...{self.nome} está brincando com {outro_gato.nome}!")
        if outro_gato.nome not in self._nome_dos_amigos:
            print(f"...uma amizade foi criada!")
            self._nome_dos_amigos.append(outro_gato.nome)
        
    

    def atacar(self,outro_gato):
        """Faz o gato atacar e depois brincar"""
        print(f"...{self.nome} está atacando {outro_gato.nome}!")
        self.brincar(outro_gato)
        
        
    @property
    def numero_de_vidas(self):
        """Getter para o atributo __numero_de_vidas"""
        return self.__numero_de_vidas
    
    @numero_de_vidas.setter
    def numero_de_vidas(self,num_vidas):
        """Setter para o atributo __numero_de_vidas"""
        if num_vidas <= 0:
            raise ValueError(f'Numero de vidas ({num_vidas}) deve ser > 0')
        self.__numero_de_vidas = num_vidas
    
    