from typing import Optional

from pydantic import BaseModel

class Funcionario(BaseModel):
    id: Optional[int] = None 
    nome: str 
    idade: int 
    sexo: str 
    cargo: str 
    anoempresa: int 
    salario: float 