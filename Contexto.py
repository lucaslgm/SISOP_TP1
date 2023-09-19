from dataclasses import dataclass

from Mnemonico import Mnemonico
@dataclass
class Contexto:
    pc : Mnemonico
    acc : int
    data : dict[str, int]
    flags : dict[str, Mnemonico]

    def __str__(self):
        return f'pc={self.pc}, acc={self.acc}, data={self.data}, flags={self.flags}'