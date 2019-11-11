# Desafio

Desenvolvemos uma API disponibilizando dados do contexto de clima espacial, disponível em: http://teste-inpe.herokuapp.com/

O objetivo do desafio é consumir os dados dessa API, inserir esses dados em um banco de dados qualquer, resgatar os dados do banco e por fim apresentar uma visualização gráfica de algumas variáveis.


## Minha metodologia

- Utilizando Python, consumi a API com a biblioteca Requests e armazenei em um banco MySQL usando PyMySQL.

- Como sugestão de um dos orientadores do desafio eu criei um servidor com Python Flask e o gráfico com Highcharts JS. Juntando os dois fiz uma rota para minha página (front-end) e nela fiz uma requisição
dos dados que estava consumindo no back-end.

![imagem do grafico](https://github.com/WilliamBarretoH/DesafioINPE/issues/1#issue-521129715)
