# desafio-tor
Desafio:
O objetivo deste challenge é desenvolver uma aplicação que nos permita obter uma lista de
IPs de redes Tor (https://www.torproject.org/) a partir de fontes externas, distintas e
apresentá-los de maneira unificada. Adicionalmente esta aplicação deve possibilitar a
indicação de IPs de redes que NÃO queremos que apareçam na lista.
O objetivo é desenvolver uma API REST que tenha os métodos detalhados a seguir:
1) Um endpoint GET que devolve todos os IPs de TOR obtidos das fontes externas
detalhadas abaixo:
● https://www.dan.me.uk/tornodes
● https://torstatus.blutmagie.de

2) Um endpoint POST que receba um IP e o agregue à uma base de dados onde se
encontram todos os IPs que não queremos que apareçam no output do endpoint 3
(detalhado abaixo).
3) Um endpoint GET que devolve os IPs obtidos das fontes externas EXCETO os que
se encontram na base de dados (IPs carregados utilizando o endpoint 2)
A base de dados a ser utilizada fica à sua escolha.
A aplicação desenvolvida deve executar em um container de Docker.
Resolução:
O desafio foi concluído utilizando a biblioteca Django do Python, especialmente usando a framework Django REST. 
Foi feito uma API que possui um método GET que retorna todos os IPs, aqueles obtidos de fontes externas e os armazenados no banco de dados. Outros dois métodos GET foram implementados, um retornando os dados obtidos de fontes externas e o outro os dados armazenados no banco de dados.
Por último foi feito na API um método POST, que armazena um dado IP na base de dados interna.
Além da API, os mesmos métodos foram implementados utilizando o Django convencional, mostrando os IPs atráves dos Django Templates.