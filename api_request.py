import requests

def get_api_key(usuario_id):
    try:
        # URL API para coletar token
        url = 'https://apiexample.apiex.com.br/token'
        
        payload = {
            'ID': 1, # fixo
            'ProjectID': 10, # fixo
            'Login': usuario_id,
            'Password': '1234' # fixo
        }

        # Faz a requisição para obter a token
        response = requests.post(url, json=payload)
        response.raise_for_status()

        chave_api = response.json().get('token') # guarda o token retornado
        return chave_api
    except requests.exceptions.RequestException as ex:
        print(f"Erro ao obter chave para o usuário {usuario_id}: {ex}")
        return None


def make_user_request(chave_api, usuario_id):
    try:
        # URL da API para realizar requisição 
        url = 'https://apiexample.apiex.com.br/sync/finish'
        
        # Inserindo token
        headers = {
            'Auth': f'{chave_api}',
            'Data_format': 'application/json'
        }

        # Parâmetros/JSON para o corpo da requisição
        payload = {
            'ID': 1, # fixo
            'ProjectID': 10, # fixo
            'Login': usuario_id,
            'Password': '1234' # fixo
        }

        # Faz a solicitação para o envio das informações do usuário
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        print(f"Refresh do usuário {usuario_id} concluído com sucesso.")
    except requests.exceptions.RequestException as ex: # Tratamento de exceção para erros de requisição
        print(f"Erro ao realizar refresh do usuário {usuario_id}: {ex}")