# Guia para utilizar o parser

Como executar: 

1) (Parser) 

	python3 main.py domain.pddl problem.pddl 

2) (Propositional Planner) 

	python3 main.py domain.pddl problem.pddl -p

O arquivo main.py realiza o parse de formalizações e apresenta diferentes possibilidades de se acessar as informações que foram obtidas - utilizando métodos get - incluindo comentários explicando o que é retornado ao utilizar os getters. Qualquer dúvida ou sugestão para adicionar algum método getter a mais: jonathanalmd@gmail.com

Exemplos de execução:

    python3 main.py examples/galaxy/galaxy.pddl examples/galaxy/galaxy-p1.pddl

    python3 main.py examples/galaxy/galaxy.pddl examples/galaxy/galaxy-p1.pddl -p


Obs:
O parser implementa apenas a tipagem básica (sem tipo de tipos) e apeanas os operadores básicos da linguagem PDDL: and, not e = 

Para mais detalhes da implementação: monografia em breve será publicada em http://www.bdm.unb.br 
