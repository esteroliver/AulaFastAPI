from typing import List, Optional
from models.tarefa import Tarefa

# INTERFACE
class TarefaRepositoryInterface:
    def listar(self) -> List[Tarefa]:
        raise NotImplementedError

    def buscar_por_id(self, id: int) -> Optional[Tarefa]:
        raise NotImplementedError

    def salvar(self, tarefa: Tarefa) -> Tarefa:
        raise NotImplementedError

    def remover(self, id: int) -> None:
        raise NotImplementedError

# REPOSITORY
class TarefaRepository(TarefaRepositoryInterface):
    def __init__(self):
        self.tarefas = []

    def listar(self) -> List[Tarefa]:
        return self.tarefas

    def buscar_por_id(self, id: id) -> Optional[Tarefa]:
        for tarefa in self.tarefas:
            if tarefa.id == id:
                return tarefa
        return None

    def salvar(self, tarefa: Tarefa) -> Tarefa:
        for i,t in enumerate(self.tarefas):
            if t.id == tarefa.id:
                self.tarefas[i] = tarefa
                return tarefa
        self.tarefas.append(tarefa)
        return tarefa

    def remover(self, id: str) -> None:
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa.id != id]