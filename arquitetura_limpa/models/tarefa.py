from dataclasses import dataclass

@dataclass
class Tarefa:
    id: int
    titulo: str
    descricao: str
    concluida: bool = False