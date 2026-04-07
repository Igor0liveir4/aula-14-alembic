from models import Session, Curso, Aluno

def cadastrar_curso():
    with Session() as session:
        try:
            nome_curso = input("Digite o nome do curso: ").capitalize()
            carga_horaria = int(input("Digite a carga horaria do curso: "))
            descricao = input("Digite a descrição do curso: ").capitalize()
            
            curso = Curso(nome = nome_curso, carga_horaria = carga_horaria, descriacao = descricao)
            session.add(curso)
            session.commit()
            print(f"Curso criado com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"ocorreu um erro {erro}")
        

cadastrar_curso()