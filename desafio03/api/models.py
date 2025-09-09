from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# cria a conexão do banco
db = create_engine("sqlite:///banco.db")

# cria a base do banco de dados
Base = declarative_base()

# criar as classes/tabelas do banco
class Usuario(Base):
    __tablename__ = "usuarios"

    id    = Column("id", Integer, primary_key=True, autoincrement=True)
    nome  = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome  = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Produto(Base):
    __tablename__ = "produtos"

    id         = Column("id", Integer, primary_key=True, autoincrement=True)
    nome       = Column("nome", String)
    categoria  = Column("categoria", String)
    disponivel = Column("disponivel", Boolean, default=True)
    preco      = Column("preco", Float)
    loja       = Column("loja", String)

    def __init__(self, nome, categoria, disponivel, preco, loja):
        self.nome       = nome
        self.categoria  = categoria
        self.disponivel = disponivel
        self.preco      = preco
        self.loja       = loja



class Loja(Base):
    __tablename__ = "lojas"

    id      = Column("id", Integer, primary_key=True, autoincrement=True)
    nome    = Column("nome", String)
    cnpj    = Column("cnpj", Integer, unique=True)
    email   = Column("email", String, nullable=False)
    produto = Column("produto", ForeignKey("produtos.id"))

    def __init__(self, nome, cnpj, email, produto):
        self.nome    = nome
        self.cnpj    = cnpj
        self.email   = email
        self.produto = produto



# executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)