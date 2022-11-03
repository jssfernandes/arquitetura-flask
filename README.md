# Arquitetura Definitiva para Projetos Flask
---

## Clone

```bash
git clone https://github.com/jssfernandes/arquitetura-flask.git
```

## ou faça o download

https://github.com/jssfernandes/arquitetura-flask/archive/main.zip

ou

```bash
wget https://github.com/jssfernandes/arquitetura-flask/archive/main.zip
```

## Ambiente

Python 3.6+
Ative a sua virtualenv

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
pip install -r requirements_test.txt
```

## Testando

```bash
pytest customer/tests
```

## Executando

```bash
flask create-db  # rodar uma vez para criar a estrutura das tabelas
flask populate-db # rodar uma vez para incluir alguns dados ficticios
flask add-user -u admin -p 1234  # adiciona usuario admin para logar no painel administrativo
flask run
```

Acesse:

- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/
  - user: admin, senha: 1234
- API GET:
  - http://localhost:5000/api/v1/customers/
  - http://localhost:5000/api/v1/customers/1
  - http://localhost:5000/api/v1/customers/2
  - http://localhost:5000/api/v1/customers/3


## Structure

```bash
.
├── Makefile
├── customer  (MAIN PACKAGE)
│   ├── app.py  (APP FACTORIES)
│   ├── blueprints  (BLUEPRINT FACTORIES)
│   │   ├── __init__.py
│   │   ├── restapi  (REST API)
│   │   │   ├── __init__.py
│   │   │   └── resources.py
│   │   └── webui  (FRONT END)
│   │       ├── __init__.py
│   │       ├── templates
│   │       │   ├── index.html
│   │       │   └── customer.html
│   │       └── views.py
│   ├── ext (EXTENSION FACTORIES)
│   │   ├── admin.py
│   │   ├── appearance.py
│   │   ├── auth.py
│   │   ├── commands.py
│   │   ├── configuration.py
│   │   ├── database.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models.py  (DATABASE MODELS)
│   └── tests  (TESTS)
│       ├── conftest.py
│       ├── __init__.py
│       └── test_api.py
├── README.md
├── requirements_dev.txt
├── requirements_test.txt
├── requirements.txt
└── settings.toml  (SETTINGS)

7 directories, 26 files
```
