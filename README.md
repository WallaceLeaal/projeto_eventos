# Sistema de Gestão de Eventos Acadêmicos

Projeto Integrador — Desenvolvimento Web II — DSM — FATEC Porto Ferreira
Professor: Vagner dos Santos

**Integrante:** Wallace Petterson Leal Chaves

## Como rodar

1. `python -m venv venv`
2. `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (macOS/Linux)
3. `pip install -r requirements.txt`
4. `python app.py`
5. Acessar http://127.0.0.1:5000

O banco SQLite (`instance/eventos.db`) é criado automaticamente na primeira execução.

## Estrutura

- `models/` — classes mapeadas para tabelas via ORM (Evento, Participante, Inscricao)
- `data/` — camada de acesso a dados (EventoDAO)
- `controllers/` — rotas e coordenação das requisições (Blueprint)
- `templates/` — páginas HTML (Jinja)
- `docs/DER.md` — Diagrama Entidade-Relacionamento

## Funcionalidades (Etapa 2)

- CRUD completo de eventos: listar, cadastrar, editar e excluir
- Dados persistidos em banco de dados (SQLite via Flask-SQLAlchemy)
- Acesso a dados isolado na camada DAO

## ORM x SQL direto

O ORM gera o SQL por baixo dos panos: trabalhamos com objetos (`evento.nome`)
em vez de tuplas (`linha[1]`), com menos código repetitivo. O custo é uma camada
de abstração a mais, que pode esconder consultas ineficientes (problema N+1).
