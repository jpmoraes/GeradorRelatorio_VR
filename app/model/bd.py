import sqlite3

class BancoAvaliacao:
    def __init__(self, nome_banco="avaliacao.db"):
        self.nome_banco = nome_banco

    def criar_tabela(self):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS avaliacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                experiencia_geral INTEGER,
                contribuicao_engajamento INTEGER,
                expectativa_feedback INTEGER,
                motivacao_aprendizado INTEGER,
                aspectos_mais_gostou TEXT,
                interesse_futuro INTEGER,
                data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

        conexao.commit()
        conexao.close()
        print("Tabela 'avaliacoes' criada com sucesso no banco:", self.nome_banco)

# Executar criação do banco/tabela
if __name__ == "__main__":
    banco = BancoAvaliacao()
    banco.criar_tabela()
