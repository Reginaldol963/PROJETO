import sqlite3


class Model_db():

    # Criando banco de dados
    def __init__(self, banco='sys_idiomas.db'):
        self.con = None
        self.cursor = None

        if banco:
            self.open(banco)

    # Conectando ao banco de dados
    def open(self, banco):
        try:
            self.con = sqlite3.connect(banco)
            self.cursor = self.con.cursor()
        except sqlite3.Error as e:
            print(f"não foi pessível se conectar {e}")

    # Criando tabela Aluno
    def aluno_tbl_create(self):
        cur = self.cursor
        cur.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id        INTEGER      PRIMARY KEY NOT NULL,
            nome      TEXT (100)   NOT NULL,
            cpf       INTEGER (11) NOT NULL UNIQUE,
            telefone  INTEGER (11) NOT NULL,
            curso     TEXT (100)   NOT NULL,
            matricula INTEGER (6)  NOT NULL UNIQUE,
            semestre  INTEGER (5)  NOT NULL,
            status    TEXT         NOT NULL DEFAULT matriculada
        );            
        """)

    def criar_apagar_atualizar(self, sql):
        cur = self.cursor
        cur.execute(sql)
        self.con.commit()

    def listar_dados(self, sql):
        cur = self.cursor
        cur.execute(sql)
        return cur.fetchall()


db = Model_db()

db.criar_apagar_atualizar("""
    INSERT INTO alunos 
    (nome, cpf, telefone, curso, matricula, semestre) VALUES 
    ('Reginaldo José', 23846135489, 81998765432, 'Inglês', 55555652754666, 2021.2);
""")
