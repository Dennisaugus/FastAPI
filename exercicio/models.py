from type import Optional

from pydantic import BaseModel

class Funcionario(BaseModel):
    id: Optional[int] = None 
    none: str 
    idade: int 
    sexo: str 
    cargo: str 
    anoempresa: int 
    salario: float 