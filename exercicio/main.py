from fastapi import FastAPI 
from fastapi import HTTPException
from fastapi import status

app = FastAPI()

funcionario = {
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
async def funcionarios_aquarela():
    return funcionario

@app.get('/funcionarios/{funcionario_id}')
async def get_funcionarios(funcionario_id: int):
    try:
        funcionarios = funcionario[funcionario_id]
        funcionarios.update({"id_funcionario": funcionario_id})
        return funcionarios
    
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Funcionário não encontrado na base de dados')

    

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8008, reload=True)