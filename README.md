# Sistema de Gestão de Eventos Acadêmicos

Projeto Integrador — Desenvolvimento Web II — DSM — FATEC Porto Ferreira 

**Integrantes:** Wallace Petterson e Gabriel SEbastião

## Como rodar

1. `python -m venv venv`
2. `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (macOS/Linux)
3. `pip install -r requirements.txt`
4. `python app.py`
5. Acessar http://127.0.0.1:5000

## Estrutura

- `models/` — classes mapeadas para tabelas (ORM)
- `dao/` — camada de acesso a dados
- `controllers/` — rotas e coordenação das requisições
- `templates/` — páginas HTML (Jinja)
- `docs/` — DER e demais documentação
