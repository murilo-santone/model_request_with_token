## Objetivo 

Este programa foi criado para demonstrar, de forma prática, como realizar uma requisição com base em três parâmetros principais: código de ID, login e projeto.

Tudo começa com uma consulta ao banco de dados, onde são buscadas as informações do usuário necessário para a operação.

Com esses dados em mãos, o próximo passo é fazer uma requisição de autenticação, que retorna a chave de autorização.

Por fim, com a chave e os dados do usuário, o programa realiza a requisição final, enviando as informações a cada 5 minutos.