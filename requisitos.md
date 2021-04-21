# Requisitos
Lista de features que serão implementadas

## Concluídos
* Configurar a aplicação para rodar todos os serviços em Docker
* Entender funcionando do framework e possibilitar a listagem de todos os models via API
* Melhorar os teste. Como o algumas tabelas do database não estao formalizadas, foi necessário setar managed=False
no django. Isso faz com que nos testes ele não popule o banco de teste, por isso a criação das tabelas na classe CreateTestDb.


## To do
* Melhorar os teste
* criar classes que definem o core da aplicação, como uma classe mãe para os endpoints
* separar melhor os módulos da api por recurso/método http
* Criar paginação nos endpoints
* Criação de uma DOC (swagger)
* Deploy de diferentes environments
* Acesso aos endpoints (sistemas de usuários e autenticação)