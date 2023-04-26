from fastapi import FastAPI 
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Path

from models import Funcionario
from typing import List,Optional


app = FastAPI()

funcionarios = {
    1: {
        "nome": "Dennis Augusto Gusmão",
        "idade": 28,
        "sexo": "Masculino",
        "cargo": "Engenheiro DevSecOps",
        "anoempresa": 1,
        "salario": 8000.0
    },
    2: {
        "nome": "Sara Andrade",
        "idade": 25,
        "sexo": "Feminino",
        "cargo": "Engenheira de Software",
        "anoempresa": 2,
        "salario": 8000.0
    },
    3: {
        "nome": "Caio Vinicios",
        "idade": 24,
        "sexo": "Masculino",
        "cargo": "Desenvolvedor PL",
        "anoempresa": 2,
        "salario": 7500.0
    },
    4: {
        "nome": "Marianna Dias Barbosa",
        "idade": 26,
        "sexo": "Feminino",
        "cargo": "Cientista de Dados",
        "anoempresa": 3,
        "salario": 8000.0
    },
    5: {
        "nome": "Ederley Carvalho",
        "idade": 35,
        "sexo": "Masculino",
        "cargo": "Tech Lider DevSecOps",
        "anoempresa": 1,
        "salario": 10000.0
    },
    6: {
        "nome": "Camila Monteiro",
        "idade": 34,
        "sexo": "Feminino",
        "cargo": "Recursos Humanos",
        "anoempresa": 4,
        "salario": 6000.0
    }
}

@app.get('/funcionarios')
async def get_funcionarios():
    return funcionarios

@app.get('/funcionarios/{funcionario_id}')
async def get_funcionario(funcionario_id: int = Path(title='Id do funcionário: ' ,description='Deve ser entre 1 a 6:', gt=0, lt=7)):
    try:
        funcionario = funcionarios[funcionario_id]
        funcionario.update({"id": funcionario_id})
        return funcionario
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail='Funcionario não existente')
    
@app.post('/funcionarios', status_code=status.HTTP_201_CREATED)
async def post_funcionario(funcionario: Funcionario):
    next_id: int = len(funcionarios) + 1
    funcionarios[next_id] = funcionario
    del funcionario.id
    return funcionario

@app.put('/funcionarios/{funcionario_id}')
async def put_funcionario(funcionario_id: int, funcionario: Funcionario):
    if funcionario_id in funcionarios:
        funcionarios[funcionario_id] = funcionario
        del funcionario.id

        return funcionario
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe este funcionario com o id{funcionario_id}')

@app.delete('/funcionarios/{funcionario_id}')
async def delete_funcionario(funcionario_id: int):
    if funcionario_id in funcionarios:
        del funcionarios[funcionario_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe este funcionario com o id{funcionario_id}')




if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8008, reload=True)