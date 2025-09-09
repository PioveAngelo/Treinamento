from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import pegar_sessao, verificar_token
from schemas import ProdutoSchema, LojaSchema
from models import Produto, Usuario


products_router = APIRouter(prefix="/products", tags=["products"], dependencies=[Depends(verificar_token)])

@products_router.get("/")
async def produtos():
    '''
        Essa é a rota padão de produtos do sistema. As rotas de produtos precisam de autenticação.
    '''
    return {"mensagem" : "Você acessou a rota de produtos"}



@products_router.post("/produto")
async def criar_produto(produto_schema: ProdutoSchema, session: Session = Depends(pegar_sessao)):
    produto = Produto(produto_schema.nome, produto_schema.categoria, produto_schema.disponivel, produto_schema.preco, produto_schema.loja)
    session.add(produto)
    session.commit()
    return {"mensagem": f"Produto criado com sucesso. ID do produto: {produto.id}"} 

@products_router.get("/listar")
async def listar_produtos(session: Session = Depends(pegar_sessao)):
    
    produtos = session.query(Produto).all()

    return {
        "produtos": produtos
    } 