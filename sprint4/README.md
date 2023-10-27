# Projeto Commander

## Introdução
Nosso projeto para o challenge é um aplicativo voltado ao
campo da gestão veicular. Resolvemos desenvolver um sistema
mobile para registrar, prever e agendar manutenções, a partir
dos dados inseridos pelo usuário. Nosso aplicativo foi
desenvolvido em dart com o framework flutter.<br><br>
Para o sprint de CTFE trouxemos algumas funções do nosso app para
o python. Neste projeto, incluimos o cadastro de informações
iniciais do veículo, o registro de manutenções, e a exibição
da quilometragem sugerida para as próximas manutenções.<br><br>
Utilizamos recursos do python para validar as entradas do
usuário, além de dados padrões estabelecidos em dicinários,
que são manipulados conforme as funções definidas são
chamadas. Essas funções também são utilizadas para formatar
e imprimir na tela os dados solicitados nos menus. O arquivo
está dividido para facilitar o entendimento do código, em
busca de mantê-lo legível.

## Instruções de uso:
Ao iniciar a aplicação, será impresso um menu, contendo as
funcionalidades. Se qualque opção for escolhida antes do cadastro,
aparecerá uma mensagem de erro, instruindo o usuário a cadastrar
o veículo. Após realizar o cadastro, o usuário pode registrar
as manutenções realizadas em seu veículo, e exibir uma tabela
com as informações cadastradas, além da previsão de quando
a próxima manutenção deve ser realizada.<br><br>
Em todas as entradas há um validador, para evitar ao máximo
o encontro do usuário com erros críticos. Nos campos que incluem
data, por exemplo, não é possível inserir uma data superior à atual.
