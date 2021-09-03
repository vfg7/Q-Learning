Explore/Exploit? - Decisions with Q-Learning 

O caso 

Imaginemos o seguinte mapa:

![image](https://user-images.githubusercontent.com/62081666/131943397-0e98fe30-4790-48f1-a2ca-e3ce6ce0a737.png)

Como partir do inicio e chegar a um dos estados terminais? Em quantos passos? 

Os desafios do caso:

* Foi escolhido um exemplo pequeno, porém escalável, para representar o uso do algoritmo. Exemplos maiores certamente trariam maior complexidade de tempo à solução.
* Processos de decisão e aprendizado reforçado passam pelo tradeoff explore/exploit, que o Q-Learning executa: explora o mapa várias vezes e vai sempre atualizando os caminhos de acordo com as iterações. 
* A taxa de aprendizado é um fator fundamental para o funcionamento do algoritmo. Testei com duas taxas diferentes para ver como o algoritmo convergia até o valor ótimo para avaliar. Outros parâmetros sensíveis são os fatores alfa e gama, da equação de Bellman.


Documentação 

O projeto foi feito em Python, versão 3.7.0

Foram usadas as bibliotecas:

* random
* 
O projeto foi feito no pycharm, então, clonar este repositório e abrir como um novo projeto na referida IDE deve ser o bastante para sua reprodução

Próximos passos

* Por mais que esteja comentado, reconheço que o código precisa de uma refatoração, seja para reescrever alguns métodos de forma mais sucinta, seja para ajudar na legibilidade do código
* Muitas funções foram implementadas do zero e não busquei bibliotecas para o problema, deixando o código em baixo nível. Enquanto considero que há notáveis vantagens em implementar seu código, também reconheço que o uso de bibliotecas e funções pode facilitar a resolução do problema.
* O código foi feito com um número controlado de iterações por que quis acompanhar manualmente o aprendizado, mas seria uma boa ideia deixá-lo enlaçado para rodar automaticamente até a geração de uma solução ótima
