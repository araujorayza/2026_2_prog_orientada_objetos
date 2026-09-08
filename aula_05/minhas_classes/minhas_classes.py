# minhas_classes.py
"""Definicao da classes Televisao e ControleRemoto"""

class Televisao:
    """Classe exemplo sobre uma televisao cujo canal e volume podem ser alterados"""
    def __init__(self, canal_inicial: int = 1, volume_inicial: int = 10):
              
        # Atributos protegidos/privados
        self._canal = canal_inicial
        self._volume = volume_inicial
        self._ligada = False
        
        # Limites operacionais do sistema
        self.CANAL_MIN = 1
        self.CANAL_MAX = 100
        self.VOL_MIN = 0
        self.VOL_MAX = 50
        
        print(f"[TV] A televisão {self} foi criada.")

    def liga_desliga(self):
        self._ligada = not self._ligada
        status = "ligada" if self._ligada else "desligada"
        print(f"[TV] A televisão está {status}.")

    # Getters para consulta de estado (pelo controle)
    @property
    def canal(self) -> int:
        return self._canal

    @property
    def volume(self) -> int:
        return self._volume

    @property
    def ligada(self) -> bool:
        return self._ligada

    # Métodos de controle de estado com validação
    def alterar_volume(self, delta: int):
        if not self._ligada:
            print("[TV Error] A TV está desligada.")
            return
        
        novo_volume = self._volume + delta
        if self.VOL_MIN <= novo_volume <= self.VOL_MAX:
            self._volume = novo_volume
            print(f"[TV] Volume: {self._volume}")
        else:
            print(f"[TV Aviso] Limite de volume atingido ({self._volume}).")

    def definir_canal(self, novo_canal: int):
        if not self._ligada:
            print("[TV Erro] A TV está desligada.")
            return

        if self.CANAL_MIN <= novo_canal <= self.CANAL_MAX:
            self._canal = novo_canal
            print(f"[TV] Canal alterado para: {self._canal}")
        else:
            print(f"[TV Erro] Canal {novo_canal} inválido.")


class ControleRemoto:
    """Classe exemplo sobre um controle remoto que controla uma televisao"""
    def __init__(self, tv: Televisao):
        # Associação com o objeto Televisao
        print(f"[CONTROLE] Criando um controle associado a tv {tv}...")
        self._tv = tv

    def aperta_onoff(self):
        self._tv.liga_desliga()

    def aumentar_volume(self):
        self._tv.alterar_volume(1)

    def diminuir_volume(self):
        self._tv.alterar_volume(-1)

    def sintonizar_canal(self, canal: int):
        self._tv.definir_canal(canal)

    def aumentar_canal(self):
        self._tv.definir_canal(self._tv.canal + 1)

    def diminuir_canal(self):
        self._tv.definir_canal(self._tv.canal - 1)

    def exibir_status(self):
        status = "Ligada" if self._tv.ligada else "Desligada"
        print(f"\n--- Status Atual ---")
        print(f"Power: {status} | Canal: {self._tv.canal} | Volume: {self._tv.volume}")
        print("--------------------\n")