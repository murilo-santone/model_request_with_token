import pyodbc

def database_connection():
    """Realiza a conexão com o banco de dados."""
    # Substitua o nome do seu servidor e banco de dados
    server = 'SERVER_NAME' # Exemplo: 'localhost'
    database = 'DATABASE_NAME' # Exemplo: 'mydatabase'

    try:
        # Use 'Trusted_Connection=yes' para autenticação do Windows
        conexao = pyodbc.connect(
        f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server};DATABASE={database};Trusted_Connection=yes;'
        )
        return conexao
    except pyodbc.Error as ex:
        print(f"Erro na conexão com o banco de dados: {ex}")
        return None

def close_conection(conexao):
    """Fecha a conexão com o banco de dados."""
    try:
        conexao.close()
    except pyodbc.Error as ex:
        print(f"Erro ao fechar a conexão com o banco de dados: {ex}")