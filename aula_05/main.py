# main.py
"""Uso das classes Televisao e ControleRemoto"""

from minhas_classes.minhas_classes import Televisao,ControleRemoto

# Instanciação do objeto Televisão
minha_tv = Televisao(canal_inicial=5, volume_inicial=1)

# Instanciação do Controle Remoto associado à TV criada
controle = ControleRemoto(minha_tv)
 
# Tentando interagir com a TV desligada
print("=== Teste 1: TV Desligada ===")
controle.aumentar_volume()

# Ligando a TV
print("\n=== Teste 2: Ligando e Ajustando Volume ===")
controle.aperta_onoff()
controle.aumentar_volume()
controle.aumentar_volume()
controle.diminuir_volume()

# Troca de canais
print("\n=== Teste 3: Mudança de Canais ===")
controle.sintonizar_canal(42)
controle.aumentar_canal()
controle.diminuir_canal()

# Tentativa de sintonia fora dos limites operacionais
print("\n=== Teste 4: sintonia fora dos limites operacionais ===")
controle.sintonizar_canal(150)

# Tentativa de alterar o volume para fora dos limites operacionais
print("\n=== Teste 5: volume fora dos limites operacionais ===")
controle.diminuir_volume()
controle.diminuir_volume()
controle.diminuir_volume()

# Checagem de status via controle
controle.exibir_status()