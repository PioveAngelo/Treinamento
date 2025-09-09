from pydantic import BaseModel
from typing import Optional


class UsuarioSchema(BaseModel):
    nome:  str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_atributes = True

class ProdutoSchema(BaseModel):
    nome:       str
    categoria:  str
    disponivel: bool
    preco:      float
    loja:       str

    class Config:
        from_atributes = True

class LojaSchema(BaseModel):
    id_produto: int

    class Config:
        from_atrinutes = True

class LoginSchema(BaseModel):
    email: str
    senha: str

    class Config:
        from_atributes = True