# Configurar o alembic

# Instalar a biblioteca 
# pip install sqlalchemy alembic

# No terminal inicie o alembic
# pyton -m alembic init alembic (migration)

# Configurando a conexão com db
# ---------------------------------

# abra o arquivo alembic.ini
# e pocure a linha com essa informação:
# sqlalchemy.url = driver://user:pass@localhost/dbname

# Conectando o alembic ao sqlalchemy
# --------------------------------------

# Abre o arquivo:
# alembic/env.py

# Importe a Base no arquivo env.py
# from models import Base
# Encontre a linha com:
# target_metadata = None
# e altere para:
# target_metadata = Base.metadata