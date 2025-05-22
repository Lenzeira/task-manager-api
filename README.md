# Task Manager API

## Descrição do Projeto  
API RESTful desenvolvida com **FastAPI** para gerenciamento colaborativo de tarefas, focada em boas práticas de arquitetura, segurança e qualidade de código.

---

## 🚀 Funcionalidades

- Autenticação com JWT 
- Cadastro e login de usuários 
- Criação, atualização e exclusão de tarefas 
- Associação de tarefas a usuários 
- Organização de tarefas por status e prioridade 

---

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python 3.12 
- **Framework:** FastAPI 
- **Banco de Dados:** PostgreSQL 
- **ORM:** SQLAlchemy 
- **Migrações:** Alembic 
- **Testes:** Pytest 
- **Documentação:** Swagger/OpenAPI (via FastAPI) 
- **Servidor ASGI:** Uvicorn 

---

## Arquitetura do Projeto

O projeto segue o padrão arquitetural MVC/Arquitetura Limpa com organização modular para garantir manutenibilidade e escalabilidade:

- **routers:** Definem os endpoints da API (controladores). 
- **services:** Lógica de negócio da aplicação. 
- **crud:** Operações de acesso e manipulação do banco de dados. 
- **models:** Definição das entidades do banco de dados. 
- **schemas:** Modelos para validação e serialização de dados (Pydantic). 
- **dependencies:** Gerenciamento de dependências, como autenticação e conexão com banco. 

---

## Banco de Dados

Optamos por **PostgreSQL** por sua robustez, confiabilidade e boa integração com o ecossistema Python, especialmente com SQLAlchemy e Alembic para migrações.

O arquivo `db_create.sql` e as migrações gerenciadas pelo Alembic garantem a criação e atualização do schema do banco.

---

## Testes Automatizados

- Testes escritos com **pytest**, cobrindo rotas, serviços e camadas de CRUD. 
- Cobertura atual acima de 60%, conforme requisito. 
- Testes organizados na pasta `tests/` para fácil manutenção 

Para rodar os testes com cobertura 
```bash
pytest --cov=app tests/

git clone https://github.com/Lenzeira/task-manager-api.git
cd task-manager-api
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
