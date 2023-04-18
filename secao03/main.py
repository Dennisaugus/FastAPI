from fastapi import FastAPI

app = FastAPI()

curos = {
    1: {
        "titulo": "Programação em Python",
        "aulas": "112",
        "horas": "58"

    },
    2: {
        "titulo": "Programação em Java",
        "aulas": "56",
        "horas": "25"
    }
}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True)