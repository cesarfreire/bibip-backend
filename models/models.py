from sqlmodel import SQLModel, Field


class Veiculo(SQLModel, table=True):
    placa: str = Field(nullable=False, unique=True, primary_key=True)
    cor: str = Field(nullable=False)
    modelo: str = Field(nullable=False)
    valor: str = Field(nullable=False)
    multas: int = Field(default=0)
    pendencias_financeiras: float = Field(default=0)
