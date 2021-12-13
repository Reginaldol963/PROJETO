import sqlite3


class Model_db():

    # Criando banco de dados
    def __init__(self, banco='banco/sys_idiomas.db'):
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
   id        INTEGER      PRIMARY KEY AUTOINCREMENT
                           NOT NULL,
    nome      TEXT (100)   NOT NULL,
    cpf       INTEGER (11),
    telefone  INTEGER (11) NOT NULL,
    curso     TEXT (100)   NOT NULL,
    matricula INTEGER (6)  NOT NULL
                           DEFAULT naoinformada,
    semestre  INTEGER (5)  NOT NULL,
    status    TEXT         NOT NULL
                           DEFAULT Matriculado
                           ); """)

    def professores_tbl_create(self):
        cur = self.cursor
        cur.execute("""
       CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY NOT NULL, 
            nome TEXT (100) NOT NULL, 
            cpf INTEGER (11) NOT NULL, 
            telefone INTEGER (11) NOT NULL, 
            cuso TEXT (100) NOT NULL, 
            matricula INTEGER (6) UNIQUE NOT NULL, 
            quant INTEGER (2) NOT NULL, 
            status TEXT (100) NOT NULL);
        """)

    def funcionarios_tbl_create(self):

        cur = self.cursor
        cur.execute("""
             CREATE TABLE IF NOT EXISTS funcionarios (
                  id INTEGER PRIMARY KEY NOT NULL, 
                  nome TEXT (100) NOT NULL, 
                  cpf INTEGER (11) NOT NULL, 
                  telefone INTEGER (11) NOT NULL, 
                  cuso TEXT (100) NOT NULL, 
                  matricula INTEGER (6) UNIQUE NOT NULL, 
                  quant INTEGER (2) NOT NULL, 
                  status TEXT (100) NOT NULL);
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
db.aluno_tbl_create()
db.professores_tbl_create()
