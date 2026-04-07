# models é o arquivo onde fica as classes

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
engine = create_engine("sqlite:///escola.db")
Session = sessionmaker(bind=engine)

#Criando as tabelas do banco
class Cursos(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    carga_horaria = Column(Integer, nullable=False)

    alunos = relationship("Aluno", back_populates="curso")

    def __repr__(self):
        return f"Curso = id: {self.id} - Nome: {self.nome} - Carga Hóraria: {self.carga_horaria}"
    
class Alunos(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)

    curso_id = Column(Integer, ForeignKey("cursos.id"))

    curso = relationship("Curso", back_populates="alunos")
    
    def __repr__(self):
        return f"Aluno = id: {self.id} - Nome: {self.nome} - Email: {self.email}"
    
