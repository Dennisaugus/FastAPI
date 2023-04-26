from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import status

from models import Curso
from typing import List, Optional


app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação em Python",
        "aulas": 112,
        "horas": 58

    },
    2: {
        "titulo": "Programação em Java",
        "aulas": 56,
        "horas": 25
    },
    3: {
        "titulo": "Programação em C#",
        "aulas": 34,
        "horas": 34
    }
}

# Trás todos os recursos
@app.get('/cursos')
async def get_cursos():
    return cursos 

# Trás recursos expecíficos 
@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        return curso 
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')
 
# Novo endpoint
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
   next_id: int = len(cursos) + 1
   cursos[next_id] = curso
   del curso.id #Remove a visualização do id null
   return curso
    

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe este curso com o id {curso_id}')
    

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
       #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT) em faze de bug ainda 0.95.0
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Não existe este curso com o id {curso_id}')


@app.get('/calculadora')
async def calcular(a: int,b: int,c: Optional[int]):
    soma = a + b
    if c:
        soma += c
        
    return {"resultado": soma}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)