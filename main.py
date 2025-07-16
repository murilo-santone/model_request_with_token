import database
import api_request
import pyodbc
import time

def userquery():
    conexao = database.database_connection()
    if conexao:
        try:
            cursor = conexao.cursor()
            # Consulta que retornará os usuários
            cursor.execute("""SELECT DISTINCT IR.UserID
                                FROM TB_RequestUser tb with(nolock)
                                WHERE tb.seq = 0 
                                AND tb.enabled = 1""")
            userRequest = [str(row[0]).lstrip('0') for row in cursor.fetchall()]
            return userRequest
        except pyodbc.Error as ex:
            print(f"Erro na consulta ao banco de dados: {ex}")
        finally:
            database.close_conection(conexao)

def main():
    try:
        # Consulta usuários para requisição
        userRequest = userquery()

        # Para cada usuário, obtem a chave e realiza o envio da requisição
        for user_id in userRequest:
            chave_api = api_request.get_api_key(user_id)
            if chave_api:
                # Realiza o envio da requisição do usuário usando a chave obtida
                api_request.make_user_request(chave_api, user_id)  
    except Exception as ex: # Tratamento genérico de exceções
        print(f"Ocorreu um erro inesperado: {ex}")
    finally: 
        # Fechando a conexão com o banco de dados
        print("Fechando a conexão com o banco de dados.")

if __name__ == "__main__":

    while True:
        try:
            print("Executando a tarefa...")
            main()
            print("Aguarde 5 minutos para o novo refresh")
            time.sleep(300)  # Pausa por 5 minutos (300 segundos)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")