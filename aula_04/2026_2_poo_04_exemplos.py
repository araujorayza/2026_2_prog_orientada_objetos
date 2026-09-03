# 2026_2_poo_04_exemplos.py
"""Exemplo sobre objetos"""

from pasta_gato.gato_module import Gato

gato1 = Gato("Gato",3,"laranja") #cria objeto
gato2 = Gato("Tom",4,"branco")

print("\n\n")

print(f"O nome do gato1 é {gato1.nome}")
print(f"O nome do gato2 é {gato2.nome}")
print("\n")
gato1.nome = "Bob"
print(f"O nome do gato1 agora é {gato1.nome}")
print(f"O nome do gato2 ainda é {gato2.nome}")

print("\n\n")

print(f"A especie do gato2 é {gato2.especie}")
print(f"A especie do gato1 é {gato1.especie}")
Gato.especie = "felis catus"
print("\n")
print(f"A especie do gato2 agora é {gato2.especie}")
print(f"A especie do gato1 agora é {gato1.especie}")

print("\n\n")

gato1.beber_agua()
print("\n")
gato2.brincar(gato1)
print("\n")
gato2.atacar(gato1)

print("\n\n")

print(gato2._nome_dos_amigos)
print(gato1._nome_dos_amigos)

print("\n\n")

# print(gato1.__numero_de_vidas)
# print("\n\n")

print(gato1.numero_de_vidas)
gato1.numero_de_vidas = 9
print(gato1.numero_de_vidas)

