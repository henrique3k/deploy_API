# deploy_API
simples API criada para auxiliar na agilidade de deploy, recebendo via Http todos os parâmetros necessários para funcionamento e persistindo em um simples banco de dados. 

## Parâmetros:

**c** - Componente: Componente que está em processo de deploy

**v** - Versão: Versão que está sendo entregue

**r** - Rsponsável: Nome do membro do time de engenharia que está realizando o processo de deploy

**s** - Status: Status do processo de deploy


Como uma das premissas foi não agregar complexidade desnecessária ao projeto, levando em conta o tamanho dos pacotes e a instalação do container, optei por utilizar a linguagem **Python** e o framework **Flask** para estar criando a API, assim como os dados recebidos são persistidos em um banco de dados simples MongoDB, O que também facilita a exportação dos dados para uma planilha.


Dockerfile e docker-compose incluso no projeto.

é possível acompanhar o andamento da aplicação através do arquivo de Log.
OBS: a API rodará na porta default 0.0.0.0:5000

## Como Usar

#docker-compose build 

#docker-compose up

**Exemplo do endpoint via http:** 
http://localhost:5000/api/v1.0/deploy?c=deploy_api_test&v=1.3&r=HenriqueFernandes&s=dev&

**Exemplo de chamada via cURL**
curl --request GET \
  --url 'http://localhost:5000/api/v1.0/deploy?c=deploy_api_test&v=1.3&r=HenriqueFernandes&s=dev'
  
  
  ## **EXTRA:**
  Para retorno dos dados no navegador, basta realizar a chamada da seguinte forma: 
  http://localhost:5000/api/v1.0/export
