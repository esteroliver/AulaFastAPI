from repositories.tarefa_repository import TarefaRepositoryInterface
from models.tarefa import Tarefa
from typing import List,Optional

class TarefaService:
    def __init__(self, repository: TarefaRepositoryInterface):
        self.repository = repository

    def listar_tarefas(self) -> List[Tarefa]:
        return self.repository.listar()
    
    def buscar_tarefa(self, id: int) -> Optional[Tarefa]:
        return self.repository.buscar_por_id(id)

    def criar_tarefa(self, titulo: str, descricao: str, concluida: bool) -> Tarefa:
        tarefa = Tarefa(id=0, titulo=titulo, descricao=descricao, concluida=concluida)
        return self.repository.criar_tarefa(tarefa)

    def remover_tarefa(self, id: int):
        return self.repository.remover(id)