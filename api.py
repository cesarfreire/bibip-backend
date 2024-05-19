from sqlmodel import Session
from fastapi import FastAPI, Response, status
from db import engine, SQLModel
from models.models import Veiculo
import random

SQLModel.metadata.create_all(engine)

app = FastAPI()


def sorteia_cor():
    cores = ["Vermelho", "Azul", "Verde", "Amarelo", "Preto", "Branco"]
    cor_sorteada = random.choice(cores)
    return cor_sorteada


def sorteia_modelo():
    modelos = ["Chevette", "Kadett", "Puma GTE", "Opala", "Fusca", "Brasilia"]
    modelo_sorteado = random.choice(modelos)
    return modelo_sorteado


def sorteia_valor():
    valor_sorteado = random.randint(10000, 50000)
    return valor_sorteado


def sorteia_multas():
    multas_sorteado = random.randint(0, 10)
    return multas_sorteado


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/veiculos/{placa_veiculo}")
def get_veiculo(placa_veiculo: str, response = Response):
    with Session(engine) as session:
        veiculo = session.get(Veiculo, placa_veiculo.lower())
        if not veiculo:
            multas = sorteia_multas()
            new_veiculo = Veiculo(
                placa=placa_veiculo,
                cor=sorteia_cor(),
                modelo=sorteia_modelo(),
                valor=sorteia_valor(),
                multas=multas,
                pendencias_financeiras=multas * 150.00
            )
            session.add(new_veiculo)
            session.commit()
            session.refresh(new_veiculo)
            response.status_code = status.HTTP_201_CREATED
            return new_veiculo
        response.status_code = status.HTTP_200_OK
        return veiculo


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
